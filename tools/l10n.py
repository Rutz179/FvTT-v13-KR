#!/usr/bin/env python3
"""
FvTT 한글화 유지보수 도구  (Python 3.9+, 표준 라이브러리만 사용)

  python tools/l10n.py status              현재 번역 현황
  python tools/l10n.py sync                ko.json 을 en.json 구조/순서에 맞춰 재구성
  python tools/l10n.py export              번역할 문자열을 DeepL 붙여넣기용 txt 로 추출
  python tools/l10n.py import              DeepL 결과(*_ko.txt)를 ko.json 에 반영
  python tools/l10n.py deepl               (선택) DeepL API 로 자동 번역 후 반영
  python tools/l10n.py check               오류 검사 (CI 에서도 사용)

핵심 아이디어
  * 모든 비교는 "평탄화된 키"(EDITOR.Markdown) 기준으로 합니다.
    en.json 이 {"EDITOR.Markdown": ...} 이든 {"EDITOR": {"Markdown": ...}} 이든 같은 키로 취급하고,
    ko.json 은 항상 en.json 과 똑같은 모양·순서로 다시 씁니다.
  * sync 가 끝나면 그때의 en.json 을 l10n/en.synced.json 에 스냅샷으로 저장합니다.
    다음 업데이트 때는 이 스냅샷과 새 en.json 을 비교해서
      - 영어 문장이 그대로인데 키만 바뀐 것  → 번역 자동 이전
      - 영어 문장이 바뀐 것                → '재검토 필요(stale)'로 표시, export 에 포함
    를 정확하게 찾아냅니다.
"""
from __future__ import annotations

import argparse
import html
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from collections import Counter, OrderedDict, defaultdict
from pathlib import Path

_KEEP: set = set()
ROOT = Path(__file__).resolve().parent.parent
EN = ROOT / "lang" / "en.json"
KO = ROOT / "lang" / "ko.json"
L10N = ROOT / "l10n"
BASE = L10N / "en.synced.json"      # ko.json 이 마지막으로 맞춰진 en.json 스냅샷
STALE = L10N / "stale.json"          # 영어가 바뀌어 재번역이 필요한 키 목록
GLOSSARY = L10N / "glossary.json"
DEEPL_DIR = L10N / "deepl"
REPORT = L10N / "sync-report.md"

PH_RE = re.compile(r"\{[\w.\-]+\}")                 # {name}, {count} ...
ATTR_TAG_RE = re.compile(r"<[a-zA-Z][\w-]*\s[^<>]*=[^<>]*>")   # 속성이 있는 태그 <a href="...">
TAG_RE = re.compile(r"</?[a-zA-Z][\w-]*(?:\s[^<>]*=[^<>]*)?\s*/?>")
HANGUL = re.compile(r"[가-힣]")
MASK_RE = re.compile(f"{ATTR_TAG_RE.pattern}|{PH_RE.pattern}")
ANY_TAG_OR_PH = re.compile(r"(<[^<>]*>)|(\{[\w.\-]+\})")
LINE_RE = re.compile(r"^\s*\[(\d+)\]\s?(.*)$")


# ─────────────────────────── JSON 입출력 ───────────────────────────

def _lenient_fix(text: str) -> str:
    """손으로 편집하다 생기는 흔한 실수(빠진 쉼표, 남는 쉼표)를 고쳐 봅니다."""
    text = text.replace("\r\n", "\n")
    text = re.sub(r",(\s*[}\]])", r"\1", text)
    for _ in range(1000):
        try:
            json.loads(text)
            return text
        except json.JSONDecodeError as e:
            if not e.msg.startswith("Expecting ',' delimiter"):
                raise
            lines = text.split("\n")
            j = e.lineno - 2
            while j >= 0 and not lines[j].strip():
                j -= 1
            lines[j] = lines[j].rstrip() + ","
            print(f"  ! {j + 1}번째 줄 끝에 빠진 쉼표를 추가했습니다: {lines[j].strip()[:60]}")
            text = re.sub(r",(\s*[}\]])", r"\1", "\n".join(lines))
    raise RuntimeError("JSON 자동 수리 실패")


