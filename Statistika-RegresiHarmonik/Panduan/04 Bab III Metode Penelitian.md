---
tipe: panduan
tags: [statistika, regresi-harmonik, panduan]
---

# Panduan 04: Bab III Metode Penelitian

Naskah asli: [[Bab III Metode Penelitian]]. Prasyarat: [[03 Bab II Kajian Pustaka]].

Bab III menjawab: **bagaimana penelitian dikerjakan, supaya orang lain bisa mengulangi dan memeriksa?** Isinya data dari mana, diolah pakai apa, dan analisisnya langkah apa.

## 3.1 Jenis penelitian
- **Isi:** Kuantitatif, data sekunder deret waktu; analisis deskriptif (merangkum) dan prediktif (memodelkan pola dan meramal).
- **Artinya:** Kuantitatif = berupa angka. Sekunder = angkanya dikumpulkan pihak lain (BPS/BMKG), bukan kami ukur sendiri. Deskriptif = menceritakan data apa adanya. Prediktif = menebak yang belum terjadi.
- Konsep: [[Konsep Deret Waktu dan Pola Musiman]].

## 3.2 Lokasi dan waktu
Kota Mataram, NTB; data Januari 2020–Desember 2025; pengolahan Oktober 2026. Satu kalimat, tidak perlu dijelaskan panjang.

## 3.3 Pengumpulan data
- **Isi:** Dibaca dari Tabel 1.2.1 buku *Kota Mataram dalam Angka* edisi 2021–2026. Satu edisi memuat satu tahun, jadi edisi N berisi data tahun N−1. Data tidak diunduh dari portal BMKG karena dibatasi dua tahun per permintaan dan perlu akun.
- **Artinya:** Buku terbitan 2021 berisi hujan tahun 2020, dan seterusnya. Itu membingungkan, jadi ada tabel pemetaan.

| Tahun data | Buku | Halaman PDF |
|---|---|---|
| 2020 | Dalam Angka 2021 | 78 |
| 2021 | Dalam Angka 2022 | 84 |
| 2022 | Dalam Angka 2023 | 79 |
| 2023 | Dalam Angka 2024 | 80 |
| 2024 | Dalam Angka 2025 | 73 |
| 2025 | Dalam Angka 2026 | 73 |

- **Alasan:** Setiap angka bisa dilacak sampai halaman. Bukti tangkapan layar ada di Lampiran A (enam gambar, satu per halaman).
- Konsep: [[Konsep Sumber Data BPS]].

## 3.4 Populasi dan sampel
- **Isi:** Populasi = seluruh hujan bulanan Mataram sepanjang waktu. Sampel = 72 bulan Jan 2020–Des 2025, diambil semua karena deret waktu tidak boleh bolong.
- **Dampak ke hitungan:** karena sampel, simpangan baku memakai pembagi n−1.
- Konsep: [[Konsep Populasi dan Sampel]].

## 3.5 Jenis dan sumber data, serta keanehan data
- **Isi:** Data sekunder, kuantitatif, skala rasio. Sebelum dipakai, dua pemeriksaan dilakukan: rata-rata 12 bulan tiap tahun dicocokkan dengan baris "Kota Mataram" di tabel BPS, dan 72 angka dicocokkan satu per satu dengan halaman PDF.
- **Artinya:** Yang dicek adalah *kami menyalin dengan benar*. Itu tidak membuktikan angka BPS sendiri benar, dan laporan menyebutnya terus terang.
- **Empat catatan jujur** (ini yang paling sering ditanya):
  1. Judul tabel menyebut stasiun "BMKG Lombok Barat" (edisi 2024 tidak menyebut stasiun). Jadi belum pasti stasiunnya ada di dalam Kota Mataram.
  2. Juli 2021 dan Agustus 2023 tercatat 0,00 mm, padahal ada hari hujan (6 dan 1). Dugaan: hujan di bawah batas ukur dicatat nol, tetapi salah cetak belum bisa dikesampingkan. Angka tidak diubah.
  3. Rata-rata 2024: edisi 2025 menulis 150,73 mm, edisi 2026 menulis 166,82 mm. Data bulanan 2024 tetap dari edisi 2025 karena edisi 2026 tidak memuat rincian bulanan.
  4. Presisi angka berbeda antar edisi dan tidak dicocokkan ke portal BMKG.
- **Selisih 0,01 mm pada 2024** di teks: hitungan 150,725 vs tabel 150,73. Itu hanya pembulatan.
- Konsep: [[Konsep Keanehan Data]]; rincian: [[Catatan Kualitas Data]], [[Revisi BPS 2024]].

## 3.6 Teknik dan alat
- **Isi:** PDF diubah ke teks dengan *pdftotext*, 12 nilai tiap edisi disalin ke satu CSV (72 baris). Hitungan statistik dan regresi memakai Python 3 (pandas, SciPy, statsmodels, matplotlib). Tabel data dan statistik deskriptif disajikan di Excel (Lampiran B).
- **Artinya:** Python mengerjakan semuanya, termasuk regresi. Excel hanya memuat data dan statistik deskriptif (mean, median, dan seterusnya), supaya dosen bisa membuka dan mengklik rumusnya. Regresi, uji F, dan ramalan **tidak** ada di Excel.
- **Berkas Excel:** `Data_Curah_Hujan_Mataram_Bab3.xlsx`, dua sheet. *Data*: tabel 6 tahun × 12 bulan, rata-rata, kolom cek terhadap BPS, dua grafik. *Ringkasan*: mean, median, modus, simpangan baku, min, maks, jumlah data, rata-rata musim, grafik. Statistik di sana berupa rumus aktif, jadi bisa diklik dan dilihat rumusnya.

