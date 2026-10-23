/**
 * Lite / Plus editions from one source tree.
 *
 *   node tools/edition.mjs lite  [--in-place | --out dist]   → the free edition
 *   node tools/edition.mjs plus  [--in-place | --out dist]   → the supporter edition (= the source as it is)
 *   node tools/edition.mjs check                             → lists what Lite leaves out, and checks the markers
 *
 * edition.json (module root):
 *   {
 *     "public": "plus" | "lite",      // which edition the public GitHub release carries (open beta: "plus")
 *     "plusFiles": ["scripts/travel.mjs", "scripts/plus/"],   // left out of Lite (replaced by empty stubs)
 *     "lite":  { "description": "…" }, // module.json overrides for Lite
 *     "plus":  { "description": "…" }  // module.json overrides for Plus
 *   }
 *
 * In Lite:
 *   - scripts/edition.mjs becomes `export const PLUS = false;`
 *   - every plusFiles entry is replaced by a stub with the same exports (functions do nothing,
 *     classes are empty, constants are null/{}), so static imports keep working;
 *   - lines between `// @plus` and `// @end-plus` (in .mjs/.js/.css/.hbs/.html) are removed;
 *   - module.json gets flags.<id>.edition = "lite" and the "lite" overrides.
 * The code still checks PLUS before showing Plus-only buttons, tabs and settings.
 *
 * No edition.json = a free module: one edition ("plus" = the folder as it is), packed the way the
 * old GitHub workflow packed it (everything but git, dist, private notes and these tools).
 *
 * --out dist writes dist/<edition>/ and dist/<id>-<edition>.zip (+ dist/<edition>-module.json).
 * --in-place rewrites the working tree (used by the GitHub release workflow on a fresh checkout).
 */
import fs from "node:fs";
import path from "node:path";
import { spawnSync } from "node:child_process";

const ROOT = process.cwd();
const [edition, ...args] = process.argv.slice(2);
const FREE = !fs.existsSync(path.join(ROOT, "edition.json"));
const conf = FREE ? { public: "plus", plusFiles: [] } : JSON.parse(fs.readFileSync(path.join(ROOT, "edition.json"), "utf8"));
const manifest = JSON.parse(fs.readFileSync(path.join(ROOT, "module.json"), "utf8"));
// media/ holds screenshots and GIFs for README and the Foundry package page, not the module.
const SKIP = new Set([".git", ".github", ".private", "dist", "node_modules", "tools", "media", "edition.json", ".gitignore", ".DS_Store"]);
// Free modules keep their tools/ folder (helpers that ship with them); only these are left out.
const FREE_SKIP = new Set([".git", ".github", ".private", "dist", "node_modules", "media", ".gitignore", ".DS_Store", "Thumbs.db", ".vscode"]);
const FREE_SKIP_FILES = new Set(["tools/edition.mjs", "tools/release.mjs", "tools/local.config.json", "tools/last-release.json"]);
const freeLeftOut = rel => FREE_SKIP_FILES.has(rel) || /(^|\/)(node_modules|\.DS_Store|LOG|LOG\.old)(\/|$)/.test(rel) || /(^|\/)package-lock\.json$|\.env$/.test(rel);
const TEXT = /\.(mjs|js|css|hbs|html)$/;

const norm = p => p.replace(/\\/g, "/");
const isPlusFile = rel => (conf.plusFiles ?? []).some(p => (p.endsWith("/") ? norm(rel).startsWith(p) : norm(rel) === p));

/** Same exports, no behaviour. */
function stubFor(source, rel) {
  const lines = [`// ${rel}: Plus edition only (this is the Lite edition).`];
  const names = new Set();
  const add = (name, kind) => {
    if (names.has(name)) return;
    names.add(name);
    if (kind === "class") lines.push(`export class ${name} {}`);
    else if (kind === "fn") lines.push(`export function ${name}() { return null; }`);
    else lines.push(`export const ${name} = Object.freeze({});`);
  };
  for (const m of source.matchAll(/^export\s+(?:async\s+)?function\s*\*?\s*([A-Za-z_$][\w$]*)/gm)) add(m[1], "fn");
  for (const m of source.matchAll(/^export\s+class\s+([A-Za-z_$][\w$]*)/gm)) add(m[1], "class");
  for (const m of source.matchAll(/^export\s+(?:const|let|var)\s+([A-Za-z_$][\w$]*)/gm)) add(m[1], "const");
  for (const m of source.matchAll(/^export\s*\{([^}]+)\}/gm)) {
    for (const part of m[1].split(",")) {
      const name = part.trim().split(/\s+as\s+/).pop()?.trim();
      if (name && name !== "default") add(name, "fn");
    }
  }
  if (/^export\s+default\b/m.test(source)) lines.push("export default null;");
  return `${lines.join("\n")}\n`;
}

