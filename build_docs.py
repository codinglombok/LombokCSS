#!/usr/bin/env python3
import html as H

PAGES = [
    ("index.html",           "Overview"),
    ("getting-started.html", "Getting started"),
    ("migration.html",       "Migration from Bootstrap"),
    ("theming.html",         "Theming & styles"),
    ("components.html",      "Components"),
    ("forms.html",           "Forms"),
    ("utilities.html",       "Utilities"),
    ("accessibility.html",   "Accessibility"),
]

NAV = """
<div class="docs-navtitle">Guide</div>
<nav class="docs-nav">
  <a data-page="index.html">Overview</a>
  <a data-page="getting-started.html">Getting started</a>
  <a data-page="migration.html">Migration from Bootstrap</a>
  <a data-page="theming.html">Theming &amp; styles</a>
</nav>
<div class="docs-navtitle">Reference</div>
<nav class="docs-nav">
  <a data-page="components.html">Components</a>
  <a data-page="forms.html">Forms</a>
  <a data-page="utilities.html">Utilities</a>
  <a data-page="accessibility.html">Accessibility</a>
</nav>
"""

def shell(active_file, title, content):
    nav = NAV
    # mark active link
    nav = nav.replace('data-page="%s"' % active_file,
                      'data-page="%s" class="is-active"' % active_file)
    return f"""<!DOCTYPE html>
<html lang="en" data-style="modern-corporate-flat" data-theme="light" dir="ltr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · LombokCSS — switch the look, not the HTML</title>
<meta name="description" content="Switch the look, not the HTML. LombokCSS is a token-first component CSS framework: one markup, five design styles, dark mode and RTL, in ~9.7 KB.">
<meta property="og:title" content="LombokCSS — switch the look, not the HTML">
<meta property="og:description" content="One markup, five design styles, dark mode & RTL. A token-first component framework in ~9.7 KB.">
<meta property="og:type" content="website">
<meta property="og:image" content="https://raw.githubusercontent.com/codinglombok/LombokCSS/main/docs/assets/social-preview.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="LombokCSS — switch the look, not the HTML">
<meta name="twitter:image" content="https://raw.githubusercontent.com/codinglombok/LombokCSS/main/docs/assets/social-preview.png">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<link rel="manifest" href="site.webmanifest">
<meta name="theme-color" content="#3b82f6">
<link rel="stylesheet" href="assets/lombok.min.css">
<link rel="stylesheet" href="assets/docs.css">
</head>
<body>
<div class="docs">
  <aside class="docs-aside no-print">
    <a class="docs-brand" data-page="index.html">LombokCSS</a>
    <div class="docs-tagline" style="margin:-4px 0 14px;font-size:12px;line-height:1.35;color:var(--lc-text-muted)">Switch the look, not the HTML.</div>
    {nav}
  </aside>
  <div class="docs-main">
    <header class="docs-top no-print">
      <button class="btn btn-ghost btn-sm docs-burger" aria-label="Menu">☰</button>
      <div class="seg" role="radiogroup" aria-label="Design style">
        <button data-style-set="modern-corporate-flat">Corporate</button>
        <button data-style-set="resonant-stark">Stark</button>
        <button data-style-set="neo-brutalism">Brutalism</button>
        <button data-style-set="semantic-minimalist">Minimal</button>
        <button data-style-set="glassmorphism">Glass</button>
      </div>
      <div class="docs-toggles">
        <label class="switch"><span class="text-sm">Dark</span><input type="checkbox" id="dk"><span class="track"></span></label>
        <label class="switch"><span class="text-sm">RTL</span><input type="checkbox" id="rt"><span class="track"></span></label>
      </div>
    </header>
    <main class="docs-content">
{content}
    </main>
  </div>
</div>
<div class="toast-region" aria-live="polite"></div>
<script src="assets/lombok.js"></script>
<script src="assets/docs.js"></script>
</body>
</html>
"""

def ex(example_html, code=None):
    """Rendered example box + escaped code block."""
    code = code if code is not None else example_html
    return ('<div class="example">\n' + example_html + '\n</div>\n'
            '<pre><code>' + H.escape(code.strip()) + '</code></pre>\n')

# ---------------------------------------------------------------- OVERVIEW
overview = """
<h1>LombokCSS</h1>
<p class="lead"><strong>Switch the look, not the HTML.</strong> A token-first component framework: drop a class, get a working component — then re-skin the whole page by changing one attribute.</p>
<p>Use the controls at the top to switch design style, dark mode and RTL. Every example on these pages reacts live, and your selection follows you between pages.</p>

<div class="grid grid-cols-1 md:grid-cols-3 gap-4 mt-6">
  <div class="card"><div class="card-body"><h3 class="card-title">Component-based</h3><p class="card-text">Ready-made buttons, cards, forms, modals, navbars and more.</p></div></div>
  <div class="card"><div class="card-body"><h3 class="card-title">Token-driven</h3><p class="card-text">Five design styles + dark + RTL, all from CSS variables.</p></div></div>
  <div class="card"><div class="card-body"><h3 class="card-title">Tiny</h3><p class="card-text">~9.5&nbsp;KB gzipped for the full build. JS is optional.</p></div></div>
</div>

<h2>Quick start</h2>
<p>Drop in the CDN links and start writing markup:</p>
<pre><code>&lt;link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/lombokcss/dist/lombok.min.css"&gt;
&lt;script defer src="https://cdn.jsdelivr.net/npm/lombokcss/dist/lombok.js"&gt;&lt;/script&gt;</code></pre>
""" + ex(
'<button class="btn btn-primary">Primary</button>\n<button class="btn btn-outline">Outline</button>\n<span class="badge badge-success">live</span>',
'<button class="btn btn-primary">Primary</button>\n<button class="btn btn-outline">Outline</button>\n<span class="badge badge-success">live</span>'
) + """
<h2>Three pillars</h2>
<p>Component classes give you Bootstrap-style speed. Utility classes give you Tailwind-style control. The token layer keeps the whole thing Pico-small and lets a single <code>data-style</code> attribute restyle everything without touching your HTML.</p>
"""

