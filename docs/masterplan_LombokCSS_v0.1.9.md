# Masterplan — LombokCSS v0.1.9

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

## 1. Identitas & posisi

**LombokCSS** adalah framework CSS komponen berbasis token yang universal: satu markup,
lima gaya desain (`modern-corporate-flat`, `resonant-stark`, `neo-brutalism`,
`semantic-minimalist`, `glassmorphism`), mode gelap dan RTL sebagai sumbu independen.
Ukuran ~9,7 KB gzip (CSS) + JS opsional ~3 KB gzip; nol dependensi runtime.

Posisi (netral-domain): lapisan presentasi untuk UI berbasis mesin browser apa pun.
LombokCSS adalah produk mandiri — **bukan komponen dari aplikasi atau framework mana pun**
(Prinsip #11, ADR-019). Aplikasi/framework yang memakainya dicatat hanya sebagai
*contoh pemakai* di [Map](map_LombokCSS_v0.1.9.md).

## 2. Skenario pemakaian (Prinsip #1)

| # | Skenario | Pemakai |
| --- | --- | --- |
| 1 | Situs landing/marketing & dokumentasi statis tanpa build step (CDN) | Indie developer, agensi |
| 2 | Dasbor SaaS / panel admin dengan rebrand via token dan mode gelap | Startup, tim produk |
| 3 | Formulir layanan publik bilingual, termasuk bahasa RTL (Arab) | E-government |
| 4 | Panel web perangkat (router, gateway IoT, kiosk/HMI) yang disajikan dari flash terbatas | Pembuat hardware |
| 5 | Aplikasi hibrid di WebView iOS/Android, Electron/Tauri | Tim mobile/desktop |
| 6 | Design system perusahaan: satu set komponen, beberapa merek (gaya kustom) | Enterprise |
| 7 | Dokumen cetak (invoice, laporan) lewat lapisan `print.css` | Semua |

## 3. Checklist Universalitas (ADR-019)

| Dimensi | Status | Keterangan |
| --- | --- | --- |
| D1 — Multi-kebutuhan | ✅ | 7 skenario di §2: landing, dasbor, e-gov RTL, panel perangkat, WebView, design system, cetak |
| D2 — Multi-platform | ✅ | Browser desktop & mobile evergreen, WebView iOS/Android, Electron/Tauri, SSR (Next/Nuxt/Astro/SvelteKit — impor aman tanpa DOM, diuji `scripts/ssr-check.mjs`), panel web perangkat embedded |
| D3 — Multi-bahasa | ✅ | Aset CSS/JS bahasa-agnostik; distribusi identik (byte sama) lewat npm, Composer, RubyGems, Bower, NuGet & Maven (GitHub Packages), container, CDN jsDelivr/unpkg |
| D4 — Ekosistem Lombok | N/A | L0 zero-dependency by design; tidak memakai library Lombok lain. Bekerja berdampingan (peer opsional) dengan LombokIcons, LombokAnimate, LombokCharts, LombokTableSheet |
| D5 — Keamanan | ⏳ | CodeQL, OSSAR, Defender for DevOps, dependency-review, action di-pin SHA, JS tanpa jaringan/storage. Belum ada SBOM rilis; kontak email di `SECURITY.md` masih placeholder (temuan C-02) |
| D6 — Keunikan (SOTA) | ✅ | Satu markup → lima gaya desain via satu atribut `data-style`, dikomposisi dengan `data-theme` dan `dir`; pembanding (Bootstrap, Bulma, Pico, DaisyUI) mengikat tampilan ke komponen atau ke build step |
| D7 — Skala pengguna | ✅ | Indie (CDN satu baris) → startup (npm) → enterprise (override token/gaya kustom, paket GitHub Packages) |
| D8 — Kelengkapan | ⏳ | 40+ komponen, utilitas, mode classless, lapisan cetak, tabel sortir sadar-bahasa. Gap vs Bootstrap: tooltip JS, scrollspy, validasi form JS, date picker (lihat [Full Summary](full_summary_project_LombokCSS_v0.1.9.md) §3) |
| D9 — Standar internasional | ✅ | WCAG 2.2 AA (kontras gaya bawaan), WAI-ARIA 1.2 + APG (tabs, dialog, disclosure, sortable table), CSS Logical Properties, Media Queries L5, BCP 47 (`lang` → `Intl.Collator`), WHATWG HTML (`<dialog>`, `<details>`) |

Skor: **6/9 ✅** (D1, D2, D3, D6, D7, D9) — memenuhi ambang rilis registry publik (≥6/9).
Penilaian mandiri; belum ada review independen.

## 4. Kepatuhan dokumen & README (MASTERPLAN_UTAMA v3.4 §5)

| Syarat | Status |
| --- | --- |
| 12 dokumen standar (§5.1) | ✅ `docs/*_LombokCSS_v0.1.9.md` |
| Checklist universalitas (§5.2) | ✅ §3 dokumen ini |
| README "Why this library? (Mengapa library ini?)" (§5.3) | ✅ |
| README "Standards implemented" | ✅ |
| README "Lombok Ecosystem" berlabel peer, bukan pemilik | ✅ |
| Deskripsi manifest (npm, Composer, gem, Bower, NuGet, Maven) tanpa klaim aplikasi + "Part of Lombok Ecosystem" | ✅ |
| Deskripsi GitHub (About) | ⏳ Perlu diubah manual oleh pemilik (lihat §6) |
| Audit pola terlarang (ARCHITECTURE v3.4 §4) | ✅ nol kecocokan (`part of Lombok[A-Z]`, `library #`, `component of`, `for Lombok(RAG\|PDF\|Agentic)`) |

## 5. Temuan audit repo (v3.4)

| ID | Temuan | Severity | Status |
| --- | --- | --- | --- |
| C-01 | README belum memuat bagian "Mengapa library ini?" & "Standar" (U-004) | 🟡 Rendah | ✅ Diperbaiki |
| C-02 | `SECURITY.md` memakai email placeholder `security@your-domain.example` | 🟠 Sedang | ❌ OPEN — pemilik perlu menetapkan alamat nyata |
| C-03 | Folder `package/` adalah salinan lama (README & dist tidak sinkron dengan root) dan tidak dipakai `files` npm | 🟡 Rendah | ❌ OPEN — usul dihapus |
| C-04 | Belum ada SBOM di rilis (Prinsip #8) | 🟡 Rendah | ❌ OPEN — target 0.2.0 |
| C-05 | Sortir tabel memakai `localeCompare()` tanpa locale → urutan tidak sesuai bahasa halaman (Prinsip #6, D9) | 🟡 Rendah | ✅ Diperbaiki: `Intl.Collator` dari `lang` terdekat, `numeric: true`, fallback aman untuk tag rusak (+2 test) |
| C-06 | Nama dokumen standar mengikat versi; release-please tidak mengganti nama berkas | 🟡 Rendah | ❌ OPEN — rename manual saat rilis minor |

## 6. Tindakan manual pemilik

1. GitHub → Settings → About, deskripsi:
   `Universal token-first CSS framework — one markup, five design styles, dark mode + RTL, ~10 KB gzip, zero dependencies. Part of Lombok Ecosystem. MIT.`
2. Isi alamat kontak keamanan nyata di `SECURITY.md` (C-02).

## 7. Roadmap

| Versi | Fokus |
| --- | --- |
| 0.1.x | Kepatuhan v3.4 (dokumen, README, manifest), perbaikan bug |
| 0.2.0 | SBOM + provenance di rilis; hapus `package/`; tooltip & validasi form opsional; dokumen di-rename ke v0.2.0 |
| 0.3.0 | Paket token (JSON, W3C Design Tokens format) untuk dikonsumsi alat desain & library lain |
| 1.0.0 | API kelas & token dibekukan (semver penuh) |
