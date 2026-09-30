# Development Ide / Arah Pengembangan — LombokCSS v0.1.9

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

## 1. Lingkungan

- Node ≥ 18, npm; Python 3 untuk `build_docs.py`.
- Editor: `.editorconfig` + Prettier (`npm run format`).
- Chromium Playwright untuk test (`npx playwright test`).

## 2. Konvensi

- Komponen **hanya** membaca token semantik `--lc-*`; nilai mentah hanya di `variables.css`/`themes.css`.
- Pakai logical properties (`margin-inline-start`, bukan `margin-left`) agar RTL gratis.
- Gaya gelap wajib meng-override token status `*-soft` dan `*-text`.
- Perilaku JS baru wajib: tercatat di [SPEC](SPEC_LombokCSS_v0.1.9.md), punya test di `behavior.spec.js`, muat anggaran 4 KB.
- Commit: Conventional Commits.

## 3. Arah pengembangan

| Arah | Alasan (dimensi) |
| --- | --- |
| SBOM + provenance npm di rilis | D5, Prinsip #8 |
| Paket token W3C Design Tokens (JSON) | D3/D4 — alat desain & library lain (mis. LombokCharts) dapat membaca token yang sama |
| Tooltip, validasi form opsional | D8 — menutup gap vs Bootstrap |
| Gaya ke-6 bertema aksesibilitas kontras tinggi (`forced-colors`) | D9 |
| Hapus folder `package/` | Kebersihan repo (C-03) |
