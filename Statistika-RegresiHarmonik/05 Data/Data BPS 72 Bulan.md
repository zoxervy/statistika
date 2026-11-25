---
tipe: data
tags: [statistika, regresi-harmonik, data]
---

# Data BPS 72 Bulan

Seluruh data curah hujan bulanan Kota Mataram, Januari 2020 sampai Desember 2025, satuan **mm**. Angka disalin apa adanya dari Tabel 1.2.1 *Kota Mataram dalam Angka* (BPS Kota Mataram; data asal BMKG), tanpa pembulatan, penghapusan, atau perkiraan. Berkas data: `Berkas/curah_hujan_bulanan_bps_bmkg.csv` (72 baris). Dihasilkan dan dicek ulang 1 Nov 2026.

## 1. Matriks tahun × bulan (mm)
| Tahun | Jan | Feb | Mar | Apr | Mei | Jun | Jul | Agu | Sep | Okt | Nov | Des | Rata-rata |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **2020** | 182,2 | 150,8 | 273,5 | 214,1 | 173,6 | 37,7 | 13,3 | 65,9 | 51,5 | 213,2 | 281,9 | 203,7 | 155,12 |
| **2021** | 259,0 | 309,0 | 173,8 | 109,0 | 144,5 | 323,0 | 0,0 | 41,0 | 65,0 | 126,5 | 291,4 | 344,0 | 182,18 |
| **2022** | 212,0 | 281,0 | 213,0 | 220,0 | 199,0 | 134,0 | 10,0 | 130,0 | 64,0 | 395,0 | 431,0 | 384,0 | 222,75 |
| **2023** | 254,0 | 454,0 | 264,0 | 114,0 | 8,0 | 4,0 | 69,0 | 0,0 | 1,0 | 31,0 | 137,0 | 303,0 | 136,58 |
| **2024** | 134,8 | 199,9 | 209,0 | 320,9 | 3,2 | 10,5 | 23,9 | 4,7 | 17,2 | 22,9 | 189,2 | 672,5 | 150,73 |
| **2025** | 253,0 | 351,0 | 353,0 | 152,0 | 194,0 | 48,0 | 143,0 | 32,0 | 120,0 | 287,0 | 286,0 | 198,0 | 201,42 |
| **Rata-rata** | 215,8 | 291,0 | 247,7 | 188,3 | 120,4 | 92,9 | 43,2 | 45,6 | 53,1 | 179,3 | 269,4 | 350,9 | 174,80 |

Rata-rata kolom terakhir dan baris terakhir dihitung dari data di atas (bukan disalin dari BPS).

## 2. Cek terhadap rata-rata BPS
Baris "Kota Mataram" pada tabel BPS memuat rata-rata 12 bulan. Hasil hitungan dari 12 angka di atas dibandingkan dengan angka itu:

| Tahun data | Edisi BPS | Halaman PDF | Rata-rata hitungan | Rata-rata baris Kota Mataram BPS | Selisih |
|---|---|---|---|---|---|
| 2020 | Kota Mataram dalam Angka 2021 | 78 | 155,117 | 155,12 | -0,003 |
| 2021 | Kota Mataram dalam Angka 2022 | 84 | 182,183 | 182,18 | 0,003 |
| 2022 | Kota Mataram dalam Angka 2023 | 79 | 222,750 | 222,75 | 0,000 |
| 2023 | Kota Mataram dalam Angka 2024 | 80 | 136,583 | 136,58 | 0,003 |
| 2024 | Kota Mataram dalam Angka 2025 | 73 | 150,725 | 150,73 | -0,005 |
| 2025 | Kota Mataram dalam Angka 2026 | 73 | 201,417 | 201,42 | -0,003 |

Selisih 2024 sebesar 0,005 mm berasal dari pembulatan BPS (150,725 menjadi 150,73). Edisi 2026 mencatat rata-rata 2024 sebesar 166,82 mm; lihat [[Revisi BPS 2024]]. Ke-72 angka juga dicocokkan satu per satu dengan teks halaman BPS yang tersimpan: 0 selisih.

