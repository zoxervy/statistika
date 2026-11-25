---
tipe: panduan
tags: [statistika, regresi-harmonik, konsep]
---

# Konsep: Deret Waktu dan Pola Musiman

**Satu kalimat:** Deret waktu adalah data yang dicatat berurutan menurut waktu; pola musiman adalah naik-turun yang berulang pada jadwal yang sama tiap tahun.

## Deret waktu
Contoh bukan deret waktu: nilai ujian 30 mahasiswa (urutannya tidak berarti). Contoh deret waktu: hujan Januari 2020, Februari 2020, Maret 2020, dan seterusnya (urutan berarti, karena bulan ini dipengaruhi musim yang sedang berjalan). Definisi: Habinuddin dkk. (2019); Zega dan Mardiningsih (2025).

## Mengapa urutan tidak boleh diacak
Nomor t harus mengikuti bulan yang sebenarnya, karena t yang diubah menjadi sinus dan kosinus. Kalau Januari 2021 diberi nomor milik Juli, gelombangnya ikut bergeser. Ramalan 2026 dibuat dengan melanjutkan nomor itu (t = 72 sampai 83), jadi hanya memakai informasi dari 2020–2025 ([[Konsep Data Latih dan Data Uji]]).

## Pola musiman pada data kita
Rata-rata tiap bulan kalender dari enam tahun (mm):

| Jan | Feb | Mar | Apr | Mei | Jun | Jul | Agu | Sep | Okt | Nov | Des |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 215,8 | 291,0 | 247,7 | 188,3 | 120,4 | 92,9 | 43,2 | 45,6 | 53,1 | 179,3 | 269,4 | 350,9 |

Terbaca: naik dari Oktober, puncak sekitar Desember–Februari, turun ke titik terendah Juli–Agustus, lalu naik lagi. Satu putaran = 12 bulan. Itulah **periode 12 bulan**.

## Pola tidak mulus tiap tahun
Bulan terbasah dan terkering tiap tahun tidak selalu sama:

| Tahun | Bulan terbasah | Bulan terkering |
|---|---|---|
| 2020 | November | Juli |
| 2021 | Desember | Juli (0,0 mm) |
| 2022 | November | Juli |
| 2023 | Februari | Agustus (0,0 mm) |
| 2024 | Desember (672,5 mm) | Mei |
| 2025 | Maret | Agustus |

Jadi puncak bergeser antar tahun. Model gelombang menangkap pola **rata-rata**, bukan pola persis tiap tahun. Sisa yang tidak tertangkap ada di suku galat ε dan sebagian menjelaskan mengapa ramalan tidak akan tepat.

Dipakai di: [[Bab II Kajian Pustaka]] (2.2), [[Bab III Metode Penelitian]] (3.1). Kembali: [[00 Mulai Di Sini]].