# ---------------------------------------------------------------- GETTING STARTED
getting = """
<h1>Getting started</h1>

<h2>Install</h2>
<p>LombokCSS is plain CSS + an optional plain-JS file, so it works with every
package manager, bundler and framework. Pick whichever fits your stack.</p>

<h3>Package managers (npm registry)</h3>
<p>npm, Yarn and pnpm all read the same package — use whichever you have.</p>
<pre><code>npm install lombokcss
yarn add lombokcss
pnpm add lombokcss</code></pre>
<p>Then import the CSS once (and the optional JS for interactive components):</p>
<pre><code>import "lombokcss/dist/lombok.min.css";
import "lombokcss/dist/lombok.js"; // optional</code></pre>

<h3>CDN (jsDelivr / unpkg)</h3>
<pre><code>&lt;link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/lombokcss@0.1.0/dist/lombok.min.css"&gt;
&lt;script defer src="https://cdn.jsdelivr.net/npm/lombokcss@0.1.0/dist/lombok.js"&gt;&lt;/script&gt;
&lt;!-- or unpkg: https://unpkg.com/lombokcss@0.1.0/dist/lombok.min.css --&gt;</code></pre>

<h3>Composer (PHP / Packagist)</h3>
<pre><code>composer require codinglombok/lombokcss
&lt;!-- then reference vendor/codinglombok/lombokcss/dist/lombok.min.css --&gt;</code></pre>

<h3>RubyGems (Rails / Sprockets)</h3>
<pre><code># Gemfile
gem "lombokcss"

# config/initializers/assets.rb
Rails.application.config.assets.paths &lt;&lt; Lombokcss.assets_path
# app/assets/stylesheets/application.css  ->  *= require lombok.min</code></pre>

<h3>Direct download</h3>
<p>Grab <code>dist/lombok.min.css</code> (and optional <code>dist/lombok.js</code>) and link them.</p>

<h2>Bundler & framework integrations</h2>
<p>Because it ships standard <code>.css</code> and <code>.js</code>, there is no special plugin to install.</p>

<h3>Vite</h3>
<pre><code>// main.js
import "lombokcss/dist/lombok.min.css";
import "lombokcss/dist/lombok.js";</code></pre>

<h3>Webpack</h3>
<pre><code>// requires css-loader + style-loader (or MiniCssExtractPlugin) in your config
import "lombokcss/dist/lombok.min.css";
import "lombokcss/dist/lombok.js";</code></pre>

<h3>Parcel</h3>
<pre><code>// Parcel handles CSS imports out of the box
import "lombokcss/dist/lombok.min.css";</code></pre>

<h3>Vue (and React, Svelte, etc.)</h3>
<p>Import the CSS once in your entry file, then use the classes in templates.</p>
<pre><code>// main.js (Vue entry)
import { createApp } from "vue";
import App from "./App.vue";
import "lombokcss/dist/lombok.min.css";
import "lombokcss/dist/lombok.js";
createApp(App).mount("#app");

&lt;!-- App.vue --&gt;
&lt;button class="btn btn-primary"&gt;Save&lt;/button&gt;</code></pre>
<p>Set the style globally on <code>&lt;html&gt;</code>:
<code>document.documentElement.dataset.style = "neo-brutalism"</code>.</p>

<blockquote><strong>Bower</strong> is included for legacy setups
(<code>bower install lombokcss</code>) but Bower is deprecated — prefer npm/Yarn/pnpm.</blockquote>

<h2>File structure</h2>
<pre><code>src/
  variables.css   token architecture (the contract)
  core.css        reset + base element styles (classless mode)
  themes.css      token values per design style
  components.css  components (read tokens only)
  utilities.css   atomic utilities + responsive prefixes
dist/
  lombok.css      bundled, readable
  lombok.min.css  bundled + minified (ship this)
  lombok.js       optional interactive behaviors</code></pre>

<h2>Classless mode</h2>
<p>Plain semantic HTML is styled with zero classes — good for prose and prototypes.</p>
""" + ex(
'<div style="max-inline-size:32rem">\n  <h3 style="margin-top:0">A heading</h3>\n  <p>A paragraph with a <a href="#">link</a>, some <code>inline code</code> and a <kbd>⌘</kbd><kbd>K</kbd> shortcut.</p>\n  <blockquote>Tokens are the contract; styles are signatures on it.</blockquote>\n</div>',
'<h3>A heading</h3>\n<p>A paragraph with a <a href="#">link</a>, some <code>inline code</code>\n   and a <kbd>⌘</kbd><kbd>K</kbd> shortcut.</p>\n<blockquote>Tokens are the contract; styles are signatures on it.</blockquote>'
) + """
<h2>Build process</h2>
<p>The dist files are produced with Lightning CSS:</p>
<pre><code>cat src/variables.css src/core.css src/themes.css \\
    src/components.css src/utilities.css > dist/lombok.css
npx lightningcss --minify --bundle dist/lombok.css -o dist/lombok.min.css</code></pre>
<p>PostCSS equivalent: <code>postcss-import</code> + <code>autoprefixer</code> + <code>cssnano</code>. To shrink further, ship <code>utilities.css</code> only if you use utility classes, purge unused classes against your templates, and drop styles you don't use from <code>themes.css</code>.</p>

<h2>Browser support &amp; accessibility</h2>
<p>Modern CSS with graceful fallbacks: <code>:has()</code>, <code>:user-invalid</code>, <code>accent-color</code>, <code>backdrop-filter</code> (opaque fallback via <code>@supports</code>), logical properties, native <code>&lt;dialog&gt;</code>/<code>&lt;details&gt;</code>. Components ship with visible focus rings, ARIA hooks and respect <code>prefers-reduced-motion</code>.</p>
"""

# ---------------------------------------------------------------- THEMING
def style_preview(style, label):
    block = (f'<div data-style="{style}" style="flex:1 1 220px;border-radius:12px;overflow:hidden;border:1px solid var(--lc-border)">'
             f'<div style="background:var(--lc-bg);padding:16px;display:flex;flex-direction:column;gap:10px">'
             f'<strong style="color:var(--lc-text)">{label}</strong>'
             f'<button class="btn btn-primary btn-sm">Button</button>'
             f'<div class="card"><div class="card-body" style="padding:12px"><span class="badge badge-primary">badge</span> <span style="color:var(--lc-text-muted);font-size:13px">card surface</span></div></div>'
             f'</div></div>')
    return block