def load_json(path: Path, lenient: bool = False):
    text = path.read_text(encoding="utf-8-sig")
    try:
        return json.loads(text, object_pairs_hook=OrderedDict)
    except json.JSONDecodeError as e:
        if not lenient:
            sys.exit(f"[오류] {path.relative_to(ROOT)} JSON 문법 오류: {e.lineno}줄 {e.colno}칸 - {e.msg}")
        print(f"[경고] {path.name} 에 JSON 문법 오류가 있어 자동 수리를 시도합니다 ({e.lineno}줄: {e.msg})")
        return json.loads(_lenient_fix(text), object_pairs_hook=OrderedDict)


def dump_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    path.write_text(text, encoding="utf-8", newline="\n")


def flatten(node, prefix: str = "", out=None) -> "OrderedDict[str, str]":
    """중첩/점 표기 어느 쪽이든 'A.B.C' 평탄 키로. 배열은 'KEY[0]' 로."""
    if out is None:
        out = OrderedDict()
    for k, v in node.items():
        key = f"{prefix}{k}"
        if isinstance(v, dict):
            flatten(v, key + ".", out)
        elif isinstance(v, list):
            for i, item in enumerate(v):
                out[f"{key}[{i}]"] = item
        else:
            out[key] = v
    return out


def rebuild(en_node, ko_flat: dict, prefix: str = ""):
    """en.json 과 똑같은 모양/순서로, 번역이 있는 것만 채워 넣습니다."""
    out = OrderedDict()
    for k, v in en_node.items():
        key = f"{prefix}{k}"
        if isinstance(v, dict):
            sub = rebuild(v, ko_flat, key + ".")
            if sub:
                out[k] = sub
        elif isinstance(v, list):
            items = [ko_flat.get(f"{key}[{i}]") for i in range(len(v))]
            if all(x is not None for x in items):
                out[k] = items
        elif key in ko_flat:
            out[k] = ko_flat[key]
    return out


def load_list(path: Path) -> list:
    return list(load_json(path)) if path.exists() else []


# ─────────────────────────── 키 이동 추정 (스냅샷이 없을 때) ───────────────────────────

_NOISE = {"fields", "label", "hint", "actions", "notifications", "types"}


def _norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", s.lower())


def _sigs(key: str):
    parts = key.replace("[", ".").replace("]", "").split(".")
    root = parts[0]
    full = _norm("".join(parts))
    core = [p for p in parts[1:] if _norm(p) not in _NOISE]
    leaf = _norm(core[-1]) if core else ""
    tail = parts[-1].lower()
    suffix = tail if tail in ("label", "hint", "placeholder") else ""
    return full, (root, leaf, suffix)


def guess_moves(missing: list, orphans: list):
    """1) 키 전체를 구분자/대소문자 무시하고 비교 (LIGHT.AnimationFlame ↔ LIGHT.ANIMATION.Flame)
       2) 같은 최상위 네임스페이스 안에서 마지막 이름이 같고 양쪽 모두 유일할 때 (HOTBAR.CLEAR ↔ HOTBAR.ACTIONS.Clear)"""
    moves = {}
    by_full = defaultdict(list)
    for o in orphans:
        by_full[_sigs(o)[0]].append(o)
    rest = []
    for m in missing:
        c = by_full.get(_sigs(m)[0], [])
        if len(c) == 1:
            moves[m] = (c[0], "경로 일치")
        else:
            rest.append(m)
    used = {v[0] for v in moves.values()}
    o_idx, m_idx = defaultdict(list), defaultdict(list)
    for o in orphans:
        if o not in used:
            o_idx[_sigs(o)[1]].append(o)
    for m in rest:
        m_idx[_sigs(m)[1]].append(m)
    for sig, ms in m_idx.items():
        if sig[1] and len(ms) == 1 and len(o_idx.get(sig, [])) == 1:
            moves[ms[0]] = (o_idx[sig][0], "이름 일치(추정)")
    return moves


# ─────────────────────────── 명령: status ───────────────────────────

def cmd_status(args):
    en = flatten(load_json(EN))
    ko = flatten(load_json(KO, lenient=True))
    stale = set(load_list(STALE))
    missing = [k for k in en if k not in ko]
    orphans = [k for k in ko if k not in en]
    done = len(en) - len(missing)
    print(f"en 키 {len(en)}개 / 번역됨 {done}개 ({done / len(en) * 100:.1f}%)")
    print(f"  미번역 {len(missing)} · 재검토(stale) {len(stale)} · en 에 없는 키 {len(orphans)}")
    print(f"  스냅샷(l10n/en.synced.json): {'있음' if BASE.exists() else '없음 → 키 이동은 추정 모드로 처리됩니다'}")
    if missing:
        print("\n미번역 상위 네임스페이스:")
        for ns, n in Counter(k.split(".")[0] for k in missing).most_common(15):
            print(f"  {ns:<24}{n}")


