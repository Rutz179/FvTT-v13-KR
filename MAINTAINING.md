# 유지보수 가이드

Python 3.9 이상만 있으면 됩니다 (추가 설치 없음). VS Code 에서는 `Ctrl+Shift+P → Tasks: Run Task → l10n: …` 로도 실행할 수 있습니다.

## 폴더 구조

| 경로 | 설명 |
|---|---|
| `lang/en.json` | Foundry 원본 영어 파일 (릴리스 zip 에는 안 들어감) |
| `lang/ko.json` | 번역 파일. **항상 도구가 en.json 과 같은 구조·순서로 다시 씀** |
| `l10n/en.synced.json` | ko.json 이 마지막으로 맞춰진 en.json 스냅샷. 다음 업데이트 때 비교 기준 |
| `l10n/stale.json` | 영어 원문이 바뀌어 재번역이 필요한 키 목록 |
| `l10n/glossary.json` | 용어집 (Token→토큰 등). `check` 가 어긋난 번역을 경고 |
| `l10n/sync-report.md` | 마지막 sync 결과 (이동된 키, 삭제된 키 등) |
| `l10n/deepl/` | DeepL 작업용 임시 폴더 (git 에 안 올라감) |

## Foundry 업데이트가 나왔을 때 (v14.x 패치, v15 …)

```bash
# 1. 새 버전 Foundry 설치 폴더의 en.json 을 lang/en.json 에 덮어쓰기
#    Windows: C:\Program Files\Foundry Virtual Tabletop\resources\app\public\lang\en.json

# 2. 구조 맞추기 — 키 이동/형식 변경은 자동 반영, 바뀐 문장은 stale 로 표시
python tools/l10n.py sync

# 3. 번역할 것만 뽑기
python tools/l10n.py export
#    → l10n/deepl/01_en.txt, 02_en.txt … 를 DeepL 에 붙여넣고
#      결과를 01_ko.txt, 02_ko.txt … 로 저장

# 4. 반영 + 검사
python tools/l10n.py import
python tools/l10n.py check

# 5. 변경 내용 눈으로 확인 후 커밋
git diff lang/ko.json
git add -A && git commit -m "v15 대응"
```

### DeepL 붙여넣기 규칙
- `[123]` 번호는 절대 지우지 마세요. 줄 순서가 바뀌거나 줄이 쪼개져도 번호로 찾아서 넣습니다.
- `{0}`, `{1}` 은 `{name}` 같은 치환자나 링크 태그를 숨겨 둔 것입니다. 번역문 안에서 위치만 맞게 두면 됩니다.
  (기존 번역에 `{count}` → `{개수}` 처럼 DeepL 이 치환자를 번역해 버린 사례가 있어서 이렇게 가립니다.)
- 파일당 4500자로 나눕니다. DeepL 무료 웹 입력창 한도가 더 작다면 `export --chunk 1500`.
- 치환자가 빠진 번역은 반영하지 않고 `l10n/deepl/problems.txt` 에 모읍니다. 고쳐서 `import l10n/deepl/problems.txt`.

### DeepL API 를 쓰면 (선택, API Free 는 월 50만 자 무료)
```bash
export DEEPL_API_KEY=xxxxxxxx:fx      # Windows PowerShell: $env:DEEPL_API_KEY="xxxxxxxx:fx"
python tools/l10n.py deepl --dry-run  # l10n/deepl/api_ko.txt 로만 저장 → 확인 후 import
python tools/l10n.py deepl            # 바로 반영
```

## 릴리스

```bash
git tag v2.0.0     # v14 대응은 메이저 버전을 올려 구분하는 것을 추천
git push origin main --tags
```
GitHub Actions 가 알아서
1. `check` 로 오류 검사 (오류가 있으면 릴리스 중단),
2. `module.json` 의 version / manifest / download 를 태그에 맞게 채우고,
3. `module.zip` 을 만들어 Release 에 `module.json` 과 함께 올립니다.

`module.json` 의 `version` 은 손으로 고칠 필요 없습니다. 태그가 곧 버전입니다.

## 브랜치
- `main` : 최신 코어(v14) 번역
- `v13`  : v13 용 마지막 상태 보존. v13 쪽 오타 수정이 필요하면 이 브랜치에서 작업 후 `v1.3.5` 같은 태그로 릴리스
  (워크플로가 main 이 아닌 브랜치의 태그는 **Latest** 로 지정하지 않으므로 v14 사용자 업데이트에 영향 없음)