function stripBlocks(text, rel) {
  const out = [];
  let depth = 0;
  for (const line of text.split("\n")) {
    if (/(?:\/\/|\/\*|<!--|\{\{!--)\s*@plus\b(?!-)/.test(line) && !/@end-plus/.test(line)) { depth++; continue; }
    if (/@end-plus\b/.test(line)) { if (depth === 0) throw new Error(`${rel}: @end-plus without @plus`); depth--; continue; }
    if (depth === 0) out.push(line);
  }
  if (depth) throw new Error(`${rel}: @plus without @end-plus`);
  return out.join("\n");
}

function transform(rel, buf, ed) {
  if (ed === "plus") return buf;
  if (norm(rel) === "scripts/edition.mjs") return Buffer.from("export const PLUS = false;\n");
  if (isPlusFile(rel)) return TEXT.test(rel) && /\.(mjs|js)$/.test(rel) ? Buffer.from(stubFor(buf.toString("utf8"), rel)) : null;
  if (TEXT.test(rel)) return Buffer.from(stripBlocks(buf.toString("utf8"), rel));
  return buf;
}

function moduleJsonFor(ed) {
  const m = structuredClone(manifest);
  if (FREE) return m;
  Object.assign(m, conf[ed] ?? {});
  m.flags ??= {};
  m.flags[m.id] = { ...(m.flags[m.id] ?? {}), edition: ed };
  return m;
}

function walk(dir, rel = "") {
  const out = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (!rel && (FREE ? FREE_SKIP : SKIP).has(entry.name)) continue;
    const r = rel ? `${rel}/${entry.name}` : entry.name;
    if (FREE && freeLeftOut(r)) continue;
    if (entry.isDirectory()) out.push(...walk(path.join(dir, entry.name), r));
    else if (r !== "module.json") out.push(r);
  }
  return out;
}

function build(ed, target) {
  for (const rel of walk(ROOT)) {
    const data = transform(rel, fs.readFileSync(path.join(ROOT, rel)), ed);
    const dest = path.join(target, rel);
    if (data === null) { if (target === ROOT) fs.rmSync(dest, { force: true }); continue; }
    fs.mkdirSync(path.dirname(dest), { recursive: true });
    fs.writeFileSync(dest, data);
  }
  fs.writeFileSync(path.join(target, "module.json"), `${JSON.stringify(moduleJsonFor(ed), null, 2)}\n`);
}

function zipDir(dir, zipPath) {
  fs.rmSync(zipPath, { force: true });
  // Files at the root of the zip (what Foundry expects), named one by one: Windows' tar doesn't expand "*".
  const entries = fs.readdirSync(dir);
  const ps = p => `'${p.replace(/'/g, "''")}'`;
  const tries = process.platform === "win32"
    ? [["tar", ["-a", "-c", "-f", zipPath, ...entries]],
       ["powershell", ["-NoProfile", "-Command", `Compress-Archive -Path ${entries.map(ps).join(",")} -DestinationPath ${ps(zipPath)}`]]]
    : [["zip", ["-r", "-q", zipPath, ...entries]]];
  for (const [cmd, a] of tries) {
    const r = spawnSync(cmd, a, { cwd: dir, stdio: "inherit" });
    if (r.status === 0 && fs.existsSync(zipPath)) return;
  }
  throw new Error("could not make the zip");
}

if (edition === "check") {
  const left = walk(ROOT).filter(isPlusFile);
  console.log(`Lite leaves out ${left.length} file(s):\n  ${left.join("\n  ")}`);
  let blocks = 0;
  for (const rel of walk(ROOT).filter(r => TEXT.test(r))) {
    const text = fs.readFileSync(path.join(ROOT, rel), "utf8");
    stripBlocks(text, rel);
    blocks += (text.match(/@plus\b(?!-)/g) ?? []).length;
  }
  console.log(`${blocks} @plus block(s), all closed. Public release: ${conf.public ?? "lite"}.`);
} else if (edition === "lite" || edition === "plus" || edition === "public") {
  const ed = edition === "public" ? (conf.public ?? "lite") : edition;
  if (args.includes("--in-place")) {
    build(ed, ROOT);
    for (const rel of walk(ROOT).filter(isPlusFile)) if (ed === "lite" && !/\.(mjs|js)$/.test(rel)) fs.rmSync(path.join(ROOT, rel), { force: true });
    console.log(`${manifest.id}: working tree is now the ${ed} edition.`);
  } else {
    const out = path.resolve(ROOT, args[args.indexOf("--out") + 1] && args.includes("--out") ? args[args.indexOf("--out") + 1] : "dist");
    fs.mkdirSync(out, { recursive: true });
    // git leaves the build folder alone without touching the module's .gitignore
    if (!fs.existsSync(path.join(out, ".gitignore"))) fs.writeFileSync(path.join(out, ".gitignore"), "*\n");
    const target = path.join(out, ed, manifest.id);
    fs.rmSync(target, { recursive: true, force: true });
    fs.mkdirSync(target, { recursive: true });
    build(ed, target);
    const zip = path.join(out, `${manifest.id}-${ed}.zip`);
    zipDir(target, zip);
    fs.copyFileSync(path.join(target, "module.json"), path.join(out, `${ed}-module.json`));
    console.log(`${zip}\n${path.join(out, `${ed}-module.json`)}`);
  }
} else {
  console.log("usage: node tools/edition.mjs lite|plus|public [--out dist | --in-place]  ·  node tools/edition.mjs check");
  process.exit(1);
}
