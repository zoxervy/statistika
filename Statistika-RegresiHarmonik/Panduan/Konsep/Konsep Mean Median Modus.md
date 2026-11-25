---
tipe: panduan
tags: [statistika, regresi-harmonik, konsep]
---

# Konsep: Mean, Median, Modus

**Satu kalimat:** Tiga cara memilih satu angka yang mewakili sekumpulan data.

## Contoh kecil dulu
Lima angka: 10, 20, 20, 30, 120.
- **Mean** (rata-rata) = jumlah ÷ banyak = 200 ÷ 5 = **40**.
- **Median** (nilai tengah) = urutkan, ambil yang di tengah = **20**.
- **Modus** (paling sering muncul) = **20** (muncul dua kali).

Mean (40) jauh di atas median (20) karena ada angka besar (120) yang menariknya ke atas. Jadi: **kalau ada angka ekstrem, median lebih jujur menggambarkan data yang biasa.**

## Pada 72 bulan hujan Mataram
- **Mean = 174,80 mm.** Jumlah 72 angka dibagi 72.
- **Median = 173,70 mm.** Karena 72 genap, nilai tengah = rata-rata nilai ke-36 (173,6) dan ke-37 (173,8).
- **Modus = 0,0 mm.** Hampir semua angka berbeda; hanya 0,0 yang muncul dua kali (Juli 2021 dan Agustus 2023). Modus di sini tidak banyak berarti. Di Excel, tahun yang tidak punya angka berulang tertulis "Tidak ada".
- Mean (174,80) dan median (173,70) hampir sama: data secara keseluruhan tidak berat sebelah.

## Per tahun (contoh pentingnya median)
Tahun 2024: mean 150,73 mm, median hanya 79,35 mm. Selisih besar karena Desember 2024 (672,5 mm) menaikkan rata-rata. Maka laporan menampilkan dua-duanya.

## Rumus
Mean: x̄ = Σxᵢ / n. Rujukan: Sudaryono (2021). Median dan modus tidak ditemukan di artikel Tabel 2.1 mana pun, jadi definisinya hanya bersandar pada Sudaryono (dan hitungan sendiri dari data). Di Excel: `AVERAGE`, `MEDIAN`, `MODE`.

Dipakai di: [[Bab II Kajian Pustaka]] (2.3), [[Bab III Metode Penelitian]] (3.9 langkah 2). Kembali: [[00 Mulai Di Sini]].