## 3. Angka yang perlu diperhatikan
- **0,0 mm** pada Juli 2021 dan Agustus 2023 (hanya dua nilai nol; tercetak bersama hari hujan, lihat [[Catatan Kualitas Data]]).
- **672,5 mm** pada Desember 2024, nilai terbesar; di atas batas pencilan 590,0 mm (kuartil 3 + 1,5 × jangkauan antarkuartil).
- Seluruh data apa adanya; tidak ada angka yang diubah.

## 4. Pembagian data
- Data latih (60 bulan): Januari 2020 sampai Desember 2024, t = 0 sampai 59.
- Data uji (12 bulan): Januari 2025 sampai Desember 2025, t = 60 sampai 71.
- t = 0 pada Januari 2020.

## 5. Ringkasan statistik deskriptif (72 bulan)
- **Mean:** 174,80 mm
- **Median:** 173,70 mm
- **Modus:** 0,00 mm (muncul dua kali; nilai lain tidak ada yang berulang)
- **Simpangan baku sampel (n − 1):** 135,35 mm
- **Minimum / maksimum:** 0,0 mm / 672,5 mm
- **Musim hujan (Nov–Apr), 36 bulan:** rata-rata 260,52 mm. **Kemarau (Mei–Okt), 36 bulan:** 89,07 mm. Rasio sekitar 2,9 banding 1.
- **Bulan terbasah (rata-rata):** Des 350,9 mm. **Terkering:** Jul 43,2 mm.

Per tahun:
- 2020: mean 155,12; median 177,90; simpangan baku 91,94
- 2021: mean 182,18; median 159,15; simpangan baku 119,36
- 2022: mean 222,75; median 212,50; simpangan baku 131,48
- 2023: mean 136,58; median 91,50; simpangan baku 149,50
- 2024: mean 150,73; median 79,35; simpangan baku 195,81
- 2025: mean 201,42; median 196,00; simpangan baku 107,57

## 6. Daftar panjang (72 baris)
Bentuk yang dipakai pengolahan: satu baris per bulan, t = nomor bulan sejak Januari 2020.

