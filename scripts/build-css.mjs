#!/usr/bin/env node
/**
 * Cross-platform CSS build for LombokCSS.
 *
 * Replaces the POSIX `cat` concat, which silently produces an EMPTY
 * dist/lombok.css when npm scripts run under cmd.exe on Windows
 * (redirection creates the file, then `cat` fails).
 *
 * Minification uses the `lightningcss` Node API rather than the
 * `lightningcss-cli` binary on purpose: the CLI package ships only a
 * placeholder file and relies on a `postinstall` hook to move the real
 * binary into place. Newer npm blocks lifecycle scripts by default, which
 * left the CLI as an unusable 78-byte stub and broke `npm run build`.
 * The Node API resolves a prebuilt native module through optional
 * dependencies and needs no install script, so the build works the same
 * whether or not scripts are allowed. Output is byte-identical to the CLI.
 *
 * Steps:
 *   1. Concatenate source layers (byte-identical to `cat`, LF endings).
 *   2. Minify + bundle -> dist/lombok.min.css
 */
import { readFileSync, writeFileSync, mkdirSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import { bundle } from "lightningcss";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");

const LAYERS = [
  "variables.css",
  "core.css",
  "themes.css",
  "components.css",
  "utilities.css",
  "print.css",
];

mkdirSync(join(root, "dist"), { recursive: true });

const source = LAYERS.map((f) =>
  readFileSync(join(root, "src", f), "utf8").replace(/\r\n/g, "\n"),
).join("");

if (source.length === 0) {
  console.error("build-css: bundle is empty — aborting");
  process.exit(1);
}

const outCss = join(root, "dist", "lombok.css");
writeFileSync(outCss, source, "utf8");

const outMin = join(root, "dist", "lombok.min.css");
const { code } = bundle({ filename: outCss, minify: true });

if (code.length === 0) {
  console.error("build-css: minified bundle is empty — aborting");
  process.exit(1);
}

writeFileSync(outMin, code);

console.log(
  `build-css: dist/lombok.css ${source.length} B, dist/lombok.min.css ${code.length} B OK`,
);
