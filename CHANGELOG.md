# Changelog

## Unreleased

- Add a built-in **print stylesheet**: ink-friendly high-contrast output, hidden interactive chrome, page-break hygiene, and `.no-print`/`.print-only` helpers.

- Fix dark-mode contrast for `neo-brutalism` and `semantic-minimalist`: their dark variants now override status `*-soft`/`*-text` and `--lc-accent-soft-text` (alerts, soft buttons, and badges were unreadable).

## [0.1.3](https://github.com/codinglombok/LombokCSS/compare/lombokcss-v0.1.2...lombokcss-v0.1.3) (2026-07-31)


### Bug Fixes

* guard lombok.js against environments without a DOM ([15a8c87](https://github.com/codinglombok/LombokCSS/commit/15a8c87f108349eb9300745a3f88044aa60b315d))
* **themes:** restore dark-mode status colors for neo-brutalism ([e8571ab](https://github.com/codinglombok/LombokCSS/commit/e8571ab0aca1b60b09f8232dac34fe63a941b2c2))

## [0.1.2](https://github.com/codinglombok/LombokCSS/compare/lombokcss-v0.1.1...lombokcss-v0.1.2) (2026-07-28)


### Bug Fixes

* **docs:** allow all five styles in switcher, derive allowlist from buttons ([963aa4a](https://github.com/codinglombok/LombokCSS/commit/963aa4a4118964304adb9fbf20ad49c3b96969cc))

## [0.1.1](https://github.com/codinglombok/LombokCSS/compare/lombokcss-v0.1.0...lombokcss-v0.1.1) (2026-07-28)


### Bug Fixes

* **build:** restore print layer in min.css, format src, sync docs assets ([58b8ae8](https://github.com/codinglombok/LombokCSS/commit/58b8ae8b7d7a6ecf2ac17b65a3df44eabbf41e03))
* **build:** use lightningcss Node API; ci(lint): add repo linter configs, ignore generated CHANGELOG ([203684b](https://github.com/codinglombok/LombokCSS/commit/203684b2620f016157a61488ea35d4839a9b7a80))

## 0.1.0

- Initial release.
- Token-first architecture; components read semantic tokens only.
- Five design styles via `data-style`: modern-corporate-flat, resonant-stark,
  neo-brutalism, semantic-minimalist, glassmorphism (with backdrop-filter fallback).
- Independent dark mode (`data-theme` + `prefers-color-scheme`) and RTL (`dir`).
- Components: buttons, card, badge, alert, full forms (inputs, sizes, states,
  input-group, validation), table (sortable), avatar, progress, spinner,
  skeleton, stat, list-group, breadcrumb, pagination, navbar, tabs, accordion,
  dropdown, modal, toast, popover, tooltip, sidebar, drawer/offcanvas, carousel,
  timeline, steps, kbd/code.
- Utility classes incl. status colors and full responsive scale (sm/md/lg/xl).
- Classless mode for semantic HTML.
- Multi-page docs site in `docs/` + single-file playground in `examples/`.
- ~9.5 KB gzipped (CSS) + ~2.2 KB gzipped (optional JS).
