---
tipe: tugas
tags: [statistika, regresi-harmonik, tugas]
---

# Daftar Tugas dan Status Proyek

Lingkup: laporan Bab I–III, Daftar Pustaka, Lampiran A dan B. Tidak ada Bab IV dan Bab V.

## 1. Data
- [x] Ekstraksi 72 data observasi bulanan BPS Kota Mataram (2020–2025) tanpa data kosong.
- [x] Verifikasi angka BPS terhadap dokumen PDF dan rata-rata tahunan.
- [x] Statistik deskriptif (mean 174,80 mm, median 173,70 mm, modus 0,00 mm, simpangan baku sampel 135,35 mm).

## 2. Literatur
- [x] 15 artikel Indonesia 2016–2026, isi dari abstrak resmi; metadata cocok Crossref.
- [x] Kelompok Tabel 2.1: 5 Fourier/harmonik, 6 spektral, 3 Mataram/NTB metode lain, 1 musim dan RMSE.
- [x] Bimaprawira (2021) dan Pratiwi (2020) diganti [[Zega 2025]] dan [[Kotarumalos 2025]] (31 Okt).
- [x] 12 artikel dibaca penuh untuk uji hipotesis: [[Catatan Progres 31 Okt 2026]].
- [x] Audit Aulia (2019), Khikmah & Sofro (2025), Mulsandi (2024) selesai 31 Okt 2026.
- [x] Daftar Pustaka 22 entri APA 7 (Aulia 2019, Khikmah 2025, Mulsandi 2024 dilepas 1 Nov) (Wei dilepas 31 Okt; Wilks dilepas 1 Nov; Sudaryono tetap, ISBN terverifikasi).

## 3. Naskah
- [x] Format naskah template S1 Ilmu Komputer Universitas Bumigora.
- [x] Abstrak (4 paragraf), Kata Pengantar, Daftar Isi/Tabel/Gambar.
- [x] Bab I (7 paragraf latar belakang, 1 rumusan, 1 tujuan), Bab II (Tabel 2.1, Gambar 2.1), Bab III.
- [x] Lampiran A (6 tangkapan BPS). Lampiran B: lihat bagian 4 (tangkapan baru belum ada).
- [x] Bab IV, Bab V, dan bahan presentasi dikeluarkan dari proyek (31 Okt 2026), disimpan di `arsip_di_luar_bab3/`.

## 4. Terbuka
- [x] Keputusan 31 Okt: ADF dan Ljung-Box dibuang; uji hipotesis uji F saja ($H_0: b_1 = b_2 = 0$, $\alpha = 0{,}05$), uji t dibuang; Wei (2019) dilepas; sheet sin/cos tidak dibuat. Rincian di [[Catatan Progres 31 Okt 2026]]; urutan kerja di [[Riwayat Pekerjaan]].
- [x] Teks Abstrak, Bab II 2.2/2.4/2.7, Bab III 3.9, Gambar 2.1, Alur Regresi Harmonik, dan Panduan sudah diubah di vault (31 Okt).
- [x] Xlsx sampai Bab III dibuat (31 Okt): `hasil/Data_Curah_Hujan_Mataram_Bab3.xlsx`, 2 sheet, 0 sel error, angka cocok dengan statistik sebelumnya. Salinan di `hasil/kirim/`. Xlsx lama berisi hasil disalin ke `arsip_di_luar_bab3/hasil/`.
- [ ] Lampiran B di PDF: dikerjakan pengguna sendiri. Judul gambar di skrip dan daftar di [[Lampiran]] sudah disesuaikan (1 Nov); sisa: tangkapan layar. Tangkapan lama B.3–B.7 sudah dipindah ke arsip (1 Nov); `hasil/lampiran/` kini hanya berisi `harmonik_excel_1` dan `_2` (statistik deskriptif) dan tangkapan BPS. Seluruh berkas hasil regresi/ARMA lain sudah di `arsip_di_luar_bab3/hasil/` (1 Nov).
- [x] Skrip build disatukan jadi dua berkas, `build/buat_xlsx.py` dan `build/buat_docx.py`, dan teksnya sudah disamakan dengan vault (31 Okt). Diuji di folder sementara: 27 halaman, 36 tautan, 26 entri, tanpa ADF/Ljung-Box/Wei.
- [ ] Build ulang PDF/docx ke `hasil/`: menunggu perintah, dan menunggu Lampiran B baru dari pengguna. Build terakhir 1 Nov (tahap 21–22, 24 halaman) sudah tertinggal dari vault karena perbaikan tahap 23.
- [x] Perbaikan vault tahap 23 (1 Nov, tanpa build): sitasi Bab I par. 6, Bab II 2.3 dan 2.5; Bab III 3.6 (Excel hanya data dan statistik deskriptif); tanggal Kata Pengantar November 2026; [[Status Laporan Revisi]] disegarkan; [[Pertanyaan Terbuka]] No. 5 (autokorelasi residual).
- [x] DOI Kotarumalos: selesai. Pengguna menyetujui tautan halaman jurnal (1 Nov 2026); tidak perlu dicek ulang.
- [x] Bab I par. 1: "sumber daya air" dan kekeringan kini bersitasi Aulia Putri dkk. (2026); pertanian ditambah Hadinata dkk. (2026) (1 Nov).
- [ ] Varians sampel: tidak wajib; tambahkan hanya bila dosen minta ([[Konsep Varians Sampel]]).

## 5. Revisi ramal 2026 (25 Nov 2026, [[Keputusan Ramal 2026 dan Dasar Penelitian]])
- [x] Vault: Abstrak par. 2–4; Bab I par. 7, 1.2, 1.3 butir 5, 1.4, 1.5; Bab II 2.4 (alasan k = 1), 2.5 (jadi Ukuran Kecocokan Model), 2.6, 2.7; Bab III 3.2, 3.5 (pencilan Desember 2024), 3.9.
- [x] Gambar 2.1 (sumber adaptasi Kusdarwati dan Astuti), Alur Regresi Harmonik, Data BPS 72 Bulan bagian 4, Tabel 2.1 (dasar penelitian), Peta, START, kanvas, catatan konsul K02, K04, K08, K10.
- [x] Panduan 00–04 dan Konsep (Data Latih dan Data Uji, RMSE, Baseline, R², Uji F, OLS, Deret Waktu, Penelitian Terdahulu).
- [x] Teks `build/buat_docx.py` disamakan dengan vault (tidak dijalankan).
- [ ] Docx: belum diubah. Bagian yang perlu disamakan sama dengan daftar vault di atas; tunggu perintah.
- [x] Judul (25 Nov 2026): "Analisis Curah Hujan Bulanan Kota Mataram Tahun 2020–2025 dan Peramalan Tahun 2026 dengan Model Regresi Harmonik" (vault dan `buat_docx.py`; docx belum).

Kembali: [[00 Peta Proyek]]
- [x] OCR Susilokarti (1 Nov 2026): abstrak cocok dengan isi, kecuali angka MSE 14,92 yang hanya ada di abstrak; dibuang dari Tabel 2.1.
