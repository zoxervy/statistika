---
tipe: panduan
tags: [statistika, regresi-harmonik, konsep]
---

# Konsep: Sumber Data BPS dan Aturan Edisi

**Satu kalimat:** Data diambil dari buku tahunan BPS *Kota Mataram dalam Angka* (Tabel 1.2.1), yang menyalin pengamatan BMKG.

## Siapa BPS dan BMKG
- **BMKG** (Badan Meteorologi, Klimatologi, dan Geofisika) mengukur hujan lewat stasiun.
- **BPS** (Badan Pusat Statistik) menerbitkan angka itu dalam buku tahunan per kota.

## Aturan edisi: buku N berisi tahun N−1
Buku terbit setelah tahun datanya selesai. Karena itu:

| Buku | Berisi tahun | Halaman PDF |
|---|---|---|
| Dalam Angka 2021 | 2020 | 78 |
| Dalam Angka 2022 | 2021 | 84 |
| Dalam Angka 2023 | 2022 | 79 |
| Dalam Angka 2024 | 2023 | 80 |
| Dalam Angka 2025 | 2024 | 73 |
| Dalam Angka 2026 | 2025 | 73 |

Salah paham umum: mengira "buku 2021 = data 2021". Salah; itu data 2020.

## Mengapa bukan portal BMKG
1. Portal BMKG daring membatasi unduhan dua tahun per permintaan dan perlu akun. Kita butuh enam tahun.
2. Buku BPS terbuka, bisa diperiksa siapa saja.
3. Peneliti lain juga memakai hujan dari buku BPS (Kusdarwati, 2023; Purnama, 2021).

## Cara data dipindahkan dan diperiksa
1. PDF diubah ke teks dengan *pdftotext*.
2. 12 nilai tiap edisi disalin ke satu CSV (72 baris).
3. Rata-rata 12 bulan tiap tahun dibandingkan dengan baris "Kota Mataram" di tabel BPS: 155,12; 182,18; 222,75; 136,58; 150,73; 201,42 untuk 2020–2025. Semua cocok; selisih terbesar 0,005 mm pada 2024 karena pembulatan.
4. 72 nilai dicocokkan satu per satu dengan halaman PDF.

## Berkas yang disimpan
PDF penuh enam buku (±50 MB) sudah dihapus. Yang disimpan: tujuh halaman yang dipakai (PDF di `Berkas/BPS/`, teksnya di `data_mentah/bps_halaman/`) dan teks penuh tiap buku. Kalau perlu halaman lain, unduh ulang dari tautan di Daftar Pustaka.

Batasnya: pemeriksaan ini hanya membuktikan salinan kami benar, bukan bahwa angka BPS sendiri benar.

Dipakai di: [[Bab III Metode Penelitian]] (3.3, 3.5), [[Data BPS 72 Bulan]]. Kembali: [[00 Mulai Di Sini]].
