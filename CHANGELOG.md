# Changelog

## Unreleased

- Add a built-in **print stylesheet**: ink-friendly high-contrast output, hidden interactive chrome, page-break hygiene, and `.no-print`/`.print-only` helpers.

- Fix dark-mode contrast for `neo-brutalism` and `semantic-minimalist`: their dark variants now override status `*-soft`/`*-text` and `--lc-accent-soft-text` (alerts, soft buttons, and badges were unreadable).

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
