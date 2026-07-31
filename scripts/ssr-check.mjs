// Guards the SSR fix. package.json sets "type": "module" and points
// main/exports["."] at dist/lombok.js, so Next/Nuxt/Astro/SvelteKit evaluate
// this file on the server. It must import without touching the DOM.
//
// Self-reference ("lombokcss") is deliberate: it exercises the exports map,
// not just the file path.
const entries = ["lombokcss", "lombokcss/js"];

for (const entry of entries) {
  try {
    await import(entry);
  } catch (err) {
    console.error(`✗ import("${entry}") threw on the server: ${err.message}`);
    process.exit(1);
  }
  console.log(`✓ import("${entry}") is safe without a DOM`);
}

if (typeof globalThis.Lombok !== "undefined") {
  console.error("✗ the DOM guard did not bail out early — window.Lombok was assigned");
  process.exit(1);
}
console.log("✓ the DOM guard bails out before any browser API is touched");