theming = """
<h1>Theming &amp; styles</h1>
<p class="lead">Components read only semantic tokens. A "design style" is just a different set of values for those tokens — switching it never touches component CSS or your HTML.</p>

<h2>The token contract</h2>
<p>Every component references variables like these. Override them anywhere to customize.</p>
<pre><code>--lc-bg, --lc-surface, --lc-surface-2     /* backgrounds */
--lc-text, --lc-text-muted, --lc-text-faint
--lc-border, --lc-border-strong, --lc-border-width
--lc-accent, --lc-accent-hover, --lc-accent-text, --lc-accent-soft
--lc-radius-sm, --lc-radius, --lc-radius-lg, --lc-radius-full
--lc-shadow-sm, --lc-shadow, --lc-shadow-lg, --lc-shadow-hard
--lc-blur                                  /* glass backdrop-filter */
--lc-space-1 … --lc-space-12, --lc-text-xs … --lc-text-4xl</code></pre>

<h2>The five styles</h2>
<p>Set <code>data-style</code> on <code>&lt;html&gt;</code> (or any element, to scope it). These previews each pin one style locally:</p>
<div class="example" style="align-items:stretch">
""" + "\n".join([
    style_preview("modern-corporate-flat","Corporate Flat"),
    style_preview("resonant-stark","Resonant Stark"),
    style_preview("neo-brutalism","Neo-Brutalism"),
    style_preview("semantic-minimalist","Minimalist"),
    style_preview("glassmorphism","Glassmorphism"),
]) + """
</div>
<pre><code>&lt;html data-style="neo-brutalism"&gt;        &lt;!-- thick borders, hard shadows --&gt;
&lt;html data-style="glassmorphism"&gt;        &lt;!-- frosted glass over a gradient --&gt;
&lt;html data-style="resonant-stark"&gt;       &lt;!-- Linear-style dark --&gt;</code></pre>

<h2>Dark mode</h2>
<p>An independent axis that composes with any style. Three modes:</p>
<pre><code>&lt;html data-theme="dark"&gt;    &lt;!-- force dark --&gt;
&lt;html data-theme="light"&gt;   &lt;!-- force light --&gt;
&lt;html&gt;                       &lt;!-- follow the OS setting --&gt;</code></pre>

<h2>RTL</h2>
<p>Set the document direction; all components use logical properties and mirror automatically.</p>
<pre><code>&lt;html dir="rtl" lang="ar"&gt;</code></pre>

<h2>Make your own style</h2>
<p>Add a token block — no component edits required.</p>
<pre><code>[data-style="sunset"] {
  --lc-bg:#1a0f0f; --lc-surface:#2a1818; --lc-text:#ffe;
  --lc-accent:#ff7849; --lc-radius:14px;
  --lc-shadow:0 8px 24px rgba(0,0,0,.4);
}</code></pre>
"""

