# How to Dist — LombokCSS v0.1.9

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

## 1. Alur rilis

```text
commit Conventional (fix:/feat:) → push main → release-please membuka PR rilis
  → merge → GitHub Release + tag lombokcss-vX.Y.Z
  → npm-publish.yml        → npmjs.org (jsDelivr/unpkg otomatis)
  → publish-packages.yml   → GitHub Packages: npm, RubyGems, NuGet, Maven, Container
  → pages.yml              → situs docs (build + build:docs)
```

Panduan langkah demi langkah (secret, branch protection, Pages): [`GITHUB_SETUP.md`](../GITHUB_SETUP.md).

## 2. Pemeriksaan sebelum rilis

```bash
npm ci
npm run build          # dist/ dari src/
npm test               # anggaran ukuran + SSR guard
npm run test:behavior  # 44 test perilaku
npm run test:visual    # baseline visual (container Playwright v1.56.0-noble)
npm run lint           # Prettier
```

## 3. Versi

Versi tunggal di `package.json`, `composer.json`, `lib/lombokcss/version.rb` dan
`.release-please-manifest.json` — dinaikkan oleh release-please.
Saat versi minor naik, rename manual `docs/*_LombokCSS_v<ver>.md` (temuan C-06).

## 4. Deskripsi registry (ADR-019)

Semua field deskripsi menyebut fungsi universal + "Part of Lombok Ecosystem" dan tidak
boleh menyebut aplikasi/framework sebagai pemilik.
