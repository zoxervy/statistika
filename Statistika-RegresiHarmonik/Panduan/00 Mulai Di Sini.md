---
tipe: panduan
tags: [statistika, regresi-harmonik, panduan]
---

# Mulai Di Sini

Catatan ini untuk anggota kelompok yang belum paham statistika sama sekali. Semua istilah dijelaskan dari nol, dengan contoh angka kecil. Baca berurutan; tiap istilah punya catatan sendiri di folder `Konsep/`.

## Penelitian ini tentang apa, dalam satu paragraf
Hujan di Kota Mataram tidak turun merata sepanjang tahun. Rata-rata Desember (2020–2025) 350,9 mm, rata-rata Juli hanya 43,2 mm. Pola ini berulang tiap tahun. Kami ingin tahu: kalau pola berulang itu ditulis sebagai satu rumus gelombang, seberapa cocok rumus itu dengan hujan 2020–2025, dan berapa tebakannya untuk tiap bulan tahun 2026? Rumus dibuat dari seluruh 72 bulan, karena dosen meminta langsung meramal 2026.

## Analogi pegangan
Bayangkan jam dinding yang jarumnya berputar satu putaran penuh tiap 12 bulan. Posisi jarum menentukan "hujan sedang banyak atau sedikit". Rumus kami hanya mencari tiga angka: tinggi rata-rata, seberapa jauh ayunan naik-turun, dan bulan berapa puncaknya. Tiga angka itu cukup untuk menggambar satu gelombang tahunan.

## Bahan
- 72 angka: curah hujan bulanan Januari 2020 sampai Desember 2025, dari buku BPS *Kota Mataram dalam Angka* (data asal BMKG).
- Ke-72 angka dipakai semua untuk membuat rumus. Tidak ada data uji ([[Konsep Data Latih dan Data Uji]] menjelaskan kenapa).
- Penelitian dasar: Kusdarwati (2023) untuk cara kerja, dan Astuti dkk. (2018) yang dulu meneliti hujan Mataram dengan deret Fourier dan kini kami lanjutkan dengan data baru ([[Keputusan Ramal 2026 dan Dasar Penelitian]]).

## Langkah kerja (Bab III, subbab 3.9)
1. Susun 72 angka menjadi tabel 6 tahun × 12 bulan.
2. Hitung mean, median, modus, simpangan baku.
3. Buat dua kolom bantu (sinus dan kosinus dari waktu), cari tiga angka rumus dengan OLS dari 72 bulan, lalu uji dengan uji F apakah gelombang itu nyata atau kebetulan.
4. Ukur seberapa cocok kurva dengan 72 data (R² dan RMSE), lihat grafik data di samping kurva, lalu tebak 12 bulan tahun 2026.

## Batas laporan
Laporan berhenti di **Bab III**. Tidak ada Bab IV dan V, jadi tidak ada angka hasil model di laporan. Yang ada: latar belakang, teori, dan rencana cara kerja.

## Urutan baca
1. [[01 Abstrak dan Kata Pengantar]]
2. [[02 Bab I Pendahuluan]]
3. [[03 Bab II Kajian Pustaka]]
4. [[04 Bab III Metode Penelitian]]

Tiap catatan Panduan memakai pola yang sama: **Isi** (apa yang tertulis), **Artinya** (bahasa biasa), **Alasan** (kenapa ditulis begitu), **Kalau ditanya dosen** (jawaban pendek). Bagian **Belum beres** menandai hal yang masih dicek; jangan dijawab seolah sudah pasti.

## Kamus istilah (urut dari paling dasar)
Dasar data:
- [[Konsep Curah Hujan dan Milimeter]]
- [[Konsep Monsun dan El Nino]]
- [[Konsep Sumber Data BPS]]
- [[Konsep Keanehan Data]]
- [[Konsep Skala dan Variabel]]
- [[Konsep Populasi dan Sampel]]

Statistik deskriptif:
- [[Konsep Mean Median Modus]]
- [[Konsep Varians Sampel]]
- [[Konsep Simpangan Baku]]

Inti metode:
- [[Konsep Deret Waktu dan Pola Musiman]]
- [[Konsep Regresi Harmonik dan Gelombang Sinus Kosinus]]
- [[Konsep Estimasi OLS]]
- [[Konsep Hipotesis dan Uji F]]
- [[Konsep Amplitudo dan Fase]]
- [[Konsep R-Squared dan Goodness of Fit]]

Menilai model:
- [[Konsep RMSE dan MAE]] (RMSE dipakai bersama R²)
- [[Konsep Data Latih dan Data Uji]] (kenapa tidak dipakai lagi)
- [[Konsep Baseline Ramalan Rata-rata]] (tidak dipakai lagi)

Pustaka:
- [[Konsep Penelitian Terdahulu Harmonik]]
- [[Konsep Rujukan Teori dan Daftar Pustaka]]

Aturan main proyek: [[Aturan Kerja]]. Kembali: [[00 Peta Proyek]]