# ---------------------------------------------------------------- COMPONENTS
components = """
<h1>Components</h1>
<p class="lead">Every example below reacts to the style / dark / RTL controls at the top.</p>

<h2>Buttons</h2>
""" + ex('<button class="btn btn-primary">Primary</button>\n<button class="btn btn-secondary">Secondary</button>\n<button class="btn btn-outline">Outline</button>\n<button class="btn btn-soft">Soft</button>\n<button class="btn btn-ghost">Ghost</button>\n<button class="btn btn-link">Link</button>\n<button class="btn btn-danger">Danger</button>') \
+ ex('<button class="btn btn-primary btn-sm">Small</button>\n<button class="btn btn-primary">Default</button>\n<button class="btn btn-primary btn-lg">Large</button>\n<button class="btn btn-primary btn-rounded">Rounded</button>\n<span class="btn-group"><button class="btn btn-secondary">L</button><button class="btn btn-secondary">M</button><button class="btn btn-secondary">R</button></span>') + """

<h2>Card</h2>
""" + ex('<article class="card" style="max-inline-size:340px">\n  <div class="card-header">Header</div>\n  <div class="card-body"><h3 class="card-title">Title</h3><p class="card-text">Body copy goes here.</p></div>\n  <div class="card-footer">Footer</div>\n</article>') + """

<h2>Badge &amp; Pill</h2>
""" + ex('<span class="badge">default</span>\n<span class="badge badge-primary">primary</span>\n<span class="badge badge-success">success</span>\n<span class="badge badge-warning">warning</span>\n<span class="badge badge-danger">danger</span>\n<span class="badge badge-pill badge-info">pill</span>\n<span class="badge badge-solid">solid</span>') + """

<h2>Alert</h2>
""" + ex('<div style="display:flex;flex-direction:column;gap:8px;inline-size:100%">\n  <div class="alert alert-info"><div><div class="alert-title">Info</div>Something to note.</div></div>\n  <div class="alert alert-success"><div><div class="alert-title">Saved</div>All good.</div></div>\n  <div class="alert alert-danger"><div><div class="alert-title">Failed</div>Could not reach the server.</div></div>\n</div>',
'<div class="alert alert-info"><div><div class="alert-title">Info</div>Something to note.</div></div>') + """

<h2>Form &amp; validation</h2>
<p>Validation uses native <code>:user-invalid</code> + <code>:has()</code>. Type an invalid email and blur the field to reveal the error.</p>
""" + ex('<form style="inline-size:100%;max-inline-size:420px">\n  <div class="field">\n    <label class="label" for="de">Email</label>\n    <input class="input" id="de" type="email" placeholder="you@example.com" required>\n    <span class="help">We never share it.</span>\n    <span class="error-text">Enter a valid email.</span>\n  </div>\n  <div class="field"><label class="label" for="ds">Role</label>\n    <select class="select" id="ds"><option>Engineer</option><option>Designer</option></select></div>\n  <div class="check"><input type="checkbox" id="dc"><label for="dc">I agree</label></div>\n  <label class="switch mt-2"><span>Notify me</span><input type="checkbox" checked><span class="track"></span></label>\n</form>',
'<div class="field">\n  <label class="label" for="e">Email</label>\n  <input class="input" id="e" type="email" required>\n  <span class="help">We never share it.</span>\n  <span class="error-text">Enter a valid email.</span>\n</div>\n<label class="switch"><span>Notify me</span><input type="checkbox"><span class="track"></span></label>') + """

<h2>Avatar &amp; Progress</h2>
""" + ex('<span class="avatar">AR</span>\n<span class="avatar avatar-lg">LG</span>\n<span class="avatar-group"><span class="avatar avatar-sm">A</span><span class="avatar avatar-sm">B</span><span class="avatar avatar-sm">C</span></span>\n<div class="progress" style="inline-size:160px"><div class="bar" style="inline-size:60%"></div></div>\n<span class="spinner"></span') + """

<h2>Tabs</h2>
""" + ex('<div style="inline-size:100%">\n  <div class="tabs" role="tablist">\n    <button role="tab" aria-selected="true" aria-controls="dx1">One</button>\n    <button role="tab" aria-selected="false" aria-controls="dx2">Two</button>\n  </div>\n  <div class="tab-panel" id="dx1" role="tabpanel">First panel.</div>\n  <div class="tab-panel" id="dx2" role="tabpanel" hidden>Second panel.</div>\n</div>') + """

<h2>Accordion</h2>
""" + ex('<div class="accordion" style="inline-size:100%">\n  <details open><summary>What is it?</summary><div class="accordion-body">A token-first framework.</div></details>\n  <details><summary>Build step?</summary><div class="accordion-body">None required.</div></details>\n</div>') + """

<h2>Dropdown</h2>
""" + ex('<div class="dropdown">\n  <button class="btn btn-soft" data-dropdown-toggle aria-expanded="false">Menu ▾</button>\n  <div class="dropdown-menu">\n    <a class="dropdown-item" href="#">Profile</a>\n    <a class="dropdown-item" href="#">Settings</a>\n    <div class="dropdown-divider"></div>\n    <button class="dropdown-item">Sign out</button>\n  </div>\n</div>') + """

<h2>Modal</h2>
""" + ex('<button class="btn btn-primary" data-modal-open="dlgDocs">Open modal</button>\n<dialog class="modal" id="dlgDocs">\n  <div class="modal-card">\n    <div class="modal-header">Title <button class="btn btn-ghost btn-icon btn-sm" data-modal-close>✕</button></div>\n    <div class="modal-body"><p class="mb-0">Native &lt;dialog&gt; — Esc, backdrop click and focus trapping included.</p></div>\n    <div class="modal-footer"><button class="btn btn-ghost" data-modal-close>Cancel</button><button class="btn btn-primary" data-modal-close>OK</button></div>\n  </div>\n</dialog>') + """

<h2>Toast</h2>
""" + ex("<button class=\"btn btn-secondary\" onclick=\"Lombok.toast('Saved',{variant:'success'})\">Fire toast</button>",
'Lombok.toast("Saved", { variant: "success" });') + """

<h2>Popover</h2>
""" + ex('<div class="popover">\n  <button class="btn btn-outline" data-popover-toggle aria-expanded="false">Show ▾</button>\n  <div class="popover-panel"><div class="popover-title">Popover</div><p class="card-text mb-0">Click-triggered, holds any content.</p></div>\n</div>') + """

<h2>Tooltip</h2>
""" + ex('<button class="btn btn-soft" data-tip="I am a tooltip">Hover me</button>') + """

<h2>Breadcrumb &amp; Pagination</h2>
""" + ex('<nav><ul class="breadcrumb"><li><a href="#">Home</a></li><li><a href="#">Docs</a></li><li aria-current="page">Components</li></ul></nav>') \
+ ex('<ul class="pagination"><li><a href="#">‹</a></li><li class="is-active"><a href="#">1</a></li><li><a href="#">2</a></li><li><a href="#">3</a></li><li><a href="#">›</a></li></ul>') + """

<h2>List group</h2>
""" + ex('<div class="list-group" style="inline-size:100%;max-inline-size:320px">\n  <a class="list-group-item is-active" href="#">Inbox</a>\n  <a class="list-group-item" href="#">Starred</a>\n  <a class="list-group-item" href="#">Archive</a>\n</div>') + """

<h2>Table (sortable)</h2>
<p>Click a header to sort.</p>
""" + ex('<div class="table-wrap" style="inline-size:100%">\n  <table class="table table-hover">\n    <thead><tr><th aria-sort="none">Name</th><th aria-sort="none">Plan</th><th aria-sort="none">MRR</th></tr></thead>\n    <tbody>\n      <tr><td>Nadia</td><td>Pro</td><td>49</td></tr>\n      <tr><td>Bayu</td><td>Team</td><td>199</td></tr>\n      <tr><td>Citra</td><td>Free</td><td>0</td></tr>\n    </tbody>\n  </table>\n</div>') + """

<h2>Sidebar</h2>
""" + ex('<nav class="sidebar" style="border-radius:10px">\n  <div class="sidebar-title">Workspace</div>\n  <a class="sidebar-link is-active" href="#">Dashboard</a>\n  <a class="sidebar-link" href="#">Projects</a>\n  <a class="sidebar-link" href="#">Team</a>\n</nav>') + """

<h2>Drawer / Offcanvas</h2>
""" + ex('<button class="btn btn-primary" data-drawer-open="dDocs">Open drawer</button>\n<aside class="drawer" id="dDocs">\n  <div class="drawer-header">Menu <button class="btn btn-ghost btn-icon btn-sm" data-drawer-close>✕</button></div>\n  <div class="drawer-body">Drawer content. Esc or click outside to close.</div>\n</aside>\n<div class="drawer-overlay" id="dDocs-overlay"></div>') + """

<h2>Carousel</h2>
""" + ex('<div class="carousel" style="inline-size:100%">\n  <button class="carousel-btn carousel-prev" aria-label="Previous">‹</button>\n  <button class="carousel-btn carousel-next" aria-label="Next">›</button>\n  <div class="carousel-track">\n    <div class="carousel-slide is-third card"><div class="card-body">Slide 1</div></div>\n    <div class="carousel-slide is-third card"><div class="card-body">Slide 2</div></div>\n    <div class="carousel-slide is-third card"><div class="card-body">Slide 3</div></div>\n    <div class="carousel-slide is-third card"><div class="card-body">Slide 4</div></div>\n  </div>\n  <div class="carousel-dots"><button class="is-active"></button><button></button><button></button><button></button></div>\n</div>') + """

<h2>Timeline &amp; Steps</h2>
""" + ex('<ul class="timeline" style="inline-size:100%;max-inline-size:420px">\n  <li><div class="timeline-time">09:00</div><div class="timeline-title">Started</div><p class="card-text mb-0">Kickoff.</p></li>\n  <li><div class="timeline-time">14:00</div><div class="timeline-title">Shipped</div><p class="card-text mb-0">Done.</p></li>\n</ul>') \
+ ex('<ul class="steps" style="inline-size:100%;max-inline-size:360px"><li class="is-done">Account</li><li class="is-active">Profile</li><li>Done</li></ul>')

