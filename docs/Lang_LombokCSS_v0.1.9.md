# Bahasa (i18n) — LombokCSS v0.1.9

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

## 1. Ringkasan i18n

LombokCSS **tidak mengirim string UI sendiri**: semua teks (label tombol, isi toast,
judul) ditulis pemakai di HTML/JS. Karena itu katalog pesan Core-20 (Prinsip #6) tidak
berlaku untuk library ini; yang berlaku adalah dukungan tata tulis dan urutan bahasa.

| Kemampuan | Status |
| --- | --- |
| Arah tulisan RTL (Arab, Ibrani, Persia, Urdu) | ✅ CSS logical properties; carousel sadar `dir` |
| Urutan alfabet per bahasa (sortir tabel) | ✅ `Intl.Collator` dari atribut `lang` terdekat (BCP 47) |
| Angka dalam teks ("Item 2" < "Item 10") | ✅ `numeric: true` |
| Font skrip non-Latin | ⏳ pakai `--lc-font-sans`; tidak ada font bawaan |
| Katalog pesan | N/A — tidak ada pesan bawaan |

## 2. Contoh

```html
<html lang="ar" dir="rtl">
<table class="table" lang="sv">…</table>   <!-- Å, Ä, Ö diurutkan setelah Z -->
```

## 3. Aturan fallback

Tag `lang` kosong, tidak ada, atau tidak valid → collation default runtime (tidak melempar error).
