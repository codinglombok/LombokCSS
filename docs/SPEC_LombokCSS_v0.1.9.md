# Behavioral Specification — LombokCSS v0.1.9

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

Kontrak normatif perilaku `dist/lombok.js` (ADR-015). Kata **HARUS/TIDAK BOLEH** bersifat
normatif. Setiap butir diuji di `tests/behavior.spec.js` (kolom Test = blok `describe`).

| ID | Aturan | Test |
| --- | --- | --- |
| S-01 | Mengimpor skrip tanpa `document` (SSR) TIDAK BOLEH melempar dan TIDAK BOLEH menyentuh API browser | `scripts/ssr-check.mjs` |
| S-02 | Skrip TIDAK BOLEH melakukan permintaan jaringan atau memakai storage | tinjauan kode |
| S-03 | Dropdown: klik `[data-dropdown-toggle]` HARUS men-toggle `.is-open` pada `.dropdown` terdekat dan menyetel `aria-expanded`; klik di luar dan `Escape` HARUS menutup | dropdown |
| S-04 | Tabs: klik tab HARUS menyetel `aria-selected="true"` padanya, `"false"` pada lainnya, dan hanya panel `aria-controls`-nya yang tidak `hidden` | tabs |
| S-05 | Modal: `[data-modal-open=id]` HARUS memanggil `showModal()` pada `<dialog id>`; `[data-modal-close]` dan klik backdrop HARUS menutup | modal |
| S-06 | Drawer, popover, navbar: toggle `.is-open` pada kontainer terdekat; popover HARUS tertutup oleh `Escape` | drawer / popover / navbar |
| S-07 | Carousel HARUS bergerak ke indeks slide target (bukan delta), dibatasi [0, n−1], dan membalik arah bila `dir="rtl"` | carousel |
| S-08 | Sortir tabel: klik `th[aria-sort]` HARUS mengurutkan `tBodies[0]` naik, klik kedua turun; `th` lain direset ke `none`; sel satu baris tetap bersama | table sort |
| S-09 | Sortir tabel: bila kedua nilai numerik HARUS dibandingkan sebagai angka; selain itu HARUS memakai `Intl.Collator` untuk `lang` terdekat dengan `numeric: true` | table sort |
| S-10 | Tag `lang` tidak valid TIDAK BOLEH melempar; HARUS jatuh ke collation default | table sort |
| S-11 | `Lombok.toast(msg, opts)` HARUS membuat `.toast-region[aria-live=polite]` bila belum ada, menambah elemen `role=status` berisi `msg` sebagai teks (bukan HTML), dan menghapusnya setelah `opts.timeout` (default 3500 ms) | toast |
| S-12 | Tidak ada exception tak tertangkap selama interaksi mana pun | `afterEach` global |
