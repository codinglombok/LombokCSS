# CLAUDE.md — memori proyek LombokCSS

Berkas ini adalah memori lintas sesi untuk Claude Code. Baca dulu sebelum bekerja,
perbarui di akhir setiap sesi (bagian "Status & lanjutan").

## Konteks

- Repo `codinglombok/LombokCSS`, katalog ekosistem **01.01**, tingkat **L0**, status 🟢 LIVE, versi **0.1.9**, lisensi **MIT**.
- Acuan normatif: **MASTERPLAN_UTAMA v3.4** (2026-09-29) — Prinsip #11 "Universal tanpa klaim aplikasi", **ADR-019**, 9 dimensi D1–D9, 12 dokumen standar per repo.
- Dokumen standar repo: `docs/*_LombokCSS_v0.1.9.md` (masterplan, architecture, changelog, map, structure_repo, full_summary_project, guide_how_to_use, how_to_dist, development_ide, API, Lang, SPEC) — **LOKAL SAJA**, tidak di-commit.

## Aturan wajib (v3.4)

- **Markdown (keputusan pemilik):** hanya `*.md` di root repo (README, CHANGELOG, CONTRIBUTING, dst.) dan `.github/` yang boleh online. Semua `*.md` di subfolder (mis. `docs/masterplan_*.md`) di-`.gitignore` dan disimpan lokal saja. Jangan pernah `git add -f` berkas itu. (Kasus sama pernah terjadi di LombokCompress.)

- DILARANG di README/manifest/dokumen: "Part of Lombok<Aplikasi/Framework>", "Library #…", "component of …", "for LombokRAG/PDF/Agentic". Yang boleh: "Part of Lombok Ecosystem", "Dipakai oleh X" (bagian terpisah).
- Audit cepat: `grep -n -i -E "part of Lombok[A-Z]|library #|component of|for Lombok(RAG|PDF|Agentic)" README.md package.json composer.json bower.json lombokcss.gemspec`
- README wajib punya "Why this library? (Mengapa library ini?)" dan "Standards implemented".
- Checklist D1–D9 di `docs/masterplan_…` minimal 6/9 ✅ untuk rilis publik (saat ini 6/9).

## Perintah

```bash
npm ci && npm run build        # dist/ dari src/
npm test                       # anggaran ukuran (CSS ≤15 KB, JS ≤4 KB gzip) + SSR guard
npx playwright test tests/behavior.spec.js   # 44 test perilaku
npm run lint                   # Prettier
cp dist/lombok.js docs/assets/lombok.js      # sinkron aset situs bila JS berubah
```

- `CHANGELOG.md` ditulis release-please — jangan diedit tangan; catatan masterplan masuk ke `docs/changelog_LombokCSS_v<ver>.md` (lokal).
- Perubahan perilaku JS: perbarui `docs/SPEC_…` + test di `tests/behavior.spec.js`.

## Status & lanjutan

Sesi 2026-09-30 (branch `claude/affectionate-sagan-o4rxmx`) — penyelarasan v3.4:

- [x] 12 dokumen standar + checklist universalitas (6/9)
- [x] README: Why this library, Standards implemented, ekosistem = peer
- [x] Deskripsi manifest npm/Composer/Bower/gem/NuGet/Maven + "Part of Lombok Ecosystem"
- [x] `lombok.js`: sortir tabel via `Intl.Collator` dari `lang` terdekat (+2 test)

Sesi 2026-09-30 lanjutan — PR #36 di-merge; lalu PR #38 (di-merge):

- [x] C-03: folder `package/` dihapus
- [x] `docs/*.md` dicabut dari git + `.gitignore` (`*.md`, kecuali root dan `.github/`)

Pembersihan riwayat (2026-10-01, dijalankan pemilik dengan `git filter-branch`):

- [x] `docs/*_LombokCSS_*.md` dihapus dari seluruh riwayat `main`; force-push `44f0ef5 → 2b95d7d`. Semua hash commit `main` berubah.
- [x] Branch `release-please--branches--main--components--lombokcss` dihapus (PR #37 tertutup; release-please membuat ulang dari `main` baru).
- [x] Terverifikasi via clone mirror: 0 commit memuat dokumen itu di semua branch + 10 tag.
- **Jangan pernah push dari clone lama** (sebelum `2b95d7d`) — riwayat lama akan kembali. Clone ulang dulu.
- Commit lama `43321ef`/`5ff26d9` hanya tersisa di `refs/pull/36`, `37`, `38` (tidak bisa dihapus lewat push).

Belum selesai (lanjutkan di sesi berikut):

- [ ] Pemilik: minta GitHub Support (kategori "Remove sensitive data") menghapus cached view + `refs/pull/36`, `37`, `38` (commit `43321ef`, path `docs/*_LombokCSS_v0.1.9.md`)
- [ ] Pemilik: ganti folder lama `C:\Users\Raffa\Documents\GitHub\LombokCSS` dengan clone baru (atau pakai `LombokCSS-clean`)
- [ ] Pemilik: ubah deskripsi GitHub About (teks ada di `docs/masterplan_…` §6)
- [ ] Pemilik: perbaiki model Copilot untuk check `github-advanced-security` (gagal: "model not supported")
- [ ] C-02: email kontak nyata di `SECURITY.md` (masih placeholder) — butuh keputusan pemilik
- [ ] C-04: SBOM + provenance npm di workflow rilis (target 0.2.0)
- [ ] C-06: rename `docs/*_v0.1.9.md` saat versi minor naik
- [ ] D8: tooltip & validasi form opsional; D5 → ✅ setelah C-02 + C-04