## 3.7 Variabel
- **Isi:** Variabel terikat Y_t = curah hujan bulanan (kontinu, rasio). Variabel bebas dibentuk dari waktu: sin(2πt/12) dan cos(2πt/12). Monsun menjelaskan pola musiman; ENSO memengaruhi variasi antartahun tetapi tidak dimasukkan.
- **Artinya:** "Variabel bebas" di sini bukan suhu atau angin, melainkan hasil olahan nomor bulan. Karena itu penelitian disebut univariat.
- **Alasan tidak memasukkan ENSO/IOD:** kesederhanaan; dan dosen mengatakan variabel X dan Y terpisah tidak wajib ([[K11 Variabel x dan y tidak wajib]]).
- Konsep: [[Konsep Skala dan Variabel]], [[Konsep Monsun dan El Nino]].

## 3.8 Definisi operasional
Curah hujan bulanan = jumlah hujan satu bulan kalender yang dicatat BMKG, dimuat di kolom "Jumlah Curah Hujan" Tabel 1.2.1, dalam mm. Definisi operasional = definisi yang menyebut persis kolom mana dan satuan apa yang dipakai, supaya tidak ada tafsir lain.

## 3.9 Teknik analisis (empat langkah)

### Langkah 1: susun matriks
72 angka ditata menjadi tabel 6 baris (tahun) × 12 kolom (bulan). Tujuan: mudah dibaca dan dihitung per tahun maupun per bulan. Ini sheet *Data* di Excel.

### Langkah 2: statistik deskriptif
Hitung mean, median, modus, simpangan baku per tahun dan seluruh data. Contoh membaca: pada 2024 rata-ratanya 150,73 mm tetapi mediannya hanya 79,35 mm. Bedanya jauh karena Desember 2024 mencapai 672,5 mm yang menarik rata-rata ke atas. Itu alasan melaporkan mean *dan* median. Konsep: [[Konsep Mean Median Modus]], [[Konsep Simpangan Baku]].

### Langkah 3: sinus-kosinus, OLS, uji F
- Waktu diberi nomor: Januari 2020 = 0, Februari 2020 = 1, ... Desember 2020 = 11, Januari 2021 = 12, ... Desember 2024 = 59, Januari 2025 = 60, ... Desember 2025 = 71.
- Tiap bulan diubah menjadi dua angka: X₁ = sin(2πt/12) dan X₂ = cos(2πt/12). Contoh: Januari (t = 0) → X₁ = 0, X₂ = 1. April (t = 3) → X₁ = 1, X₂ = 0. Juli (t = 6) → X₁ = 0, X₂ = −1. Nilainya berulang tiap 12 bulan, itulah yang membuat gelombang berulang.
- Tiga angka b₀, b₁, b₂ dicari dengan OLS dari **60 bulan data latih saja**. Konsep: [[Konsep Estimasi OLS]].
- Uji F memeriksa: gelombang ini nyata atau kebetulan? H₀: b₁ = b₂ = 0, H₁: minimal satu tidak nol, α = 0,05. Konsep: [[Konsep Hipotesis dan Uji F]].
- Sumber bentuk hipotesis: Darmawan dkk. (2017), Purnama (2021). Uji F dibaca dari keluaran regresi: Azmi dkk. (2020).

### Langkah 4: ramal 2025 dan nilai
- Masukkan t = 60 sampai 71 ke rumus → 12 ramalan.
- Bandingkan dengan 12 hujan sebenarnya 2025 → RMSE dan MAE. Konsep: [[Konsep RMSE dan MAE]].
- Bandingkan dengan dua tebakan malas. Konsep: [[Konsep Baseline Ramalan Rata-rata]].
- Pembagian menurut waktu, tidak diacak. Konsep: [[Konsep Data Latih dan Data Uji]].
- Sumber: pengujian 12 bulan terakhir mengikuti Purnama (2021); RMSE mengikuti Permata dkk. (2024) dan Hadinata dkk. (2026).

## Yang sudah dibuang (jangan muncul lagi)
Uji stasioneritas ADF, uji Ljung-Box, uji t, dan model SARIMA sebagai pembanding. Alasannya sederhana: tidak bisa dihitung di Excel, tidak semua artikel acuan memakainya, dan laporan harus mudah dijelaskan.

## Kalau ditanya dosen
- *Kenapa data dari BPS, bukan BMKG?* Portal BMKG membatasi unduhan dua tahun per permintaan dan perlu akun; buku BPS terbuka dan datanya memang asal BMKG.
- *Kenapa angka 0,00 mm dibiarkan?* Karena kami tidak berhak mengubah angka sumber; keanehannya dicatat di 3.5.
- *Kenapa 60 latih dan 12 uji?* 12 bulan = satu siklus penuh; model tidak boleh melihat 2025 saat dibuat.
- *Kenapa hanya uji F?* Yang ditanya cuma satu: ada pola musiman atau tidak. Dua koefisien dinilai sekaligus oleh uji F.
- *Statistik yang dipakai apa?* Mean, median, modus, simpangan baku sampel (n−1), OLS, uji F, RMSE, MAE.

## Belum beres
- Lampiran B baru (tangkapan layar xlsx) dikerjakan pengguna; tangkapan lama B.3–B.7 berisi hasil regresi dan tidak dipakai.

Kembali: [[00 Mulai Di Sini]]
