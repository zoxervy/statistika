---
tipe: panduan
tags: [statistika, regresi-harmonik, konsep]
---

# Konsep: Estimasi OLS (Kuadrat Terkecil)

**Satu kalimat:** OLS adalah cara mencari b₀, b₁, b₂ yang membuat kurva paling dekat ke titik-titik data, dengan "dekat" diukur lewat jumlah kuadrat selisih.

## Bayangkan menarik tali melewati titik-titik
Ada 60 titik hujan. Kita memasang satu kurva gelombang dan menggeser-gesernya (mengubah b₀, b₁, b₂). Untuk tiap titik, ukur selisihnya dengan kurva (galat). Kuadratkan, jumlahkan. Pilih b yang jumlahnya paling kecil.

## Contoh kecil
Tiga titik data: 10, 12, 20. Coba dua tebakan "garis tengah":
- Tebakan 12: selisih −2, 0, 8 → kuadrat 4, 0, 64 → jumlah **68**.
- Tebakan 14: selisih −4, −2, 6 → kuadrat 16, 4, 36 → jumlah **56**.
- Tebakan 14,0 ternyata yang terkecil (rata-rata data = 14).

OLS melakukan hal yang sama dengan tiga angka sekaligus, tetapi menghitungnya langsung dengan rumus (tidak coba-coba).

## Mengapa dikuadratkan
Supaya selisih positif dan negatif tidak saling menghapus, dan supaya selisih besar dihukum lebih berat daripada selisih kecil.

## Dipakai pada bagian mana
- Pada **seluruh 72 bulan** (2020–2025), sesuai arahan dosen ([[Keputusan Ramal 2026 dan Dasar Penelitian]]).
- Dikerjakan di Python (statsmodels). Excel Bab III hanya memuat data dan statistik deskriptif, tidak memuat regresi.
- Setelah b ditemukan, tahap berikutnya adalah menguji apakah gelombangnya nyata ([[Konsep Hipotesis dan Uji F]]) dan meramal 2026.

Rujukan: Astuti dkk. (2018) (Kota Mataram, estimasi OLS pada regresi deret Fourier) dan Kotarumalos dkk. (2025). Dipakai di: [[Bab II Kajian Pustaka]] (2.4), [[Bab III Metode Penelitian]] (3.9 langkah 3). Kembali: [[00 Mulai Di Sini]].