| No | Tahun | Bulan | t | Curah hujan (mm) | Data |
|---|---|---|---|---|---|
| 1 | 2020 | Jan | 0 | 182,2 | latih |
| 2 | 2020 | Feb | 1 | 150,8 | latih |
| 3 | 2020 | Mar | 2 | 273,5 | latih |
| 4 | 2020 | Apr | 3 | 214,1 | latih |
| 5 | 2020 | Mei | 4 | 173,6 | latih |
| 6 | 2020 | Jun | 5 | 37,7 | latih |
| 7 | 2020 | Jul | 6 | 13,3 | latih |
| 8 | 2020 | Agu | 7 | 65,9 | latih |
| 9 | 2020 | Sep | 8 | 51,5 | latih |
| 10 | 2020 | Okt | 9 | 213,2 | latih |
| 11 | 2020 | Nov | 10 | 281,9 | latih |
| 12 | 2020 | Des | 11 | 203,7 | latih |
| 13 | 2021 | Jan | 12 | 259,0 | latih |
| 14 | 2021 | Feb | 13 | 309,0 | latih |
| 15 | 2021 | Mar | 14 | 173,8 | latih |
| 16 | 2021 | Apr | 15 | 109,0 | latih |
| 17 | 2021 | Mei | 16 | 144,5 | latih |
| 18 | 2021 | Jun | 17 | 323,0 | latih |
| 19 | 2021 | Jul | 18 | 0,0 | latih |
| 20 | 2021 | Agu | 19 | 41,0 | latih |
| 21 | 2021 | Sep | 20 | 65,0 | latih |
| 22 | 2021 | Okt | 21 | 126,5 | latih |
| 23 | 2021 | Nov | 22 | 291,4 | latih |
| 24 | 2021 | Des | 23 | 344,0 | latih |
| 25 | 2022 | Jan | 24 | 212,0 | latih |
| 26 | 2022 | Feb | 25 | 281,0 | latih |
| 27 | 2022 | Mar | 26 | 213,0 | latih |
| 28 | 2022 | Apr | 27 | 220,0 | latih |
| 29 | 2022 | Mei | 28 | 199,0 | latih |
| 30 | 2022 | Jun | 29 | 134,0 | latih |
| 31 | 2022 | Jul | 30 | 10,0 | latih |
| 32 | 2022 | Agu | 31 | 130,0 | latih |
| 33 | 2022 | Sep | 32 | 64,0 | latih |
| 34 | 2022 | Okt | 33 | 395,0 | latih |
| 35 | 2022 | Nov | 34 | 431,0 | latih |
| 36 | 2022 | Des | 35 | 384,0 | latih |
| 37 | 2023 | Jan | 36 | 254,0 | latih |
| 38 | 2023 | Feb | 37 | 454,0 | latih |
| 39 | 2023 | Mar | 38 | 264,0 | latih |
| 40 | 2023 | Apr | 39 | 114,0 | latih |
| 41 | 2023 | Mei | 40 | 8,0 | latih |
| 42 | 2023 | Jun | 41 | 4,0 | latih |
| 43 | 2023 | Jul | 42 | 69,0 | latih |
| 44 | 2023 | Agu | 43 | 0,0 | latih |
| 45 | 2023 | Sep | 44 | 1,0 | latih |
| 46 | 2023 | Okt | 45 | 31,0 | latih |
| 47 | 2023 | Nov | 46 | 137,0 | latih |
| 48 | 2023 | Des | 47 | 303,0 | latih |
| 49 | 2024 | Jan | 48 | 134,8 | latih |
| 50 | 2024 | Feb | 49 | 199,9 | latih |
| 51 | 2024 | Mar | 50 | 209,0 | latih |
| 52 | 2024 | Apr | 51 | 320,9 | latih |
| 53 | 2024 | Mei | 52 | 3,2 | latih |
| 54 | 2024 | Jun | 53 | 10,5 | latih |
| 55 | 2024 | Jul | 54 | 23,9 | latih |
| 56 | 2024 | Agu | 55 | 4,7 | latih |
| 57 | 2024 | Sep | 56 | 17,2 | latih |
| 58 | 2024 | Okt | 57 | 22,9 | latih |
| 59 | 2024 | Nov | 58 | 189,2 | latih |
| 60 | 2024 | Des | 59 | 672,5 | latih |
| 61 | 2025 | Jan | 60 | 253,0 | uji |
| 62 | 2025 | Feb | 61 | 351,0 | uji |
| 63 | 2025 | Mar | 62 | 353,0 | uji |
| 64 | 2025 | Apr | 63 | 152,0 | uji |
| 65 | 2025 | Mei | 64 | 194,0 | uji |
| 66 | 2025 | Jun | 65 | 48,0 | uji |
| 67 | 2025 | Jul | 66 | 143,0 | uji |
| 68 | 2025 | Agu | 67 | 32,0 | uji |
| 69 | 2025 | Sep | 68 | 120,0 | uji |
| 70 | 2025 | Okt | 69 | 287,0 | uji |
| 71 | 2025 | Nov | 70 | 286,0 | uji |
| 72 | 2025 | Des | 71 | 198,0 | uji |

## Sumber tiap tahun
Edisi tahun N memuat data tahun N − 1. Halaman yang dipakai tersimpan sebagai PDF satu halaman di `Berkas/BPS/` (teksnya di `data_mentah/bps_halaman/`):

| Tahun data | PDF halaman BPS |
|---|---|
| 2020 | [[dda2021_hal78.pdf]] |
| 2021 | [[dda2022_hal84.pdf]] |
| 2022 | [[dda2023_hal79.pdf]] |
| 2023 | [[dda2024_hal80.pdf]], narasi "almost 0.00 mm": [[dda2024_hal69.pdf]] |
| 2024 | [[dda2025_hal73.pdf]] |
| 2025 | [[dda2026_hal73.pdf]] |

 Lihat [[Konsep Sumber Data BPS]] dan [[Bab III Metode Penelitian]] (3.3, Tabel 3.1).

Terkait: [[Catatan Kualitas Data]], [[Revisi BPS 2024]], [[Bab III Metode Penelitian]].
