---
tipe: panduan
tags: [statistika, regresi-harmonik, panduan]
---

# Mulai Di Sini

Catatan ini untuk anggota kelompok yang belum paham statistika sama sekali. Semua istilah dijelaskan dari nol, dengan contoh angka kecil. Baca berurutan; tiap istilah punya catatan sendiri di folder `Konsep/`.

## Penelitian ini tentang apa, dalam satu paragraf
Hujan di Kota Mataram tidak turun merata sepanjang tahun. Rata-rata Desember (2020–2025) 350,9 mm, rata-rata Juli hanya 43,2 mm. Pola ini berulang tiap tahun. Kami ingin tahu: kalau pola berulang itu ditulis sebagai satu rumus gelombang, seberapa dekat tebakan rumus itu ke hujan sebenarnya? Untuk menguji, rumus dibuat dari hujan 2020–2024, lalu tebakannya dibandingkan dengan hujan 2025 yang sengaja disembunyikan dulu.

## Analogi pegangan
Bayangkan jam dinding yang jarumnya berputar satu putaran penuh tiap 12 bulan. Posisi jarum menentukan "hujan sedang banyak atau sedikit". Rumus kami hanya mencari tiga angka: tinggi rata-rata, seberapa jauh ayunan naik-turun, dan bulan berapa puncaknya. Tiga angka itu cukup untuk menggambar satu gelombang tahunan.

## Bahan
- 72 angka: curah hujan bulanan Januari 2020 sampai Desember 2025, dari buku BPS *Kota Mataram dalam Angka* (data asal BMKG).
- 60 angka pertama (2020–2024) = **data latih**, untuk membuat rumus.
- 12 angka terakhir (2025) = **data uji**, untuk menilai rumus.

## Langkah kerja (Bab III, subbab 3.9)
1. Susun 72 angka menjadi tabel 6 tahun × 12 bulan.
2. Hitung mean, median, modus, simpangan baku.
3. Buat dua kolom bantu (sinus dan kosinus dari waktu), cari tiga angka rumus dengan OLS, lalu uji dengan uji F apakah gelombang itu nyata atau kebetulan.
4. Tebak 12 bulan 2025, hitung seberapa meleset (RMSE dan MAE), bandingkan dengan dua tebakan sederhana: (a) satu angka rata-rata untuk semua bulan, dan (b) rata-rata tiap bulan kalender (Januari ditebak dengan rata-rata Januari tahun-tahun sebelumnya, dan seterusnya).

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

Menilai ramalan:
- [[Konsep Data Latih dan Data Uji]]
- [[Konsep RMSE dan MAE]]
- [[Konsep Baseline Ramalan Rata-rata]]

Pustaka:
- [[Konsep Penelitian Terdahulu Harmonik]]
- [[Konsep Rujukan Teori dan Daftar Pustaka]]

Aturan main proyek: [[Aturan Kerja]]. Kembali: [[00 Peta Proyek]]