# ─────────────────────────── 명령: sync ───────────────────────────

def cmd_sync(args):
    en_tree = load_json(Path(args.en))
    en = flatten(en_tree)
    ko = flatten(load_json(KO, lenient=True))
    for extra in args.also or []:                     # 보조 번역 소스(예: 이전 커밋의 ko.json)
        for k, v in flatten(load_json(Path(extra), lenient=True)).items():
            ko.setdefault(k, v)

    old_en_path = Path(args.old_en) if args.old_en else (BASE if BASE.exists() else None)
    old_en = flatten(load_json(old_en_path)) if old_en_path else None
    stale = set(load_list(STALE))

    result = OrderedDict((k, ko[k]) for k in en if k in ko)
    orphans = [k for k in ko if k not in en]
    report = defaultdict(list)

    # 1) 영어 원문이 바뀐 키 → 번역은 유지하되 stale 로 표시
    if old_en is not None:
        for k in result:
            if k in old_en and old_en[k] != en[k]:
                stale.add(k)
                report["changed"].append(k)

    # 2) 키 이동: 스냅샷이 있으면 '영어 문장 동일'로 정확히, 없으면 이름으로 추정
    missing = [k for k in en if k not in result]
    if old_en is not None:
        text_to_orphan = defaultdict(list)
        for o in orphans:
            if o in old_en:
                text_to_orphan[old_en[o]].append(o)
        for m in missing:
            cands = text_to_orphan.get(en[m], [])
            if cands:
                result[m] = ko[cands[0]]
                report["moved"].append((m, cands[0], "영어 동일"))
    elif not args.no_fuzzy:
        for m, (o, how) in guess_moves(missing, orphans).items():
            result[m] = ko[o]
            report["moved"].append((m, o, how))

    # 3) 영어를 그대로 복사해 둔 값은 번역이 아니므로 제거 → 미번역으로 export 됨
    for k in list(result):
        if looks_untranslated(en[k], result[k]):
            del result[k]
            report["english"].append(k)

    # 4) 치환자/태그가 원문과 안 맞는 번역 → 영어가 바뀌었거나 오역. 번역은 유지하고 stale 로
    for k in result:
        if isinstance(en[k], str) and validate(en[k], result[k]) and k not in stale:
            stale.add(k)
            report["invalid"].append(k)

    # 5) 번역 메모리: 같은 영어 문장이 다른 키에서 이미 번역돼 있으면 재사용.
    #    번역이 한 가지로 일치할 때만, 그리고 1~2단어짜리 짧은 문장은 문맥을 타므로 2곳 이상에서 같을 때만.
    if not args.no_tm:
        tm = defaultdict(list)
        for k, v in result.items():
            if k not in stale and isinstance(en.get(k), str) and HANGUL.search(v):
                tm[en[k]].append(v)
        for m in [k for k in en if k not in result]:
            cands = tm.get(en[m], [])
            short = len(str(en[m]).split()) <= 2
            if cands and len(set(cands)) == 1 and (len(cands) >= 2 or not short):
                result[m] = cands[0]
                report["tm"].append(m)

    stale = {k for k in stale if k in en}
    ordered = OrderedDict((k, result[k]) for k in en if k in result)
    dump_json(KO, rebuild(en_tree, ordered))
    dump_json(BASE, en_tree)
    dump_json(STALE, sorted(stale))

    removed = [k for k in ko if k not in en and k not in {o for _, o, _ in report["moved"]}]
    missing = [k for k in en if k not in ordered]
    _write_report(en, ko, ordered, report, removed, missing)
    print(f"ko.json 을 en.json 구조로 재작성했습니다. ({len(ordered)}/{len(en)} 번역)")
    print(f"  키 이동 반영 {len(report['moved'])} · 번역메모리 재사용 {len(report['tm'])} · "
          f"영어 원문 변경 {len(report['changed'])} · 치환자/태그 불일치 {len(report['invalid'])} · "
          f"영어 그대로였던 값 {len(report['english'])}")
    print(f"  삭제된 키 {len(removed)} · 재검토(stale) {len(stale)} · 미번역 {len(missing)}")
    print(f"  자세한 내용: {REPORT.relative_to(ROOT)}")
    print("  다음 단계: python tools/l10n.py export")


