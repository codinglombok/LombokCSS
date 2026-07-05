# LombokCSS

> **Switch the look, not the HTML.**

[![CI](https://github.com/codinglombok/lombokcss/actions/workflows/ci.yml/badge.svg)](https://github.com/codinglombok/lombokcss/actions/workflows/ci.yml)
[![Deploy docs](https://github.com/codinglombok/lombokcss/actions/workflows/pages.yml/badge.svg)](https://github.com/codinglombok/lombokcss/actions/workflows/pages.yml)
[![npm version](https://img.shields.io/npm/v/lombokcss.svg)](https://www.npmjs.com/package/lombokcss)
[![npm downloads](https://img.shields.io/npm/dm/lombokcss.svg)](https://www.npmjs.com/package/lombokcss)
[![jsDelivr hits](https://img.shields.io/jsdelivr/npm/hm/lombokcss.svg)](https://www.jsdelivr.com/package/npm/lombokcss)
[![gzip size](https://img.shields.io/badge/gzip-9.7%20KB-success.svg)](#)
[![license](https://img.shields.io/npm/l/lombokcss.svg)](LICENSE)

<p align="center">
  <img src="https://raw.githubusercontent.com/codinglombok/LombokCSS/main/docs/assets/preview.png" alt="LombokCSS — the same markup rendered in five design styles" width="100%">
</p>


A modern, **token-first** component CSS framework. Drop a class, get a working
component — like Bootstrap. Re-theme everything by changing **one attribute** —
like a design system. Ships at **~9.7 KB gzipped** (full build, minified).

```
Component-based (Bootstrap)  +  Token-driven theming (design systems)  +  Tiny (Pico/UnoCSS)
```

---

## Why it's different

Most frameworks bake their look into each component, so changing the visual
style means overriding hundreds of rules. LombokCSS inverts that:

- **Components read only semantic tokens** (`--lc-surface`, `--lc-text`, `--lc-radius`, `--lc-shadow`, `--lc-accent`, …).
- **A "design style" is just a different set of token values.** Switching it never touches component CSS or your HTML.

```html
<!-- same markup, five identities -->
<html data-style="neo-brutalism">      <!-- thick borders, hard shadows -->
<html data-style="glassmorphism">       <!-- frosted glass -->
<html data-style="resonant-stark">       <!-- Linear-style dark -->
```

Dark mode (`data-theme`) and RTL (`dir`) are **independent** axes that compose
with any style.

---

## Install

**CDN (jsDelivr)** — fastest start:
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/lombokcss/dist/lombok.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/lombokcss/dist/lombok.js"></script>
```

**npm:**
```bash
npm install lombokcss
# or: yarn add lombokcss   /   pnpm add lombokcss
```
```js
import "lombokcss/dist/lombok.min.css";
import "lombokcss/dist/lombok.js"; // optional, only for interactive components
```

Pin a version for production (jsDelivr):
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/lombokcss@0.1.0/dist/lombok.min.css">
```

**Download:** grab `dist/lombok.min.css` (+ optional `dist/lombok.js`) and link them directly.

The JS is **optional**. Accordions, modals and `<dialog>` work natively without
it; the script only adds dropdown/tab/toast/table-sort/navbar-toggle behavior.

---



**Other registries.** Also distributed via Composer (`composer require codinglombok/lombokcss`),
RubyGems (`gem "lombokcss"` → `Lombokcss.assets_path` for Sprockets), and Bower
(legacy: `bower install lombokcss`, prefer npm). Works with any bundler
(Vite/Webpack/Parcel) and framework (Vue/React/Svelte) — just import the CSS.
See the **Getting started** docs for per-tool snippets.

## Documentation site

A full multi-page docs site lives in `docs/` (Overview, Getting started, Theming
& styles, Components, Utilities). Open `docs/index.html` in a browser. The style
/ dark / RTL switchers at the top apply live and **follow you across pages** via
the URL query string. A single-file interactive playground is at
`examples/demo.html`.

## Architecture

```
src/
  variables.css   → token architecture (the contract every component depends on)
  core.css        → reset/reboot + base element styles (= classless mode)
  themes.css      → token value sets per design preset (data-style)
  components.css  → all components (read tokens only, RTL-safe, glass-aware)
  utilities.css   → atomic utilities + responsive prefixes
dist/
  lombok.css      → bundled, unminified (readable)
  lombok.min.css  → bundled + minified (ship this)
  lombok.js       → optional interactive behaviors
```

### Token layers
1. **Primitives & scale** — spacing, font sizes, raw palette.
2. **Semantic tokens** — `--lc-surface`, `--lc-text`, `--lc-border`, `--lc-accent`, `--lc-radius`, `--lc-shadow`, `--lc-blur`, status colors. **Components only ever reference these.**
3. **Style presets** (`[data-style="…"]`) re-map the semantic tokens.
4. **Dark overlay** (`[data-theme="dark"]` / `prefers-color-scheme`) re-maps color tokens; composes with presets via `[data-style][data-theme]` pairs.

Glassmorphism support is built into the contract: every surface component
applies `backdrop-filter: var(--lc-blur)`. `--lc-blur` is `none` everywhere
except the glass preset, so the property is inert until a glass theme turns it
on — no per-component glass code.

---

## The five design styles

| `data-style`              | Character |
|---------------------------|-----------|
| `modern-corporate-flat`   | Clean, flat, neutral + one brand color, medium radius, soft shadows (default) |
| `resonant-stark`          | Linear-style dark: high contrast, subtle borders, tight type, violet accent |
| `neo-brutalism`           | Thick black borders, hard offset shadows, bold blocks, zero radius |
| `semantic-minimalist`     | Minimal, neutral, generous spacing, serif display, readability-first |
| `glassmorphism`           | Frosted glass over a gradient; translucent surfaces, glowing borders (with opaque fallback) |

---

## Theming guide

Everything is a CSS variable. Override on `:root` (or a scope) to customize:

```css
:root {
  --lc-accent: #e11d48;          /* brand color            */
  --lc-accent-hover: #be123c;
  --lc-radius: 4px;              /* tighter corners        */
  --lc-font-sans: "Inter", system-ui, sans-serif;
  --lc-space-4: 1.1rem;          /* rescale spacing        */
}
```

**Dark mode** — three ways, they all work together:
```html
<html data-theme="dark">   <!-- force dark           -->
<html data-theme="light">  <!-- force light           -->
<html>                      <!-- follows the OS setting -->
```

**RTL** — set the document direction; all components use logical properties:
```html
<html dir="rtl" lang="ar">
```

**Make your own style** — add a token block, no component edits:
```css
[data-style="sunset"] {
  --lc-bg:#1a0f0f; --lc-surface:#2a1818; --lc-text:#ffe;
  --lc-accent:#ff7849; --lc-radius:14px; --lc-shadow:0 8px 24px rgba(0,0,0,.4);
}
```

---

## Component usage

```html
<!-- Buttons -->
<button class="btn btn-primary">Primary</button>
<button class="btn btn-outline btn-lg btn-rounded">Big outline</button>
<span class="btn-group">
  <button class="btn btn-secondary">L</button><button class="btn btn-secondary">R</button>
</span>

<!-- Card -->
<article class="card">
  <div class="card-body">
    <h3 class="card-title">Title</h3>
    <p class="card-text">Body copy.</p>
  </div>
  <div class="card-footer">Footer</div>
</article>

<!-- Form + validation (native :user-invalid + :has) -->
<form>
  <div class="field">
    <label class="label" for="e">Email</label>
    <input class="input" id="e" type="email" required>
    <span class="help">We never share it.</span>
    <span class="error-text">Enter a valid email.</span>
  </div>
  <label class="switch"><span>Notify me</span><input type="checkbox"><span class="track"></span></label>
</form>

<!-- Alert / Badge -->
<div class="alert alert-success"><div><div class="alert-title">Saved</div>All good.</div></div>
<span class="badge badge-primary">new</span>

<!-- Tabs (JS) -->
<div class="tabs" role="tablist">
  <button role="tab" aria-selected="true" aria-controls="p1">One</button>
  <button role="tab" aria-selected="false" aria-controls="p2">Two</button>
</div>
<div class="tab-panel" id="p1" role="tabpanel">…</div>
<div class="tab-panel" id="p2" role="tabpanel" hidden>…</div>

<!-- Accordion (native, no JS) -->
<div class="accordion">
  <details open><summary>Q</summary><div class="accordion-body">A</div></details>
</div>

<!-- Dropdown (JS) -->
<div class="dropdown">
  <button class="btn btn-soft" data-dropdown-toggle aria-expanded="false">Menu ▾</button>
  <div class="dropdown-menu">
    <a class="dropdown-item" href="#">Item</a>
    <div class="dropdown-divider"></div>
    <button class="dropdown-item">Action</button>
  </div>
</div>

<!-- Modal (native <dialog> + tiny JS helpers) -->
<button class="btn btn-primary" data-modal-open="m">Open</button>
<dialog class="modal" id="m">
  <div class="modal-card">
    <div class="modal-header">Title <button class="btn btn-ghost btn-icon btn-sm" data-modal-close>✕</button></div>
    <div class="modal-body">Body</div>
    <div class="modal-footer"><button class="btn btn-primary" data-modal-close>OK</button></div>
  </div>
</dialog>

<!-- Toast (JS API) -->
<button class="btn" onclick="Lombok.toast('Done', {variant:'success'})">Notify</button>

<!-- Sortable table (JS: click headers) -->
<div class="table-wrap">
  <table class="table table-hover">
    <thead><tr><th aria-sort="none">Name</th><th aria-sort="none">MRR</th></tr></thead>
    <tbody><tr><td>Nadia</td><td>49</td></tr></tbody>
  </table>
</div>

<!-- Carousel (CSS-only, scroll-snap) -->
<div class="carousel"><div class="carousel-track">
  <div class="carousel-slide is-third card">…</div>
  <div class="carousel-slide is-third card">…</div>
</div></div>

<!-- Drawer / Offcanvas (JS) -->
<button class="btn" data-drawer-open="nav">Menu</button>
<aside class="drawer" id="nav">
  <div class="drawer-header">Menu <button class="btn btn-ghost btn-icon btn-sm" data-drawer-close>✕</button></div>
  <div class="drawer-body">…</div>
</aside>
<div class="drawer-overlay" id="nav-overlay"></div>

<!-- Popover (JS) -->
<div class="popover">
  <button class="btn btn-outline" data-popover-toggle aria-expanded="false">Info ▾</button>
  <div class="popover-panel"><div class="popover-title">Title</div><p>Rich content.</p></div>
</div>

<!-- Sidebar -->
<nav class="sidebar">
  <div class="sidebar-title">Workspace</div>
  <a class="sidebar-link is-active" href="#">Dashboard</a>
  <a class="sidebar-link" href="#">Projects</a>
</nav>

<!-- Timeline -->
<ul class="timeline">
  <li><div class="timeline-time">09:00</div><div class="timeline-title">Event</div><p>Detail.</p></li>
</ul>
```

Other components included: `navbar` (+ mobile toggle), `breadcrumb`,
`pagination`, `avatar`/`avatar-group`, `progress`, `spinner`, `skeleton`,
`stat`, `list-group`, `steps`, CSS-only tooltip (`data-tip="…"`), `kbd`, `code`/`pre`.

### Utilities
Layout (`flex`, `grid`, `items-*`, `justify-*`, `gap-*`, `grid-cols-1..12`),
spacing (`p-*`, `m-*`, logical), sizing (`w-full`, `max-w-*`, `min-h-screen`),
type (`text-sm..3xl`, `font-*`, `text-start/center/end`), color
(`bg-surface`, `text-muted`, `border`), radius/shadow, position/z-index, plus
responsive prefixes `sm: md: lg: xl:` (e.g. `md:grid-cols-3`).

### Classless mode
Plain semantic HTML is styled with zero classes — headings, paragraphs, links,
lists, `blockquote`, `table`, form inputs, `code`/`pre`/`kbd`. Good for prose
and quick prototypes.

---

## Build process

The dist files are produced with **Lightning CSS**:

```bash
# bundle the modules in order
cat src/variables.css src/core.css src/themes.css \
    src/components.css src/utilities.css > dist/lombok.css

# minify (autoprefix + dead-code removal)
npx lightningcss --minify --bundle dist/lombok.css -o dist/lombok.min.css
```

PostCSS equivalent: `postcss-import` + `autoprefixer` + `cssnano`.

### Shrinking further
- **Split core vs full:** ship `variables + core + themes + components` and add
  `utilities.css` only if you use utility classes.
- **Purge unused utilities** with your bundler's CSS purge step keyed on your
  templates.
- Drop presets you don't use from `themes.css`.

---

## Browser support & accessibility
Modern CSS used with graceful fallbacks: `:has()`, `:user-invalid`,
`accent-color`, `backdrop-filter` (opaque fallback via `@supports`), logical
properties, native `<dialog>`/`<details>`. Components ship with visible
`:focus-visible` rings, ARIA hooks, and respect `prefers-reduced-motion`.

## Testing

Visual-regression tests (Playwright) screenshot the buttons block across all
five styles plus dark/RTL, and the form validation state, comparing against
committed baselines in `tests/**-snapshots/`.

```bash
npm run test:visual          # compare against baselines
npm run test:visual:update   # refresh baselines after an intentional change
```

Baselines are browser-specific. CI runs in a pinned Playwright container
(`mcr.microsoft.com/playwright:v1.56.0-noble`) so pixels match. When you change
visuals on purpose, refresh baselines **inside that image** so they match CI:

```bash
docker run --rm -v "$PWD":/work -w /work mcr.microsoft.com/playwright:v1.56.0-noble \
  bash -c "npm ci && npm run build && npm run build:docs && npm run test:visual:update"
```

A failing run uploads a `playwright-report` artifact with side-by-side diffs.

## Publishing (maintainers)

> Full step-by-step setup (repo creation, branch protection, secrets, Pages,
> release-please flow, npm/CDN, troubleshooting) is in **[GITHUB_SETUP.md](GITHUB_SETUP.md)**.

The package ships only `dist/`, `src/`, `README.md` and `LICENSE` (see the
`files` field). `prepublishOnly` rebuilds the bundle and enforces the size
budget, so a broken or oversized build can never be published.

**Automated (recommended).** Two GitHub Actions workflows are included:

- `.github/workflows/ci.yml` — on every push/PR: `npm ci`, `npm run build`,
  size-budget check, and a guard that fails if committed `dist/` is stale.
- `.github/workflows/publish.yml` — on a published GitHub Release: builds and
  runs `npm publish --provenance --access public`. Add an `NPM_TOKEN` repo
  secret (an npm automation token); provenance uses the workflow's OIDC token.

Release flow:
```bash
npm version patch        # or minor / major — bumps package.json + git tag
git push --follow-tags
# then create a GitHub Release for that tag -> publish workflow runs
```

**Manual:**
```bash
npm run build
npm publish --access public
```

**CDN is automatic.** Once on npm, jsDelivr and unpkg serve it with no extra
step: `https://cdn.jsdelivr.net/npm/lombokcss@<version>/dist/lombok.min.css`.
The `jsdelivr` / `unpkg` fields point both CDNs at the minified CSS by default.

**Docs hosting (GitHub Pages).** `.github/workflows/pages.yml` rebuilds the
docs and deploys `docs/` to Pages on every push to `main`. Enable it once in
repo **Settings → Pages → Source: GitHub Actions**. Site goes live at
`https://codinglombok.github.io/lombokcss/`.

Need help? See **[SUPPORT.md](SUPPORT.md)**.

## License
MIT.
