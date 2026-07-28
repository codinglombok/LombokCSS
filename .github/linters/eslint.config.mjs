// Konfigurasi ESLint untuk Super-Linter (VALIDATE_JAVASCRIPT_ES).
//
// Sengaja TANPA import paket luar (@eslint/js dsb) supaya resolusi modul
// tidak bergantung pada layout node_modules di dalam container Super-Linter.
// Aturan ditulis eksplisit — sejalan dengan filosofi explicit-over-magic.
//
// Repo memakai "type": "module", jadi seluruh .js dan .mjs adalah ESM.
// Pengecualiannya src/lombok.js: itu dikirim ke browser sebagai classic
// script (bukan modul), sehingga diparse sebagai "script" dengan global
// browser. Menyamaratakan keduanya membuat ESLint gagal parse `import`.

const coreRules = {
  "no-undef": "error",
  "no-unused-vars": ["error", { args: "none", ignoreRestSiblings: true }],
  "no-redeclare": "error",
  "no-dupe-keys": "error",
  "no-dupe-args": "error",
  "no-duplicate-case": "error",
  "no-unreachable": "error",
  "no-fallthrough": "error",
  "no-cond-assign": "error",
  "no-constant-condition": "error",
  "no-empty": ["error", { allowEmptyCatch: true }],
  "no-self-assign": "error",
  "no-sparse-arrays": "error",
  "use-isnan": "error",
  "valid-typeof": "error",
  eqeqeq: ["error", "smart"],
};

const browserGlobals = {
  window: "readonly",
  document: "readonly",
  console: "readonly",
  navigator: "readonly",
  location: "readonly",
  history: "readonly",
  localStorage: "readonly",
  sessionStorage: "readonly",
  matchMedia: "readonly",
  getComputedStyle: "readonly",
  requestAnimationFrame: "readonly",
  cancelAnimationFrame: "readonly",
  setTimeout: "readonly",
  clearTimeout: "readonly",
  setInterval: "readonly",
  clearInterval: "readonly",
  queueMicrotask: "readonly",
  MutationObserver: "readonly",
  IntersectionObserver: "readonly",
  ResizeObserver: "readonly",
  CustomEvent: "readonly",
  Event: "readonly",
  Element: "readonly",
  HTMLElement: "readonly",
  Node: "readonly",
  NodeList: "readonly",
  DOMParser: "readonly",
  CSS: "readonly",
};

const nodeGlobals = {
  process: "readonly",
  console: "readonly",
  Buffer: "readonly",
  URL: "readonly",
  URLSearchParams: "readonly",
  TextEncoder: "readonly",
  TextDecoder: "readonly",
  setTimeout: "readonly",
  clearTimeout: "readonly",
  fetch: "readonly",
};

export default [
  // Aset browser: classic script, bukan modul.
  {
    files: ["src/**/*.js"],
    languageOptions: {
      ecmaVersion: 2022,
      sourceType: "script",
      globals: browserGlobals,
    },
    linterOptions: { reportUnusedDisableDirectives: true },
    rules: coreRules,
  },

  // Sisi Node: skrip build, konfigurasi, dan tes. Semuanya ESM.
  {
    files: ["**/*.mjs", "**/*.cjs", "scripts/**/*.js", "tests/**/*.js", "*.config.js"],
    languageOptions: {
      ecmaVersion: 2022,
      sourceType: "module",
      globals: nodeGlobals,
    },
    linterOptions: { reportUnusedDisableDirectives: true },
    rules: coreRules,
  },
];
