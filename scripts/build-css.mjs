#!/usr/bin/env node
/**
 * Cross-platform CSS build for LombokCSS.
 * Replaces the POSIX `cat` concat, which silently produces an EMPTY
 * dist/lombok.css when npm scripts run under cmd.exe on Windows
 * (redirection creates the file, then `cat` fails).
 *
 * Steps:
 *   1. Concatenate source layers (byte-identical to `cat`, LF endings).
 *   2. Minify via lightningcss --bundle -> dist/lombok.min.css
 */
import { readFileSync, writeFileSync, mkdirSync } from "node:fs";
import { execFileSync } from "node:child_process";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

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

const bundle = LAYERS.map((f) =>
  readFileSync(join(root, "src", f), "utf8").replace(/\r\n/g, "\n"),
).join("");

const outCss = join(root, "dist", "lombok.css");
writeFileSync(outCss, bundle, "utf8");

if (bundle.length === 0) {
  console.error("build-css: bundle is empty — aborting");
  process.exit(1);
}

execFileSync(
  "npx",
  ["lightningcss", "--minify", "--bundle", outCss, "-o", join(root, "dist", "lombok.min.css")],
  { stdio: "inherit", shell: process.platform === "win32" },
);

console.log(`build-css: dist/lombok.css ${bundle.length} B OK`);
