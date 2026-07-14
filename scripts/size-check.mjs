// Fails the build if the gzipped bundle exceeds the budget.
import { gzipSync } from "node:zlib";
import { readFileSync } from "node:fs";

const BUDGETS = { "dist/lombok.min.css": 15 * 1024, "dist/lombok.js": 4 * 1024 };
let failed = false;

for (const [file, budget] of Object.entries(BUDGETS)) {
  const gz = gzipSync(readFileSync(file)).length;
  const ok = gz <= budget;
  failed ||= !ok;
  console.log(
    `${ok ? "✓" : "✗"} ${file}: ${(gz / 1024).toFixed(2)} KB gzip (budget ${(budget / 1024).toFixed(0)} KB)`,
  );
}
if (failed) {
  console.error("\nSize budget exceeded.");
  process.exit(1);
}
console.log("\nAll bundles within budget.");