# ---------------------------------------------------------------- FORMS (deep)
forms = """
<h1>Forms</h1>
<p class="lead">A complete guide to inputs, controls, layout, sizing, states and validation. Every example reacts to the style / dark / RTL controls above.</p>

<h2>Anatomy of a field</h2>
<p>Wrap each control in <code>.field</code>. Pair it with <code>.label</code>, optional <code>.help</code> text, and a hidden <code>.error-text</code> that appears on invalid input. <code>.field</code> stacks these with consistent spacing.</p>
""" + ex('<div class="field" style="inline-size:100%;max-inline-size:420px">\n  <label class="label" for="fa">Full name</label>\n  <input class="input" id="fa" placeholder="Jane Doe">\n  <span class="help">As it appears on your ID.</span>\n</div>',
'<div class="field">\n  <label class="label" for="name">Full name</label>\n  <input class="input" id="name" placeholder="Jane Doe">\n  <span class="help">As it appears on your ID.</span>\n</div>') + """

<h2>Text inputs</h2>
<p>The <code>.input</code> class works on every text-like type. Bare <code>&lt;input&gt;</code> is also styled in classless mode.</p>
""" + ex('<div style="display:grid;gap:10px;inline-size:100%;max-inline-size:420px">\n  <input class="input" type="text" placeholder="Text">\n  <input class="input" type="email" placeholder="Email">\n  <input class="input" type="password" placeholder="Password">\n  <input class="input" type="number" placeholder="Number">\n  <input class="input" type="date">\n  <input class="input" type="search" placeholder="Search">\n</div>',
'<input class="input" type="text" placeholder="Text">\n<input class="input" type="email" placeholder="Email">\n<input class="input" type="date">') + """

<h2>Textarea &amp; Select</h2>
""" + ex('<div style="display:grid;gap:10px;inline-size:100%;max-inline-size:420px">\n  <textarea class="textarea" placeholder="Your message…"></textarea>\n  <select class="select"><option>Choose a plan</option><option>Free</option><option>Pro</option><option>Team</option></select>\n</div>',
'<textarea class="textarea" placeholder="Your message…"></textarea>\n<select class="select">\n  <option>Free</option><option>Pro</option>\n</select>') + """

<h2>Sizes</h2>
<p>Add <code>.input-sm</code> / <code>.input-lg</code> (and <code>.select-sm</code> / <code>.select-lg</code>).</p>
""" + ex('<div style="display:grid;gap:10px;inline-size:100%;max-inline-size:420px">\n  <input class="input input-sm" placeholder="Small">\n  <input class="input" placeholder="Default">\n  <input class="input input-lg" placeholder="Large">\n</div>',
'<input class="input input-sm" placeholder="Small">\n<input class="input" placeholder="Default">\n<input class="input input-lg" placeholder="Large">') + """

<h2>States</h2>
<p>Disabled and read-only are handled natively; valid / invalid use the validation hooks below.</p>
""" + ex('<div style="display:grid;gap:10px;inline-size:100%;max-inline-size:420px">\n  <input class="input" value="Disabled" disabled>\n  <input class="input" value="Read-only" readonly>\n  <input class="input is-valid" value="Looks good">\n  <input class="input is-invalid" value="Something off">\n</div>',
'<input class="input" value="Disabled" disabled>\n<input class="input" value="Read-only" readonly>\n<input class="input is-valid" value="Looks good">\n<input class="input is-invalid" value="Something off">') + """

<h2>Checkbox, Radio &amp; Switch</h2>
<p>Native controls themed with <code>accent-color</code>, so they match every style automatically.</p>
""" + ex('<div style="display:grid;gap:8px">\n  <div class="check"><input type="checkbox" id="fc1" checked><label for="fc1">Subscribe to updates</label></div>\n  <div class="check"><input type="checkbox" id="fc2"><label for="fc2">Enable two-factor auth</label></div>\n  <div class="check"><input type="radio" name="plan" id="fr1" checked><label for="fr1">Monthly</label></div>\n  <div class="check"><input type="radio" name="plan" id="fr2"><label for="fr2">Yearly</label></div>\n  <label class="switch mt-2"><span>Email notifications</span><input type="checkbox" checked><span class="track"></span></label>\n</div>',
'<div class="check"><input type="checkbox" id="c1"><label for="c1">Subscribe</label></div>\n<div class="check"><input type="radio" name="plan" id="r1"><label for="r1">Monthly</label></div>\n<label class="switch"><span>Notifications</span><input type="checkbox"><span class="track"></span></label>') + """

<h2>File upload</h2>
""" + ex('<input type="file">',
'<input type="file">') + """

<h2>Input group</h2>
<p>Join inputs with leading/trailing addons or buttons using <code>.input-group</code> + <code>.input-addon</code>. Radii and borders are handled on the ends, and it mirrors correctly in RTL.</p>
""" + ex('<div style="display:grid;gap:10px;inline-size:100%;max-inline-size:420px">\n  <div class="input-group"><span class="input-addon">@</span><input class="input" placeholder="username"></div>\n  <div class="input-group"><span class="input-addon">https://</span><input class="input" placeholder="site.com"></div>\n  <div class="input-group"><input class="input" placeholder="Search…"><button class="btn btn-primary">Go</button></div>\n  <div class="input-group"><input class="input" value="1,250.00"><span class="input-addon">USD</span></div>\n</div>',
'<div class="input-group">\n  <span class="input-addon">@</span>\n  <input class="input" placeholder="username">\n</div>\n\n<div class="input-group">\n  <input class="input" placeholder="Search…">\n  <button class="btn btn-primary">Go</button>\n</div>') + """

<h2>Validation</h2>
<p>LombokCSS layers two validation systems so you can use whichever fits:</p>
<h3>1. Native, zero-JS</h3>
<p>With <code>required</code> / <code>type</code> constraints, the browser sets <code>:user-invalid</code> after the user interacts. <code>.field:has(:user-invalid)</code> reveals the <code>.error-text</code> and hides <code>.help</code> automatically — no script. Type a bad email and click away:</p>
""" + ex('<form style="inline-size:100%;max-inline-size:420px">\n  <div class="field">\n    <label class="label" for="fv1">Email</label>\n    <input class="input" id="fv1" type="email" required placeholder="you@example.com">\n    <span class="help">We never share it.</span>\n    <span class="error-text">Please enter a valid email address.</span>\n  </div>\n  <div class="field">\n    <label class="label" for="fv2">Password</label>\n    <input class="input" id="fv2" type="password" required minlength="8" placeholder="At least 8 characters">\n    <span class="help">Minimum 8 characters.</span>\n    <span class="error-text">Password is too short.</span>\n  </div>\n  <button class="btn btn-primary" type="submit">Create account</button>\n</form>',
'<div class="field">\n  <label class="label" for="email">Email</label>\n  <input class="input" id="email" type="email" required>\n  <span class="help">We never share it.</span>\n  <span class="error-text">Please enter a valid email address.</span>\n</div>') + """
<h3>2. Manual hook</h3>
<p>When validating in JS (e.g. server response), toggle <code>.is-invalid</code> / <code>.is-valid</code> on the control, or <code>.is-invalid</code> on the <code>.field</code> to force the error text open.</p>
<pre><code>// after a failed server check
field.classList.add("is-invalid");      // shows .error-text
input.classList.add("is-invalid");      // red border + focus ring
// on success
input.classList.replace("is-invalid", "is-valid");</code></pre>
""" + ex('<div class="field is-invalid" style="inline-size:100%;max-inline-size:420px">\n  <label class="label" for="fv3">Coupon code</label>\n  <input class="input is-invalid" id="fv3" value="EXPIRED2023">\n  <span class="help">Enter a promo code.</span>\n  <span class="error-text">This coupon has expired.</span>\n</div>',
'<div class="field is-invalid">\n  <input class="input is-invalid" value="EXPIRED2023">\n  <span class="error-text">This coupon has expired.</span>\n</div>') + """

<h2>Form layout</h2>
<p>Compose multi-column forms with the grid utilities — no special form-grid classes needed.</p>
""" + ex('<form class="grid grid-cols-1 md:grid-cols-2 gap-4" style="inline-size:100%">\n  <div class="field"><label class="label" for="fl1">First name</label><input class="input" id="fl1"></div>\n  <div class="field"><label class="label" for="fl2">Last name</label><input class="input" id="fl2"></div>\n  <div class="field col-span-full"><label class="label" for="fl3">Address</label><input class="input" id="fl3"></div>\n  <div class="field"><label class="label" for="fl4">City</label><input class="input" id="fl4"></div>\n  <div class="field"><label class="label" for="fl5">Postal code</label><input class="input" id="fl5"></div>\n</form>',
'<form class="grid grid-cols-1 md:grid-cols-2 gap-4">\n  <div class="field">…first name…</div>\n  <div class="field">…last name…</div>\n  <div class="field col-span-full">…address…</div>\n</form>') + """

<h2>Accessibility notes</h2>
<p>Always pair a <code>&lt;label for&gt;</code> with each control (or wrap the control in the label). Inputs show a visible <code>:focus-visible</code> ring derived from <code>--lc-ring</code>. For custom error messaging, link the message with <code>aria-describedby</code> and set <code>aria-invalid="true"</code> when you toggle the manual hook.</p>
"""

