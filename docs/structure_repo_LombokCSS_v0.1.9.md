# Structure Repo — LombokCSS v0.1.9

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

```text
LombokCSS/
├── README.md · CHANGELOG.md · LICENSE (MIT) · SECURITY.md · SUPPORT.md
├── CONTRIBUTING.md · CODE_OF_CONDUCT.md · GITHUB_SETUP.md · CLAUDE.md (memori sesi)
├── package.json · package-lock.json · composer.json · bower.json
├── lombokcss.gemspec · lib/lombokcss(.rb, /version.rb)      # RubyGem
├── release-please-config.json · .release-please-manifest.json
├── playwright.config.js · build_docs.py (generator situs docs/)
├── src/          variables · core · themes · components · utilities · print (.css) · lombok.js
├── dist/         lombok.css · lombok.min.css · lombok.js (hasil build, di-commit)
├── scripts/      build-css.mjs · size-check.mjs · ssr-check.mjs
├── tests/        behavior.spec.js · visual.spec.js · visual.spec.js-snapshots/
├── docs/         situs GitHub Pages (*.html, assets/) + 12 dokumen standar *_LombokCSS_v0.1.9.md
├── examples/     demo.html
├── package/      salinan lama paket (tidak dipublikasikan; temuan C-03)
└── .github/      workflows/ · linters/ · ISSUE_TEMPLATE/ · dependabot.yml · CODEOWNERS
```

Catatan: `demo.html` di root adalah halaman demo mandiri; `docs/assets/lombok.js` dan
`docs/assets/lombok.min.css` disinkronkan dari `dist/` oleh `npm run build:docs`.