def _write_report(en, ko, result, report, removed, missing):
    L = ["# sync 리포트", "", "`git diff lang/ko.json` 으로 실제 변경을 함께 확인하세요.", ""]
    if report["moved"]:
        L += ["## 키 이동으로 번역을 옮긴 항목 (특히 '추정'은 한 번 훑어보세요)", "",
              "| 새 키 | 영어 | 가져온 번역 | 옛 키 | 방식 |", "|---|---|---|---|---|"]
        for new, old, how in report["moved"]:
            L.append(f"| `{new}` | {_cell(en[new])} | {_cell(result[new])} | `{old}` | {how} |")
        L.append("")
    if report["tm"]:
        L += ["## 같은 영어 문장의 기존 번역을 재사용한 항목", "", "| 키 | 영어 | 번역 |", "|---|---|---|"]
        L += [f"| `{k}` | {_cell(en[k])} | {_cell(result[k])} |" for k in report["tm"]]
        L.append("")
    if report["invalid"]:
        L += ["## 치환자/태그가 영어 원문과 안 맞는 기존 번역 (stale 로 표시, export 에 포함됨)", "",
              "영어 원문이 바뀌었거나 DeepL 이 `{count}` → `{개수}` 처럼 치환자를 번역해 버린 경우입니다.", ""]
        L += [f"- `{k}`: {', '.join(validate(en[k], result[k]))}  \n  EN: {_cell(en[k])}  \n  KO: {_cell(result[k])}"
              for k in report["invalid"]]
        L.append("")
    if report["english"]:
        L += ["## 영어가 그대로 들어 있던 값 (제거 → 미번역으로 export 됨)", ""]
        L += [f"- `{k}`: {_cell(en[k])}" for k in report["english"]]
        L.append("")
    if report["changed"]:
        L += ["## 영어 원문이 바뀐 항목 (stale, export 에 포함됨)", ""]
        L += [f"- `{k}`: {_cell(en[k])}" for k in report["changed"]]
        L.append("")
    if removed:
        L += ["## en.json 에서 사라져 ko.json 에서도 삭제된 키", "", "<details><summary>펼치기</summary>", ""]
        L += [f"- `{k}`: {_cell(ko[k])}" for k in removed]
        L += ["", "</details>", ""]
    L += [f"## 미번역 {len(missing)}개 → `python tools/l10n.py export`", ""]
    REPORT.write_text("\n".join(L), encoding="utf-8", newline="\n")


def _cell(s) -> str:
    s = str(s).replace("|", "\\|").replace("\n", " ")
    return s if len(s) <= 80 else s[:77] + "…"


# ─────────────────────────── 명령: export / import ───────────────────────────

def mask(text: str):
    """{name} 같은 치환자와 속성 있는 태그를 {0},{1}… 로 바꿔 DeepL 이 건드리지 못하게."""
    tokens = []

    def sub(m):
        tokens.append(m.group(0))
        return "{%d}" % (len(tokens) - 1)

    # 한 번에 처리해야 <a href="{url}"> 처럼 태그 안에 든 치환자를 이중으로 바꾸지 않음
    masked = MASK_RE.sub(sub, text)
    masked = masked.replace("\n", "<br>")
    return masked, tokens


def unmask(text: str, tokens: list, en_text: str = "") -> str:
    if "\n" in en_text:
        text = re.sub(r"\s*<br\s*/?>\s*", "\n", text)
    return re.sub(r"\{(\d+)\}", lambda m: tokens[int(m.group(1))] if int(m.group(1)) < len(tokens) else m.group(0), text)


def todo_items(include_stale=True):
    en = flatten(load_json(EN))
    ko = flatten(load_json(KO, lenient=True))
    stale = set(load_list(STALE)) if include_stale else set()
    return en, ko, [k for k in en if k not in ko or k in stale]


