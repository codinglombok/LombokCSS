# Changelog

## [0.1.8](https://github.com/codinglombok/LombokCSS/compare/v0.1.7...lombokcss-v0.1.8) (2026-08-21)

### Bug Fixes

* build: restore print layer in min.css, format src, sync docs assets (58b8ae8)
* build: use lightningcss Node API; ci(lint): add repo linter configs, ignore generated CHANGELOG (203684b)
* carousel: cancel a pending re-sync when moving to a new target (6b8209a)
* carousel: move to a tracked slide index instead of a scroll delta (67df315)
* docs: allow all five styles in switcher, derive allowlist from buttons (963aa4a)
* guard lombok.js against environments without a DOM (15a8c87)
* themes: restore dark-mode status colors for neo-brutalism (e8571ab)

## [0.1.7](https://github.com/codinglombok/LombokCSS/compare/v0.1.6...v0.1.7) (2026-08-20)

### CI

* sync publish-packages trigger with release-please, add composer.json to version bump

## [0.1.6](https://github.com/codinglombok/LombokCSS/compare/v0.1.5...v0.1.6) (2026-08-20)

### CI

* fix npm --ignore-scripts + Dockerfile COPY README

## [0.1.5](https://github.com/codinglombok/LombokCSS/compare/lombokcss-v0.1.4...v0.1.5) (2026-08-20)

### CI

* standardize npm-publish + add GitHub Packages (all 5 registries)
* add lombokcss package (dist + src + metadata)

## [0.1.8](https://github.com/codinglombok/LombokCSS/compare/lombokcss-v0.1.7...lombokcss-v0.1.8) (2026-08-21)


### Bug Fixes

* **build:** restore print layer in min.css, format src, sync docs assets ([58b8ae8](https://github.com/codinglombok/LombokCSS/commit/58b8ae8b7d7a6ecf2ac17b65a3df44eabbf41e03))
* **build:** use lightningcss Node API; ci(lint): add repo linter configs, ignore generated CHANGELOG ([203684b](https://github.com/codinglombok/LombokCSS/commit/203684b2620f016157a61488ea35d4839a9b7a80))
* **carousel:** cancel a pending re-sync when moving to a new target ([6b8209a](https://github.com/codinglombok/LombokCSS/commit/6b8209af504fd36bb460aca366a10d0255dc4289))
* **carousel:** move to a tracked slide index instead of a scroll delta ([67df315](https://github.com/codinglombok/LombokCSS/commit/67df31596cd0a8fc53619eab3c25c42f82db3201))
* **docs:** allow all five styles in switcher, derive allowlist from buttons ([963aa4a](https://github.com/codinglombok/LombokCSS/commit/963aa4a4118964304adb9fbf20ad49c3b96969cc))
* guard lombok.js against environments without a DOM ([15a8c87](https://github.com/codinglombok/LombokCSS/commit/15a8c87f108349eb9300745a3f88044aa60b315d))
* **themes:** restore dark-mode status colors for neo-brutalism ([e8571ab](https://github.com/codinglombok/LombokCSS/commit/e8571ab0aca1b60b09f8232dac34fe63a941b2c2))

## [0.1.4](https://github.com/codinglombok/LombokCSS/compare/lombokcss-v0.1.3...lombokcss-v0.1.4) (2026-07-31)

### Bug Fixes

* **carousel:** cancel a pending re-sync when moving to a new target ([6b8209a](https://github.com/codinglombok/LombokCSS/commit/6b8209af504fd36bb460aca366a10d0255dc4289))
* **carousel:** move to a tracked slide index instead of a scroll delta ([67df315](https://github.com/codinglombok/LombokCSS/commit/67df31596cd0a8fc53619eab3c25c42f82db3201))

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
- Print stylesheet: ink-friendly high-contrast output, `.no-print`/`.print-only` helpers.
- Multi-page docs site in `docs/` + single-file playground in `examples/`.
- ~9.5 KB gzipped (CSS) + ~2.2 KB gzipped (optional JS).
