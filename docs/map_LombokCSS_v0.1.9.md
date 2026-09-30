# Map — LombokCSS v0.1.9

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

## 1. Posisi di peta ekosistem

```text
A  Aplikasi      ── boleh menyatakan "menggunakan LombokCSS"
P  Framework     ── boleh menyatakan "menggunakan LombokCSS"
L1 LombokUI      ── dependensi wajib: LombokCSS, LombokIcons, LombokAnimate
══ BATAS KLAIM (ADR-019) ══
L0 LombokCSS     ── tanpa dependensi; tidak mengaku milik entitas di atasnya
```

## 2. Dependensi

| Jenis | Daftar |
| --- | --- |
| Wajib (runtime) | — (nol) |
| Opsional (runtime) | — |
| Dev | `lightningcss`, `prettier`, `@playwright/test` |
| Peer yang bekerja berdampingan | LombokIcons, LombokAnimate, LombokCharts, LombokTableSheet (tanpa integrasi kode) |

## 3. Contoh dependen (bukan pemilik)

| Repo | Tingkat | Hubungan |
| --- | --- | --- |
| LombokUI | L1 | Katalog v3.4 mencantumkan LombokCSS sebagai dependensi wajib |

## 4. Peta distribusi

| Kanal | Nama |
| --- | --- |
| npm | `lombokcss` |
| CDN | jsDelivr / unpkg `lombokcss` |
| Packagist | `codinglombok/lombokcss` |
| RubyGems (GPR) | `lombokcss` |
| Bower | `lombokcss` |
| NuGet (GPR) | `codinglombok.LombokCSS` |
| Maven (GPR) | `com.github.codinglombok:lombokcss` |
| Container (GHCR) | `ghcr.io/codinglombok/lombokcss` |
| SourceForge | mirror `lombokcss` |

## 5. Peta platform

Browser desktop/mobile evergreen · WebView iOS/Android · Electron/Tauri · SSR (Node) · panel web perangkat embedded (kiosk, router, gateway IoT).