def cmd_export(args):
    en, ko, keys = todo_items(not args.no_stale)
    if not keys:
        print("번역할 항목이 없습니다.")
        return
    DEEPL_DIR.mkdir(parents=True, exist_ok=True)
    for f in DEEPL_DIR.glob("*_en.txt"):
        f.unlink()

    manifest = OrderedDict()
    chunks, cur, size = [], [], 0
    for i, k in enumerate(keys, 1):
        masked, tokens = mask(en[k])
        manifest[str(i)] = {"key": k, "en": en[k], "tokens": tokens, "old_ko": ko.get(k)}
        line = f"[{i}] {masked}"
        if cur and size + len(line) + 1 > args.chunk:
            chunks.append(cur)
            cur, size = [], 0
        cur.append(line)
        size += len(line) + 1
    if cur:
        chunks.append(cur)

    for n, lines in enumerate(chunks, 1):
        (DEEPL_DIR / f"{n:02d}_en.txt").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    dump_json(DEEPL_DIR / "manifest.json", manifest)
    print(f"{len(keys)}개 문자열 → {len(chunks)}개 파일 (파일당 최대 {args.chunk}자)  {DEEPL_DIR.relative_to(ROOT)}/")
    print("  1) 각 NN_en.txt 내용을 DeepL(영어→한국어)에 붙여넣기")
    print("  2) 번역 결과를 같은 폴더에 NN_ko.txt 로 저장 (예: 01_en.txt → 01_ko.txt)")
    print("  3) python tools/l10n.py import")


def _parse_translated(files):
    got = {}
    for f in files:
        cur = None
        for raw in Path(f).read_text(encoding="utf-8-sig").splitlines():
            if raw.lstrip().startswith("#"):
                continue
            m = LINE_RE.match(raw)
            if m:
                cur = m.group(1)
                got[cur] = m.group(2).strip()
            elif cur and raw.strip():          # DeepL 이 줄을 나눠버린 경우 이어붙임
                got[cur] += " " + raw.strip()
    return got


def apply_translations(got: dict, opts):
    manifest = load_json(DEEPL_DIR / "manifest.json")
    en_tree = load_json(EN)
    ko = flatten(load_json(KO, lenient=True))
    stale = set(load_list(STALE))
    ok, problems = 0, []
    for id_, item in manifest.items():
        if id_ not in got:
            continue
        text = unmask(got[id_], item["tokens"], item["en"])
        issues = validate(item["en"], text)
        if issues and not getattr(opts, "force", False):
            problems.append((id_, item["key"], item["en"], text, issues))
            continue
        ko[item["key"]] = text
        stale.discard(item["key"])
        ok += 1
    nums = [int(i) for i in got if i.isdigit()]
    missing_ids = [str(i) for i in range(min(nums), max(nums) + 1) if str(i) not in got] if nums else []
    dump_json(KO, rebuild(en_tree, ko))
    dump_json(STALE, sorted(k for k in stale))
    print(f"반영 {ok}개 · 문제 있어 보류 {len(problems)}개 · 번역 결과에서 빠진 줄 {len(missing_ids)}개")
    if problems:
        out = DEEPL_DIR / "problems.txt"
        lines = ["# 아래 항목은 치환자/태그가 원문과 달라 반영하지 않았습니다.",
                 "# 고친 뒤 이 파일 그대로 import 하면 됩니다:  python tools/l10n.py import l10n/deepl/problems.txt", ""]
        for id_, key, en, text, issues in problems:
            masked_en, tokens = mask(en)
            masked_ko = mask(text)[0] if not tokens else _remask(text, tokens)
            lines += [f"# {key}  ({', '.join(issues)})", f"# EN: {masked_en}", f"[{id_}] {masked_ko}", ""]
        out.write_text("\n".join(lines), encoding="utf-8", newline="\n")
        print(f"  → {out.relative_to(ROOT)} 확인")
    if missing_ids[:10]:
        print("  빠진 번호 예:", ", ".join(missing_ids[:10]))


def _remask(text, tokens):
    for i, t in enumerate(tokens):
        text = text.replace(t, "{%d}" % i)
    return text.replace("\n", "<br>")


def cmd_import(args):
    files = args.files or sorted(str(p) for p in DEEPL_DIR.glob("*_ko.txt"))
    if not files:
        sys.exit("가져올 *_ko.txt 파일이 없습니다.")
    print("가져오는 파일:", ", ".join(Path(f).name for f in files))
    apply_translations(_parse_translated(files), args)


