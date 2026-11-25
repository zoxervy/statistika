---
tipe: berkas
tags: [statistika, regresi-harmonik, berkas]
---

# Berkas dan Aset Digital

Folder ini memuat data mentah, grafik data, dan aset sampul. Berkas hasil model (Bab IV/V) dipindah ke `arsip_di_luar_bab3/` di luar vault.

| Nama Berkas | Keterangan |
|---|---|
| `curah_hujan_bulanan_bps_bmkg.csv` | Data mentah 72 bulan BPS (Jan 2020 – Des 2025) |
| `deret_waktu.png` | Grafik visualisasi deret waktu curah hujan 72 bulan (2020–2025) |
| `boxplot_bulan.png` | Boxplot distribusi sebaran curah hujan per bulan kalender |
| `logo_ubg.png` | Lambang resmi Universitas Bumigora untuk sampul laporan |

## Hasil akhir (di luar vault, folder proyek `kuliah/statistika/`)

| Berkas | Isi | Dibuat oleh |
|---|---|---|
| `hasil/Laporan_RegresiHarmonik_Bab1-3.pdf` / `.docx` (**dihapus 1 Nov 2026**: versi lama memuat ADF dan Ljung-Box; dibuat lagi oleh `build/buat_docx.py` saat build) | Laporan Bab I–III, Daftar Pustaka, Lampiran A dan B; daftar isi bisa diklik | `build/buat_docx.py`. **Berkas ini masih versi lama (27 entri, Wei, ADF, Ljung-Box); versi baru 26 entri belum dibuild** |
| `hasil/Data_Curah_Hujan_Mataram_Bab3.xlsx` | 2 sheet: Data (matriks 6×12, rata-rata hitungan vs BPS, 2 grafik) dan Ringkasan (mean, median, modus, simpangan baku, min, maks, n; musim; grafik) | `build/buat_xlsx.py` |
| `hasil/Statistika-RegresiHarmonik.zip` | Vault ini | – |

Salinan kirim ada di `hasil/kirim/`. Berkas ARMA lama tidak dihapus.

Kembali: [[00 Peta Proyek]]

## PDF artikel (1 Nov 2026)
- `Berkas/Artikel/`: 15 PDF artikel Tabel 2.1 (nama sama dengan catatan di `03 Artikel/`), `README.txt`, dan hasil OCR `Susilokarti 2016 (OCR).txt`. Aulia 2019 dan Khikmah 2025 dipindah ke `arsip_di_luar_bab3/artikel_dilepas/` (1 Nov 2026).

## Data mentah BPS (1 Nov 2026)
- `data_mentah/curah_hujan_bulanan_bps_bmkg.csv`: 72 nilai.
- `Berkas/BPS/`: tujuh halaman BPS yang dipakai laporan (PDF satu halaman, di dalam vault). Teksnya: `data_mentah/bps_halaman/`.
- `data_mentah/bps_pdf/dda2021.txt` sampai `dda2026.txt`: teks penuh enam buku. PDF penuhnya sudah dihapus.
