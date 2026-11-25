---
tipe: build
tags: [statistika, regresi-harmonik, build]
---

# Build

Dua skrip mandiri. **Jangan dijalankan jika tidak disuruh** ([[Aturan Kerja]]).

| Berkas | Fungsi | Keluaran |
|---|---|---|
| `buat_xlsx.py` | Excel sampai Bab III: sheet Data (matriks 6×12, rata-rata hitungan vs BPS, 2 grafik) dan Ringkasan (mean, median, modus, simpangan baku, min, maks, n, musim, grafik). Tanpa regresi | `hasil/Data_Curah_Hujan_Mataram_Bab3.xlsx` |
| `buat_docx.py` | Laporan Bab I–III, Daftar Pustaka, Lampiran A dan B; PDF dibuat LibreOffice agar nomor halaman daftar isi benar | `hasil/Laporan_RegresiHarmonik_Bab1-3.docx` dan `.pdf` |

Perintah (dari folder `kuliah/statistika`):
```
.venv/bin/python vault/Statistika-RegresiHarmonik/build/buat_xlsx.py
.venv/bin/python vault/Statistika-RegresiHarmonik/build/buat_docx.py
```

## Catatan
- `buat_docx.py` adalah gabungan skrip lama (`buat_laporan`, `buat_laporan_ringkas`, `buat_laporan_revisi`, `buat_laporan_bab3`, `buat_pdf_harmonik`) yang dipangkas ke metode yang dipakai saja. Tidak lagi bergantung pada `hasil/ringkasan.json` (analisis ARMA lama).
- Tabel 2.1 dan Daftar Pustaka dibaca dari vault (`03 Artikel/`, `02 Laporan/`). Teks bab ditulis di dalam skrip dan **harus sama dengan `02 Laporan/`** sebelum build.
- Teks sudah disamakan dengan vault per 31 Okt 2026 (tanpa ADF, Ljung-Box, uji t, Wei; uji F saja; Zega dan Kotarumalos; 22 entri pustaka; Wilks dilepas 1 Nov). Diuji di folder sementara (27 halaman, 36 tautan, 26 entri); `hasil/` asli belum ditimpa.
- Lampiran B membaca `hasil/lampiran/harmonik_excel_*.png`, urut sebagai Gambar B.1, B.2, dan seterusnya. Judul gambar (`XL_JUDUL` di `buat_docx.py`) sudah disesuaikan dengan `Data_Curah_Hujan_Mataram_Bab3.xlsx` (4 judul). Tangkapan lama B.3–B.7 berisi hasil regresi dan sudah dipindah ke arsip. Jika tangkapan baru lebih dari 4, gambar ke-5 dan seterusnya otomatis berjudul "Lembar kerja, bagian N"; tambahkan judul di `XL_JUDUL`.
- Gambar 2.1 dibuat ulang saat build (`hasil/grafik/kerangka_harmonik.png`).
- Salinan skrip lama masih ada di `analisis/` dan backup `~/.hermes/cache/scratch/build_bak/`. Edit hanya skrip di folder ini.
- Excel lama berisi hasil regresi (`buat_xlsx_harmonik.py`) tidak dipakai lagi; berkas hasilnya diarsipkan di `arsip_di_luar_bab3/hasil/`.

Kembali: [[00 Peta Proyek]]
