# Full Summary Project — LombokCSS v0.1.9

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

## 1. Ringkasan

LombokCSS menggabungkan pendekatan komponen (seperti Bootstrap) dengan theming berbasis
token (seperti design system) dalam paket kecil (seperti Pico). Satu atribut mengganti
identitas visual seluruh halaman tanpa menyentuh HTML.

| Metrik | Nilai |
| --- | --- |
| Versi | 0.1.9 |
| CSS min + gzip | ~9,7 KB (anggaran 15 KB) |
| JS gzip | ~3,1 KB (anggaran 4 KB) |
| Dependensi runtime | 0 |
| Gaya desain | 5 |
| Test perilaku | 44 (Playwright) |
| Skor universalitas | 6/9 |

## 2. Fitur

Komponen: accordion, alert, avatar, badge, breadcrumb, button (+group), card, carousel,
checkbox/switch, drawer/offcanvas, dropdown, field/input/select/textarea/file, input-group,
list-group, modal (`<dialog>`), navbar, pagination, popover, progress, sidebar, skeleton,
spinner, stat, steps, table (striped/hover/bordered/sortable), tabs, timeline, toast.
Ditambah utilitas, mode classless, lapisan cetak, mode gelap, RTL.

## 3. Tabel gap vs pembanding

| Kemampuan | LombokCSS | Bootstrap 5 | Pico | Bulma | DaisyUI |
| --- | --- | --- | --- | --- | --- |
| Ganti identitas visual tanpa ubah HTML | ✅ 5 gaya | ❌ | ❌ | ❌ | ✅ (butuh Tailwind build) |
| Mode gelap | ✅ | ✅ | ✅ | ✅ | ✅ |
| RTL tanpa build terpisah | ✅ logical props | ❌ (CSS RTL terpisah) | ✅ | ❌ | ✅ |
| Tanpa build step | ✅ | ✅ | ✅ | ✅ | ❌ |
| Ukuran gzip | ~10 KB | ~25 KB + JS | ~10 KB | ~25 KB | tergantung |
| Tooltip JS | ❌ (popover saja) | ✅ | ❌ | ❌ | ✅ CSS |
| Scrollspy | ❌ | ✅ | ❌ | ❌ | ❌ |
| Validasi form JS | ❌ (state CSS saja) | ✅ | ❌ | ❌ | ❌ |
| Sortir tabel sadar-bahasa | ✅ | ❌ | ❌ | ❌ | ❌ |
| Lapisan cetak | ✅ | sebagian | ❌ | ❌ | ❌ |

## 4. Status

🟢 LIVE di npm dan GitHub Packages; kepatuhan MASTERPLAN_UTAMA v3.4 diselaraskan pada
branch ini. Temuan terbuka: lihat [Masterplan](masterplan_LombokCSS_v0.1.9.md) §5.