# ---------------------------------------------------------------- MIGRATION
migration = """
<h1>Migration from Bootstrap</h1>
<p class="lead">LombokCSS covers the same component surface as Bootstrap, so most migrations are a class rename plus dropping the Sass/JS bundle. This page maps the concepts and the classes.</p>

<h2>Mental model differences</h2>
<p>Three things change how you think:</p>
<ul>
  <li><strong>Theming is runtime, not build-time.</strong> Bootstrap recompiles Sass variables; LombokCSS reads CSS custom properties, and a whole look is one <code>data-style</code> attribute — no build step to re-theme.</li>
  <li><strong>Utilities are first-class.</strong> Like Bootstrap 5 utilities, but you can also drop into a Tailwind-ish flow (<code>flex items-center gap-4</code>) without leaving the framework.</li>
  <li><strong>Less JavaScript.</strong> Accordions and modals are native (<code>&lt;details&gt;</code>, <code>&lt;dialog&gt;</code>); the optional 2&nbsp;KB script only wires dropdowns, tabs, toasts, carousels, drawers and table sort.</li>
</ul>

<h2>Class map</h2>
<div class="table-wrap">
<table class="table table-striped">
  <thead><tr><th>Bootstrap</th><th>LombokCSS</th><th>Notes</th></tr></thead>
  <tbody>
    <tr><td><code>btn btn-primary</code></td><td><code>btn btn-primary</code></td><td>Same. Variants: <code>btn-secondary/outline/soft/ghost/link/danger</code>.</td></tr>
    <tr><td><code>btn-lg / btn-sm</code></td><td><code>btn-lg / btn-sm</code></td><td>Same names.</td></tr>
    <tr><td><code>btn-group</code></td><td><code>btn-group</code></td><td>Same.</td></tr>
    <tr><td><code>card / card-body / card-title</code></td><td><code>card / card-body / card-title</code></td><td>Same; also <code>card-header/footer/text</code>.</td></tr>
    <tr><td><code>badge bg-primary</code></td><td><code>badge badge-primary</code></td><td>Pill: <code>badge-pill</code>.</td></tr>
    <tr><td><code>alert alert-success</code></td><td><code>alert alert-success</code></td><td>Same.</td></tr>
    <tr><td><code>form-control</code></td><td><code>input</code> / <code>textarea</code></td><td>Or go classless — bare inputs are styled.</td></tr>
    <tr><td><code>form-select</code></td><td><code>select</code></td><td>Same idea.</td></tr>
    <tr><td><code>form-check / form-check-input</code></td><td><code>check</code> + native input</td><td>Themed via <code>accent-color</code>.</td></tr>
    <tr><td><code>form-switch</code></td><td><code>switch</code></td><td>Markup differs slightly (see Forms).</td></tr>
    <tr><td><code>is-invalid / invalid-feedback</code></td><td><code>is-invalid / error-text</code></td><td>Plus native <code>:user-invalid</code> with zero JS.</td></tr>
    <tr><td><code>input-group / input-group-text</code></td><td><code>input-group / input-addon</code></td><td>Same concept.</td></tr>
    <tr><td><code>navbar / navbar-nav / nav-link</code></td><td><code>navbar / navbar-nav</code> + <code>a</code></td><td>Mobile toggle: <code>navbar-toggle</code>.</td></tr>
    <tr><td><code>nav nav-tabs</code></td><td><code>tabs</code></td><td>Use ARIA <code>role="tab"</code>.</td></tr>
    <tr><td><code>accordion</code></td><td><code>accordion</code> + <code>&lt;details&gt;</code></td><td>Native, no JS.</td></tr>
    <tr><td><code>dropdown / dropdown-menu / dropdown-item</code></td><td><code>dropdown / dropdown-menu / dropdown-item</code></td><td>Toggle via <code>data-dropdown-toggle</code>.</td></tr>
    <tr><td><code>modal</code> (+ JS)</td><td><code>dialog.modal</code> + <code>modal-card</code></td><td>Native <code>&lt;dialog&gt;</code>; open with <code>data-modal-open</code>.</td></tr>
    <tr><td><code>toast</code></td><td><code>Lombok.toast()</code></td><td>JS helper creates the region.</td></tr>
    <tr><td><code>offcanvas</code></td><td><code>drawer</code> + <code>drawer-overlay</code></td><td><code>data-drawer-open</code>.</td></tr>
    <tr><td><code>breadcrumb / pagination</code></td><td><code>breadcrumb / pagination</code></td><td>Same.</td></tr>
    <tr><td><code>list-group / list-group-item</code></td><td><code>list-group / list-group-item</code></td><td>Same.</td></tr>
    <tr><td><code>progress / progress-bar</code></td><td><code>progress &gt; .bar</code></td><td>Width via inline <code>inline-size</code>.</td></tr>
    <tr><td><code>spinner-border</code></td><td><code>spinner</code></td><td>Same idea.</td></tr>
  </tbody>
</table>
</div>

<h2>Grid &amp; layout</h2>
<p>Replace the 12-column row/col grid with CSS grid utilities (or flex). It is terser and needs no <code>.row</code> wrapper.</p>
""" + ex('<div class="grid grid-cols-1 md:grid-cols-3 gap-3" style="inline-size:100%">\n  <div class="card"><div class="card-body" style="padding:12px">col</div></div>\n  <div class="card"><div class="card-body" style="padding:12px">col</div></div>\n  <div class="card"><div class="card-body" style="padding:12px">col</div></div>\n</div>',
'<!-- Bootstrap -->\n<div class="row">\n  <div class="col-md-4">…</div>\n  <div class="col-md-4">…</div>\n  <div class="col-md-4">…</div>\n</div>\n\n<!-- LombokCSS -->\n<div class="grid grid-cols-1 md:grid-cols-3 gap-3">\n  <div>…</div><div>…</div><div>…</div>\n</div>') + """

<h2>Theming</h2>
<p>Drop the Sass pipeline. Override CSS variables instead, and pick a look with <code>data-style</code>.</p>
<pre><code>// Bootstrap (build-time Sass)
$primary: #e11d48;
@import "bootstrap";

/* LombokCSS (runtime CSS variables) */
:root { --lc-accent:#e11d48; --lc-radius:4px; }
&lt;html data-style="resonant-stark" data-theme="dark"&gt;</code></pre>

<h2>JavaScript</h2>
<p>Bootstrap's <code>data-bs-*</code> attributes and JS plugins become small <code>data-*</code> hooks (or native elements):</p>
<pre><code>&lt;!-- Bootstrap --&gt;
&lt;button data-bs-toggle="modal" data-bs-target="#m"&gt;Open&lt;/button&gt;

&lt;!-- LombokCSS --&gt;
&lt;button data-modal-open="m"&gt;Open&lt;/button&gt;
&lt;dialog class="modal" id="m"&gt;…&lt;/dialog&gt;</code></pre>

<h2>Step-by-step</h2>
<ol>
  <li>Swap the stylesheet/script links for <code>lombok.min.css</code> (+ optional <code>lombok.js</code>).</li>
  <li>Rename component classes using the table above (most are identical).</li>
  <li>Replace <code>.row/.col-*</code> with <code>grid grid-cols-* / col-span-*</code> or flex utilities.</li>
  <li>Convert <code>data-bs-*</code> triggers to the <code>data-*</code> hooks (modal, dropdown, drawer) or native elements.</li>
  <li>Move Sass variable overrides to CSS custom properties on <code>:root</code>; choose a <code>data-style</code>.</li>
  <li>Delete the Bootstrap + Popper bundles.</li>
</ol>

<h2>Gotchas</h2>
<ul>
  <li><strong>No jQuery/Popper.</strong> Tooltips/popovers are CSS/JS-light; positioning is simpler and may need tweaks for edge cases.</li>
  <li><strong>Utilities aren't 1:1.</strong> LombokCSS ships a focused utility set; check the Utilities page for exact names (e.g. spacing uses a token scale).</li>
  <li><strong>Logical properties.</strong> If you had LTR-only overrides using <code>left/right</code>, switch to <code>inline-start/inline-end</code> to keep RTL working.</li>
  <li><strong>Color modes.</strong> Dark mode is <code>data-theme</code> (or OS), not a separate stylesheet.</li>
</ul>
"""

