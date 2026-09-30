# Guide How to Use — LombokCSS v0.1.9

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

## 1. Pasang

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/lombokcss@0.1.9/dist/lombok.min.css" />
<script defer src="https://cdn.jsdelivr.net/npm/lombokcss@0.1.9/dist/lombok.js"></script>
```

```bash
npm install lombokcss            # atau: composer require codinglombok/lombokcss
```

```js
import "lombokcss/css";
import "lombokcss"; // opsional, komponen interaktif
```

## 2. Pilih gaya, tema, arah

```html
<html lang="ar" dir="rtl" data-style="neo-brutalism" data-theme="dark">
```

| Atribut | Nilai |
| --- | --- |
| `data-style` | `modern-corporate-flat` (default) · `resonant-stark` · `neo-brutalism` · `semantic-minimalist` · `glassmorphism` |
| `data-theme` | `light` · `dark` (tanpa atribut: ikuti `prefers-color-scheme`) |
| `dir` | `ltr` · `rtl` |
| `lang` | Tag BCP 47; dipakai sortir tabel untuk urutan alfabet bahasa tersebut |

## 3. Komponen dasar

```html
<button class="btn btn-primary">Simpan</button>
<div class="alert alert-success">Tersimpan.</div>
<div class="card"><div class="card-body"><h3 class="card-title">Judul</h3></div></div>
```

## 4. Rebrand dengan token

```css
:root { --lc-accent: #0f766e; --lc-radius: 0.25rem; --lc-font-sans: "Inter", system-ui; }
```

## 5. Komponen interaktif (butuh `lombok.js`)

```html
<button data-modal-open="dlg">Buka</button>
<dialog id="dlg"><button data-modal-close>Tutup</button></dialog>

<table class="table" lang="sv">
  <thead><tr><th aria-sort="none">Nama</th></tr></thead>
  <tbody><tr><td>Äpple</td></tr><tr><td>Zebra</td></tr></tbody>
</table>
```

```js
Lombok.toast("Tersimpan", { variant: "success", timeout: 3000 });
```

Dokumentasi lengkap: <https://codinglombok.github.io/LombokCSS/>.
