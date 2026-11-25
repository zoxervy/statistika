---
tipe: panduan
tags: [statistika, regresi-harmonik, konsep]
---

# Konsep: Data Latih dan Data Uji

**Satu kalimat:** Data latih dipakai untuk membuat rumus; data uji disimpan dulu lalu dipakai untuk memeriksa rumus itu pada data yang belum pernah dilihat.

## Analogi ujian
Latihan soal = data latih. Ujian dengan soal baru = data uji. Kalau soal ujian sudah dipakai berlatih, nilainya tidak membuktikan apa-apa.

## Pembagian di penelitian ini
| Bagian | Bulan | Jumlah | Nomor t |
|---|---|---|---|
| Data latih | Januari 2020–Desember 2024 | 60 | 0 sampai 59 |
| Data uji | Januari 2025–Desember 2025 | 12 | 60 sampai 71 |

Pembagian menurut **urutan waktu**, tidak diacak ([[Konsep Deret Waktu dan Pola Musiman]]).

## Apa yang dilakukan pada tiap bagian
- Data latih: mencari b₀, b₁, b₂ (OLS) dan menguji gelombang dengan uji F.
- Data uji: **tidak ikut** pencarian itu. Setelah rumus jadi, masukkan t = 60 sampai 71 untuk mendapat 12 ramalan, lalu bandingkan dengan 12 hujan sebenarnya.

## Mengapa 12 bulan
12 bulan = satu putaran musim penuh (hujan, peralihan, kemarau, kembali ke hujan). Penelitian lain juga menguji pada 12 bulan terakhir (Purnama, 2021).

## Batas yang harus diakui
Hanya satu tahun uji, jadi hasilnya bisa dipengaruhi kebetulan tahun itu. Kalau 2025 tidak biasa, hasil uji tidak mewakili tahun-tahun lain. Ini keterbatasan, bukan kesalahan.

Rujukan: Purnama (2021). Dipakai di: [[Bab II Kajian Pustaka]] (2.5), [[Bab III Metode Penelitian]] (3.9). Kembali: [[00 Mulai Di Sini]].
