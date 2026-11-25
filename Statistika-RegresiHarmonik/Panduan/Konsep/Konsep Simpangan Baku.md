---
tipe: panduan
tags: [statistika, regresi-harmonik, konsep]
---

# Konsep: Simpangan Baku

**Satu kalimat:** Simpangan baku mengukur seberapa jauh data umumnya berserakan dari rata-ratanya.

## Dua kelas, rata-rata sama
Kelas A nilainya: 70, 70, 70, 70. Kelas B: 40, 60, 80, 100. Rata-rata keduanya 70. Tetapi kelas A seragam (simpangan baku 0), kelas B berserakan (simpangan baku besar). Rata-rata saja tidak cukup; butuh ukuran sebaran.

## Cara hitung (contoh 2, 4, 6)
Lihat [[Konsep Varians Sampel]]: hasilnya 2. Artinya "rata-rata, angka-angka ini berjarak sekitar 2 dari mean".

## Mengapa n − 1
Data kita sampel, bukan seluruh hujan Mataram. Sampel cenderung tampak sedikit lebih seragam daripada populasinya, jadi pembaginya dikurangi satu untuk mengoreksi (koreksi Bessel). Lihat [[Konsep Populasi dan Sampel]].

## Pada data Mataram
- Seluruh 72 bulan: **135,35 mm**, dengan mean 174,80 mm.
- Simpangan baku hampir sebesar mean-nya. Artinya hujan antarbulan sangat beragam, dari 0 sampai 672,5 mm. Sebaran besar ini akibat pergantian musim, dan itulah yang ingin ditangkap model gelombang.
- Per tahun (sampel, n − 1): 2020 = 91,94; 2021 = 119,36; 2022 = 131,48; 2023 = 149,50; 2024 = 195,81; 2025 = 107,57. Tahun 2024 paling beragam karena ada Desember 672,5 mm.

Rumus di Excel: `STDEV`. Rujukan: Sudaryono (2021). Pemakaian simpangan baku pada data hujan Indonesia: Kotarumalos dkk. (2025) dan Syendra Wanti dkk. (2026). Dipakai di: [[Bab II Kajian Pustaka]] (2.3), [[Bab III Metode Penelitian]] (3.9). Kembali: [[00 Mulai Di Sini]].
