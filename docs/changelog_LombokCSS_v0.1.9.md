# Changelog — LombokCSS v0.1.9

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

Catatan rilis resmi yang ditulis release-please ada di [`CHANGELOG.md`](../CHANGELOG.md).
Dokumen ini mencatat perubahan terkait masterplan, entri terbaru di depan.

## Belum dirilis — penyelarasan MASTERPLAN_UTAMA v3.4

- `docs/`: 12 dokumen standar `*_LombokCSS_v0.1.9.md` (§5.1) dengan checklist universalitas D1–D9, skor 6/9 (§5.2).
- README: bagian "Why this library? (Mengapa library ini?)", "Standards implemented", label ekosistem sebagai peer (ADR-019).
- Manifest (`package.json`, `composer.json`, `bower.json`, `lombokcss.gemspec`, NuGet/Maven di `publish-packages.yml`): "Part of Lombok Ecosystem".
- `lombok.js`: sortir tabel memakai `Intl.Collator` dari atribut `lang` terdekat (BCP 47), `numeric: true`, fallback aman; +2 test perilaku.

## 0.1.9 — 2026-08-24

- Sinkronisasi pipeline publish semua registry GitHub Packages.