# ---------------------------------------------------------------- UTILITIES
utilities = """
<h1>Utilities</h1>
<p class="lead">Atomic helpers for fine-tuning without writing CSS. All use logical properties, so they are RTL-safe.</p>

<h2>Layout</h2>
<pre><code>.flex .inline-flex .grid .inline-grid .block .inline-block .hidden
.flex-row .flex-col .flex-wrap .flex-1 .flex-none
.items-{start|center|end|stretch|baseline}
.justify-{start|center|end|between|around|evenly}
.grid-cols-{1..6,12}  .col-span-{1..12,full}</code></pre>
""" + ex('<div class="grid grid-cols-3 gap-2" style="inline-size:100%">\n  <div class="card"><div class="card-body" style="padding:12px">1</div></div>\n  <div class="card"><div class="card-body" style="padding:12px">2</div></div>\n  <div class="card"><div class="card-body" style="padding:12px">3</div></div>\n</div>') + """

<h2>Spacing</h2>
<pre><code>.p-{0..8}  .px-* .py-* .pt-4 .pb-4
.m-{0,1,2,4} .m-auto .mx-auto .my-* .mt-* .mb-* .ms-auto .me-auto
.gap-{0..6,8,10,12}  .gap-x-* .gap-y-*</code></pre>

<h2>Sizing</h2>
<pre><code>.w-full .w-auto .w-fit .w-screen
.h-full .h-screen .min-h-screen
.max-w-{xs|sm|md|lg|xl|2xl|7xl}</code></pre>

<h2>Typography</h2>
<pre><code>.text-{xs|sm|base|lg|xl|2xl|3xl}
.font-{light|normal|medium|semibold|bold}
.text-{start|center|end|justify}  .leading-* .tracking-*
.uppercase .capitalize .truncate .font-mono</code></pre>
""" + ex('<div style="inline-size:100%">\n  <p class="text-2xl font-bold mb-0">Display</p>\n  <p class="text-sm text-muted mb-0">Muted caption</p>\n  <p class="truncate" style="max-inline-size:220px">This very long line will be truncated with an ellipsis when it overflows its box.</p>\n</div>') + """

<h2>Colors</h2>
<pre><code>.text-{primary|muted|faint|success|warning|danger|info}
.bg-{bg|surface|surface-2|primary|soft}
.bg-{success|warning|danger|info}          /* solid */
.bg-{success|warning|danger|info}-soft     /* tinted */
.border .border-strong .border-{primary|success|warning|danger|info}</code></pre>
""" + ex('<span class="badge bg-success">bg-success</span>\n<span class="badge bg-warning">bg-warning</span>\n<span class="badge bg-danger">bg-danger</span>\n<span class="badge bg-info">bg-info</span>\n<span class="badge bg-success-soft">success-soft</span>\n<span class="badge bg-danger-soft">danger-soft</span>') + """

<h2>Radius, shadow &amp; effects</h2>
<pre><code>.rounded-{none|sm|md|lg|full}
.shadow-{none|sm|md|lg}  .backdrop-blur
.opacity-{50|75}  .transition</code></pre>
""" + ex('<div class="bg-surface border rounded-lg shadow p-4">rounded-lg + shadow</div>\n<div class="bg-surface border rounded-full p-4">rounded-full</div>') + """

<h2>Position &amp; misc</h2>
<pre><code>.relative .absolute .fixed .sticky  .inset-0 .top-0 .start-0 .end-0
.z-{10|20|30|50}  .overflow-{hidden|auto|x-auto}
.cursor-pointer .select-none .sr-only .aspect-square .aspect-video</code></pre>

<h2>Responsive prefixes</h2>
<p>Mobile-first breakpoints. Prefix any layout utility: <code>sm:</code> 640px, <code>md:</code> 768px, <code>lg:</code> 1024px, <code>xl:</code> 1280px.</p>
<pre><code>&lt;div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4"&gt; … &lt;/div&gt;</code></pre>
<p>Covered per breakpoint: display, flex direction/wrap, items/justify, <code>grid-cols-1..6,12</code>, <code>col-span-1..6,full</code>, <code>gap-*</code>, and text alignment. Resize the window to see it react:</p>
""" + ex('<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-2" style="inline-size:100%">\n  <div class="card"><div class="card-body" style="padding:12px">A</div></div>\n  <div class="card"><div class="card-body" style="padding:12px">B</div></div>\n  <div class="card"><div class="card-body" style="padding:12px">C</div></div>\n  <div class="card"><div class="card-body" style="padding:12px">D</div></div>\n</div>')