# ─────────────────────────── 명령: deepl (API, 선택) ───────────────────────────

def cmd_deepl(args):
    key = args.key or os.environ.get("DEEPL_API_KEY")
    if not key:
        sys.exit("DeepL API 키가 필요합니다: 환경변수 DEEPL_API_KEY 또는 --key")
    if not (DEEPL_DIR / "manifest.json").exists() or args.refresh:
        cmd_export(argparse.Namespace(chunk=4500, no_stale=False))
    manifest = load_json(DEEPL_DIR / "manifest.json")
    host = "api-free.deepl.com" if key.endswith(":fx") else "api.deepl.com"
    ids = list(manifest)
    got = {}
    for s in range(0, len(ids), 50):
        batch = ids[s:s + 50]
        texts = [_to_html(manifest[i]["en"]) for i in batch]
        body = json.dumps({
            "text": texts, "source_lang": "EN", "target_lang": "KO",
            "tag_handling": "html",
            "context": "User interface strings of Foundry Virtual Tabletop, a virtual tabletop app for role-playing games.",
            **({"glossary_id": args.glossary_id} if args.glossary_id else {}),
        }).encode()
        req = urllib.request.Request(f"https://{host}/v2/translate", data=body, method="POST",
                                     headers={"Authorization": f"DeepL-Auth-Key {key}",
                                              "Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=60) as r:
            res = json.load(r)
        for i, t in zip(batch, res["translations"]):
            got[i] = _from_html(t["text"], manifest[i]["en"])
        print(f"  {min(s + 50, len(ids))}/{len(ids)}")
    lines = [f"[{i}] {mask(t)[0] if not manifest[i]['tokens'] else _remask(t, manifest[i]['tokens'])}" for i, t in got.items()]
    (DEEPL_DIR / "api_ko.txt").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    if args.dry_run:
        print("결과를 l10n/deepl/api_ko.txt 에 저장했습니다. 확인 후: python tools/l10n.py import")
        return
    apply_translations(_parse_translated([DEEPL_DIR / "api_ko.txt"]), args)


def _to_html(text):
    # 치환자는 번역 금지 span 으로 감쌈. 줄바꿈은 <br>.
    text = ANY_TAG_OR_PH.sub(lambda m: m.group(1) or f'<span translate="no">{m.group(2)}</span>', text)
    return text.replace("\n", "<br>")


def _from_html(text, en):
    text = re.sub(r'<span translate="no">(.*?)</span>', r"\1", text)
    text = re.sub(r"\s*<br\s*/?>\s*", "\n", text)
    for ent in set(re.findall(r"&\w+;|&#\d+;", text)):
        if ent not in en:
            text = text.replace(ent, html.unescape(ent))
    return text


# ─────────────────────────── 명령: check ───────────────────────────

def validate(en_text: str, ko_text: str) -> list:
    issues = []
    if not isinstance(ko_text, str) or not ko_text.strip():
        return ["빈 번역"]
    if Counter(PH_RE.findall(en_text)) != Counter(PH_RE.findall(ko_text)):
        a, b = set(PH_RE.findall(en_text)), set(PH_RE.findall(ko_text))
        if a - b:
            issues.append("치환자 누락 " + " ".join(sorted(a - b)))
        if b - a:
            issues.append("원문에 없는 치환자 " + " ".join(sorted(b - a)))
    if ko_text.count("{") != ko_text.count("}"):
        issues.append("중괄호 짝 안 맞음")
    tag_name = lambda t: re.match(r"</?([a-zA-Z][\w-]*)", t).group(0).lower()
    if Counter(map(tag_name, TAG_RE.findall(en_text))) != Counter(map(tag_name, TAG_RE.findall(ko_text))):
        issues.append("HTML 태그 불일치")
    if re.search(r"\{\d+\}", ko_text):
        issues.append("복원되지 않은 {숫자}")
    return issues


def _keep_english():
    g = load_json(GLOSSARY) if GLOSSARY.exists() else {}
    return set(g.get("_keep_english", []))


def looks_untranslated(en_text, ko_text) -> bool:
    return (isinstance(en_text, str) and en_text not in _KEEP and ko_text == en_text and not HANGUL.search(ko_text)
            and len(re.findall(r"[A-Za-z]{2,}", PH_RE.sub("", en_text))) >= 2)


def cmd_check(args):
    en = flatten(load_json(EN))
    ko = flatten(load_json(KO))       # 여기서는 자동 수리하지 않고 문법 오류를 그대로 실패 처리
    errors, warns = [], []
    for k, v in ko.items():
        if k not in en:
            warns.append(f"en 에 없는 키: {k}")
            continue
        if looks_untranslated(en[k], v):
            warns.append(f"영어 그대로: {k} = {v}")
        for issue in validate(en[k], v):
            errors.append(f"{k}: {issue}\n      EN: {en[k]}\n      KO: {v}")
    gloss = load_json(GLOSSARY) if GLOSSARY.exists() else {}
    terms = {t: v for t, v in gloss.items() if not t.startswith("_")}
    for k, v in ko.items():
        e = en.get(k)
        if not isinstance(e, str):
            continue
        for term, want in terms.items():
            wants = want if isinstance(want, list) else [want]
            if re.search(rf"\b{re.escape(term)}s?\b", e) and not any(w in v for w in wants):
                warns.append(f"용어집: {k} — '{term}' → '{'/'.join(wants)}' 기대, 번역: {v}")
    missing = sum(1 for k in en if k not in ko)
    for w in warns[: args.max_warn]:
        print("  [경고]", w)
    if len(warns) > args.max_warn:
        print(f"  … 경고 {len(warns) - args.max_warn}개 더 (--max-warn 로 조절)")
    for e in errors:
        print("  [오류]", e)
    print(f"\n검사 결과: 오류 {len(errors)} · 경고 {len(warns)} · 미번역 {missing}")
    if errors and not args.no_fail:
        sys.exit(1)


# ─────────────────────────── main ───────────────────────────

def main():
    try:  # Windows 콘솔(cp949)에서 특수문자 때문에 죽지 않도록
        sys.stdout.reconfigure(errors="replace")
    except Exception:
        pass
    p = argparse.ArgumentParser(description="FvTT 한글화 유지보수 도구")
    sp = p.add_subparsers(dest="cmd", required=True)

    sp.add_parser("status").set_defaults(fn=cmd_status)

    s = sp.add_parser("sync", help="ko.json 을 en.json 구조에 맞춰 재구성")
    s.add_argument("--en", default=str(EN))
    s.add_argument("--old-en", help="이전 버전 en.json (기본: l10n/en.synced.json)")
    s.add_argument("--also", nargs="*", help="추가 번역 소스 json (ko.json 에 없는 키만 가져옴)")
    s.add_argument("--no-fuzzy", action="store_true", help="키 이름 기반 추정 이동을 하지 않음")
    s.add_argument("--no-tm", action="store_true", help="같은 영어 문장 번역 재사용을 하지 않음")
    s.set_defaults(fn=cmd_sync)

    s = sp.add_parser("export", help="DeepL 용 txt 추출")
    s.add_argument("--chunk", type=int, default=4500, help="파일당 최대 글자 수 (DeepL 무료 웹은 1500)")
    s.add_argument("--no-stale", action="store_true", help="재검토(stale) 항목은 제외")
    s.set_defaults(fn=cmd_export)

    s = sp.add_parser("import", help="DeepL 결과 반영")
    s.add_argument("files", nargs="*")
    s.add_argument("--force", action="store_true", help="검증 실패 항목도 반영")
    s.set_defaults(fn=cmd_import)

    s = sp.add_parser("deepl", help="DeepL API 로 자동 번역 (선택)")
    s.add_argument("--key")
    s.add_argument("--glossary-id")
    s.add_argument("--refresh", action="store_true", help="export 를 새로 한 뒤 번역")
    s.add_argument("--dry-run", action="store_true", help="ko.json 에 반영하지 않고 api_ko.txt 만 생성")
    s.add_argument("--force", action="store_true")
    s.set_defaults(fn=cmd_deepl)

    s = sp.add_parser("check", help="오류 검사")
    s.add_argument("--no-fail", action="store_true")
    s.add_argument("--max-warn", type=int, default=30)
    s.set_defaults(fn=cmd_check)

    args = p.parse_args()
    _KEEP.update(_keep_english())
    args.fn(args)


if __name__ == "__main__":
    main()
