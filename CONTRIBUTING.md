# Contributing to LombokCSS

Thanks for helping improve LombokCSS! This guide covers local setup, the
architecture rules that keep the framework small and themeable, and the PR flow.

## Prerequisites

- **Node.js ≥ 18** (CI uses 20)
- **Python 3** (only for regenerating the docs site via `build_docs.py`)

## Setup

```bash
git clone https://github.com/codinglombok/lombokcss.git
cd lombokcss
npm install
```

## Common tasks

```bash
npm run build         # bundle src/ -> dist/lombok.css + dist/lombok.min.css
npm run build:docs    # regenerate docs/ and sync docs/assets
npm run size          # print gzipped sizes
npm run size:check    # enforce the size budget (CI gate)
npm run format        # Prettier write
npm run format:check  # Prettier check
npm run test:visual   # Playwright visual-regression tests
npm run test:visual:update  # refresh screenshot baselines
```

Edit source in `src/` — **never edit `dist/` by hand**; it is generated.
After editing source, run `npm run build` and commit the updated `dist/`
(CI fails if `dist/` is stale).

## Architecture rules (please follow)

1. **Components read tokens only.** A component must reference semantic
   variables (`--lc-surface`, `--lc-text`, `--lc-radius`, `--lc-shadow`,
   `--lc-accent`, `--lc-blur`, …) — never hard-coded colors, radii or shadows.
   This is what lets one `data-style` re-skin everything.
2. **A new design style = a token block only** in `themes.css`. Do not add
   per-style component CSS.
3. **RTL-safe.** Use logical properties (`margin-inline`, `inset-inline-start`,
   `border-start-start-radius`, …), never `left`/`right`.
4. **Glass-aware surfaces** apply `backdrop-filter: var(--lc-blur)` (inert when
   `none`) so they frost automatically under the glass style.
5. **Accessibility.** Keep visible `:focus-visible` rings, ARIA hooks, and
   `prefers-reduced-motion` handling.
6. **Stay small.** Keep within the size budget (`scripts/size-check.mjs`).

## Adding a component

1. Add styles to `src/components.css` (tokens only).
2. If interactive, add a small handler to `src/lombok.js` and ensure it
   degrades gracefully without JS.
3. Document it in `build_docs.py` (Components or Forms page) with a live
   example + code, then `npm run build && npm run build:docs`.
4. Add/refresh a visual snapshot if it affects above-the-fold layout.

## Commit & PR

- Use clear messages; Conventional Commits encouraged
  (`feat:`, `fix:`, `docs:`, `refactor:`, `chore:`).
- Before opening a PR: `npm run build && npm run size:check && npm run test:visual`.
- Describe the change and include before/after screenshots for visual changes.
- By contributing you agree your work is licensed under the project's MIT license.

## Code style

Prettier governs formatting (`.prettierrc`); `.editorconfig` covers indentation
and line endings. Run `npm run format` before committing.