accessibility = """
<h1>Accessibility</h1>
<p class="lead">Accessibility is built into the components, not bolted on. This page documents what LombokCSS handles for you and the small things you still own.</p>

<h2>Focus visibility</h2>
<p>Every interactive element shows a clear <code>:focus-visible</code> ring drawn from <code>--lc-ring</code>, so keyboard users always see where they are. The ring appears for keyboard/AT focus and stays out of the way for mouse clicks. Tab through the controls below:</p>
""" + ex('<button class="btn btn-primary">Button</button>\n<a href="#" class="btn btn-outline">Link button</a>\n<input class="input" style="max-inline-size:220px" placeholder="Input">\n<select class="select" style="max-inline-size:160px"><option>Select</option></select>') + """
<p>The ring uses <code>:focus-visible</code> (not <code>:focus</code>), and honours a custom color per style — override <code>--lc-ring</code> to match your brand.</p>

<h2>Keyboard &amp; native semantics</h2>
<p>Overlay and disclosure components lean on native elements so keyboard behaviour comes for free:</p>
<ul>
  <li><strong>Modal</strong> uses <code>&lt;dialog&gt;</code> — <kbd>Esc</kbd> closes it and focus is trapped by the browser.</li>
  <li><strong>Accordion</strong> uses <code>&lt;details&gt;/&lt;summary&gt;</code> — toggled with <kbd>Enter</kbd>/<kbd>Space</kbd>, no JS required.</li>
  <li><strong>Dropdown</strong> closes on <kbd>Esc</kbd> and toggles <code>aria-expanded</code>.</li>
  <li><strong>Tabs</strong> expect <code>role="tablist"/"tab"/"tabpanel"</code> and manage <code>aria-selected</code> + panel visibility.</li>
  <li><strong>Sortable tables</strong> reflect state in <code>aria-sort</code> on the header cells.</li>
</ul>

<h2>Reduced motion</h2>
<p>All transitions and animations (spinners, toasts, carousels, skeletons) are wrapped in <code>@media (prefers-reduced-motion: reduce)</code>. If a visitor asks their OS to reduce motion, LombokCSS stops animating automatically — you don't need to do anything.</p>
<pre><code>@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: .001ms !important; transition-duration: .001ms !important; }
}</code></pre>

<h2>Colour &amp; contrast</h2>
<p>Component colours are driven by semantic tokens, and every built-in style — including dark mode and the intrinsically dark <code>resonant-stark</code> — ships status colours (<code>--lc-success</code>, <code>--lc-danger</code>, …) with matching readable text and soft backgrounds, so alerts, badges and soft buttons meet WCAG AA contrast in both light and dark. When you author a custom style, keep the same discipline: dark styles must override the status <code>*-soft</code> and <code>*-text</code> tokens.</p>

<h2>Transparency fallback</h2>
<p>The <code>glassmorphism</code> style uses <code>backdrop-filter</code> guarded by <code>@supports</code>: browsers without it get an opaque, fully legible surface instead of an unreadable blur.</p>

<h2>RTL &amp; internationalisation</h2>
<p>Layout is written with logical properties (<code>margin-inline</code>, <code>inset-inline-start</code>, <code>border-start-start-radius</code>), so setting <code>dir="rtl"</code> mirrors everything correctly — including component internals like dropdown alignment and the drawer slide direction. No separate RTL stylesheet needed.</p>

<h2>Classless &amp; semantic HTML</h2>
<p>Plain, well-structured HTML is styled out of the box, which nudges you toward semantic markup (real <code>&lt;button&gt;</code>, <code>&lt;nav&gt;</code>, <code>&lt;table&gt;</code>, headings) — the foundation of an accessible page.</p>

<h2>What you still own</h2>
<p>LombokCSS handles presentation; you provide meaning:</p>
<ul>
  <li>Give every form control a <code>&lt;label&gt;</code> (or <code>aria-label</code>), and link help/error text with <code>aria-describedby</code>.</li>
  <li>Add <code>alt</code> text to images and accessible names to icon-only buttons (<code>aria-label</code>).</li>
  <li>Set <code>aria-current</code> on the active nav/pagination item, and provide <code>aria-live</code> for toasts if you need announcements.</li>
  <li>Preserve a logical heading order and don't rely on colour alone to convey status — pair it with text or an icon.</li>
  <li>Test with a keyboard and a screen reader; the components give you the hooks, your content gives them meaning.</li>
</ul>
"""

utilities += """
<h2>Printing</h2>
<p>A built-in print stylesheet makes any page print (or export to PDF) cleanly: components switch to a high-contrast, ink-friendly palette — white background, black text, no shadows, blur or gradients — regardless of the active <code>data-style</code> or dark mode, and purely interactive chrome (dropdown menus, toasts, spinners, drawers) is hidden. Two helpers give you control:</p>
<ul>
  <li><code>.no-print</code> — hide an element only when printing.</li>
  <li><code>.print-only</code> — show an element only when printing.</li>
</ul>
<p>External link targets are appended in parentheses so URLs survive on paper. Try your browser&#39;s print preview on any page.</p>
"""

CONTENT = {
    "index.html": ("Overview", overview),
    "getting-started.html": ("Getting started", getting),
    "migration.html": ("Migration from Bootstrap", migration),
    "theming.html": ("Theming & styles", theming),
    "components.html": ("Components", components),
    "forms.html": ("Forms", forms),
    "utilities.html": ("Utilities", utilities),
    "accessibility.html": ("Accessibility", accessibility),
}

import os, shutil

os.makedirs("docs/assets", exist_ok=True)

for fname, (title, content) in CONTENT.items():
    open("docs/" + fname, "w").write(shell(fname, title, content))
    print("wrote docs/" + fname)

# Copy the built framework assets so docs/ is self-contained (Pages + local).
# docs.css / docs.js are hand-authored assets that already live in docs/assets/.
for src in ("dist/lombok.min.css", "dist/lombok.js"):
    if os.path.exists(src):
        shutil.copy(src, "docs/assets/" + os.path.basename(src))
        print("copied " + src + " -> docs/assets/")
    else:
        print("WARNING: %s missing — run `npm run build` first" % src)
