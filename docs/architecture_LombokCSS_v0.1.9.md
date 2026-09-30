# Architecture — LombokCSS v0.1.9

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

## 1. Prinsip

- **Token dulu:** komponen hanya membaca token semantik (`--lc-surface`, `--lc-text`, `--lc-accent`, …). Gaya desain = kumpulan nilai token.
- **Tiga sumbu independen:** `data-style` (identitas), `data-theme` (terang/gelap), `dir` (LTR/RTL). Semua kombinasi valid.
- **Zero dependency runtime** (Prinsip #7); JS opsional dan degradasi mulus.
- **Dependensi searah & tanpa klaim** (Prinsip #9, #11): L0, tidak bergantung pada library, framework, maupun aplikasi apa pun.

## 2. Lapisan sumber

Urutan konkatenasi di `scripts/build-css.mjs` (urutan = kaskade):

| # | Berkas | Isi |
| --- | --- | --- |
| 1 | `src/variables.css` | Token primitif & semantik, default terang, `prefers-color-scheme` |
| 2 | `src/core.css` | Reset, tipografi classless, fokus, `prefers-reduced-motion` |
| 3 | `src/themes.css` | Lima gaya desain + override gelap per gaya |
| 4 | `src/components.css` | Komponen (hanya membaca token) |
| 5 | `src/utilities.css` | Kelas utilitas |
| 6 | `src/print.css` | Lapisan cetak |

`dist/lombok.css` = konkatenasi; `dist/lombok.min.css` = minifikasi `lightningcss` (Node API).
`src/lombok.js` disalin apa adanya ke `dist/lombok.js`.

## 3. JavaScript opsional

IIFE tanpa dependensi; keluar lebih awal bila `document` tidak ada (aman untuk SSR).
Dua pola wiring:

- **Delegasi di `document`** (bekerja untuk markup yang ditambahkan kemudian): dropdown, modal, drawer, popover, navbar.
- **Sekali saat parse** (`querySelectorAll`): tabs, carousel, sortir tabel, backdrop dialog.

API global satu-satunya: `window.Lombok.toast()`.

## 4. Anggaran & kualitas

| Gerbang | Alat | Batas |
| --- | --- | --- |
| Ukuran | `scripts/size-check.mjs` | CSS ≤ 15 KB gzip, JS ≤ 4 KB gzip |
| SSR | `scripts/ssr-check.mjs` | Impor tanpa DOM tidak melempar |
| Perilaku | `tests/behavior.spec.js` (Playwright) | 44 test |
| Visual | `tests/visual.spec.js` | Baseline per gaya × tema |
| Lint | Super-Linter, Prettier | CSS, JS, JSON, YAML, Markdown |

## 5. Keputusan arsitektur yang relevan

| ADR | Dampak pada LombokCSS |
| --- | --- |
| ADR-015 | Perilaku JS dinormatifkan di [SPEC](SPEC_LombokCSS_v0.1.9.md) dan diuji `behavior.spec.js` |
| ADR-019 | README/manifest tanpa klaim kepemilikan aplikasi; checklist D1–D9 di masterplan |
