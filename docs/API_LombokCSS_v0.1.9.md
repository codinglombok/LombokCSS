# API Reference — LombokCSS v0.1.9

| Atribut | Nilai |
| --- | --- |
| Repo | [codinglombok/LombokCSS](https://github.com/codinglombok/LombokCSS) |
| Versi library | 0.1.9 |
| Tingkat / cluster | L0 · 01 Frontend, UI & Visualisasi Data (katalog 01.01) |
| Acuan | MASTERPLAN_UTAMA v3.4 (2026-09-29) · ARCHITECTURE_UTAMA v3.4 · ADR-019 |
| Tanggal dokumen | 2026-09-30 |
| Lisensi | MIT (kebijakan §10: framework CSS) |

Dokumen standar: [Masterplan](masterplan_LombokCSS_v0.1.9.md) · [Architecture](architecture_LombokCSS_v0.1.9.md) · [Changelog](changelog_LombokCSS_v0.1.9.md) · [Map](map_LombokCSS_v0.1.9.md) · [Structure Repo](structure_repo_LombokCSS_v0.1.9.md) · [Full Summary Project](full_summary_project_LombokCSS_v0.1.9.md) · [Guide How to Use](guide_how_to_use_LombokCSS_v0.1.9.md) · [How to Dist](how_to_dist_LombokCSS_v0.1.9.md) · [Development Ide](development_ide_LombokCSS_v0.1.9.md) · [API Reference](API_LombokCSS_v0.1.9.md) · [Bahasa (i18n)](Lang_LombokCSS_v0.1.9.md) · [Behavioral Specification](SPEC_LombokCSS_v0.1.9.md)

---

## 1. Atribut global

| Atribut | Elemen | Nilai |
| --- | --- | --- |
| `data-style` | `<html>` atau kontainer | `modern-corporate-flat` · `resonant-stark` · `neo-brutalism` · `semantic-minimalist` · `glassmorphism` |
| `data-theme` | `<html>` atau kontainer | `light` · `dark` |
| `dir` | `<html>` | `ltr` · `rtl` |
| `lang` | elemen mana pun | Tag BCP 47 (collation sortir tabel) |

## 2. Token (CSS custom properties)

| Kelompok | Token |
| --- | --- |
| Warna permukaan & teks | `--lc-bg` `--lc-surface` `--lc-surface-2` `--lc-text` `--lc-text-muted` `--lc-text-faint` `--lc-border` `--lc-border-strong` `--lc-border-width` |
| Aksen | `--lc-accent` `--lc-accent-hover` `--lc-accent-active` `--lc-accent-text` `--lc-accent-soft` `--lc-accent-soft-text` `--lc-ring` |
| Status | `--lc-{success,warning,danger,info}` + `-soft` + `-text` |
| Bentuk & efek | `--lc-radius-sm` `--lc-radius` `--lc-radius-lg` `--lc-radius-full` `--lc-shadow-sm` `--lc-shadow` `--lc-shadow-lg` `--lc-shadow-hard` `--lc-blur` `--lc-glass-tint` `--lc-glass-border` `--lc-transition` |
| Tipografi | `--lc-font-sans` `--lc-font-display` `--lc-font-mono` `--lc-text-{xs,sm,base,lg,xl,2xl,3xl,4xl}` `--lc-weight-{normal,medium,semibold,bold}` `--lc-leading-{tight,normal,relaxed}` `--lc-tracking` |
| Ruang & tata letak | `--lc-space-{0,1,2,3,4,5,6,8,10,12}` `--lc-container` `--lc-navbar-h` |
| Lapisan | `--lc-z-{base,dropdown,sticky,modal,toast,tooltip}` |

## 3. Kelas komponen

Lihat [Full Summary](full_summary_project_LombokCSS_v0.1.9.md) §2 dan situs docs
(`components.html`, `forms.html`, `utilities.html`). Status visual: `.is-open`, `.is-active`, `.is-valid`, `.is-invalid`.

## 4. JavaScript (`dist/lombok.js`)

| Hook | Perilaku |
| --- | --- |
| `[data-dropdown-toggle]` dalam `.dropdown` | Toggle `.is-open`, `aria-expanded`; Esc & klik luar menutup |
| `[role=tablist] [role=tab][aria-controls]` | `aria-selected`, panel `hidden` |
| `[data-modal-open="id"]` / `[data-modal-close]` | `showModal()` / `close()` pada `<dialog>`; klik backdrop menutup |
| `[data-drawer-open="id"]` / `[data-drawer-close]` | Drawer/offcanvas |
| `[data-popover-toggle]` dalam `.popover` | Toggle `.is-open`; Esc menutup |
| `.navbar-toggle` dalam `.navbar` | Toggle `.is-open` |
| `.carousel` (`.carousel-track`, `.carousel-prev/next`, `.carousel-dots`) | Geser per slide, sadar RTL |
| `table.table thead th[aria-sort]` | Sortir kolom: angka numerik, teks via `Intl.Collator(lang terdekat, {numeric:true})` |

```ts
Lombok.toast(msg: string, opts?: { variant?: "success"|"warning"|"danger"|"info"; timeout?: number /* ms, default 3500 */ }): HTMLElement
```

## 5. Ekspor paket npm

`lombokcss` → `dist/lombok.js` · `lombokcss/css` → `dist/lombok.min.css` · `lombokcss/css-full` → `dist/lombok.css` · `lombokcss/js` · `lombokcss/src/*`.
