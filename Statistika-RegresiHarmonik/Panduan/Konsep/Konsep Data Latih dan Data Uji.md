---
tipe: panduan
tags: [statistika, regresi-harmonik, konsep]
---

# Konsep: Data Latih dan Data Uji (tidak dipakai lagi)

**Satu kalimat:** Data latih dipakai membuat rumus dan data uji disimpan untuk memeriksa rumus itu. Sejak 25 Nov 2026 penelitian ini tidak membagi data: seluruh 72 bulan dipakai membuat rumus, lalu rumus langsung meramal 2026 ([[Keputusan Ramal 2026 dan Dasar Penelitian]]).

## Analogi ujian
Latihan soal = data latih. Ujian dengan soal baru = data uji. Rencana lama menyimpan hujan 2025 sebagai soal ujian. Dosen meminta semua soal dipakai untuk berlatih, lalu menebak soal tahun depan (2026) yang jawabannya belum ada.

## Pemakaian data sekarang
| Bagian | Bulan | Jumlah | Nomor t |
|---|---|---|---|
| Data untuk membuat rumus | Januari 2020–Desember 2025 | 72 | 0 sampai 71 |
| Ramalan | Januari 2026–Desember 2026 | 12 | 72 sampai 83 |

## Akibatnya
- R² dan RMSE dihitung dari 72 bulan yang sama dengan yang dipakai membuat rumus. Angka itu mengukur **kecocokan**, bukan akurasi ramalan ([[Konsep R-Squared dan Goodness of Fit]], [[Konsep RMSE dan MAE]]).
- Akurasi ramalan 2026 baru bisa dicek setelah BPS menerbitkan *Kota Mataram dalam Angka 2027*, yang memuat data 2026.
- Cara ini sama dengan penelitian dasar Kusdarwati (2023), yang menilai model dari plot data terhadap nilai duga dan AIC, tanpa data uji.

## Kalau ditanya dosen atau teman
*Kenapa tidak disisakan data uji?* Arahan dosen: langsung meramal 2026. Keterbatasannya ditulis terus terang di Bab II 2.5.

Dulu dipakai di: [[Bab II Kajian Pustaka]] (2.5) dan [[Bab III Metode Penelitian]] (3.9) dengan rujukan Purnama (2021). Kembali: [[00 Mulai Di Sini]].
