---
tipe: artikel
tags: [statistika, regresi-harmonik, artikel]
---

# Susilokarti 2016

**Rujukan (APA 7):** Susilokarti, D., Arif, S. S., Susanto, S., & Sutiarso, L. (2016). Analisis spektral dalam penentuan periodisitas siklus curah hujan di wilayah selatan Jatiluhur, Kabupaten Subang, Jawa Barat. *agriTECH*, *36*(1), 89–95. https://doi.org/10.22146/agritech.10688
**Berkas PDF:** [[Susilokarti 2016.pdf]] (di `Berkas/Artikel/`)

| Data | Metode | Hasil |
|---|---|---|
| Selatan Jatiluhur, Subang; curah hujan bulanan 1975–2012 | Fast Fourier Transform (analisis spektral) | Pola curah hujan berulang setiap 12 bulan (puncak periodogram 11,97) |

**Peran untuk penelitian ini:** Dasar periode T = 12 bulan pada curah hujan bulanan.

*Isi diringkas dari abstrak resmi artikel (https://doi.org/10.22146/agritech.10688), lalu dicocokkan dengan teks penuh hasil OCR (1 Nov 2026; teks di [[Susilokarti 2016 (OCR).txt]]).*

**Hasil pengecekan teks penuh (OCR, 7 halaman, hlm. 89–95):**
- Cocok: data bulanan 1975–2012 dari 10 stasiun; periodogram FFT, kekuatan kerapatan spektral tertinggi 11,97, dibulatkan 12 bulan per siklus; pola satu puncak per tahun dipengaruhi angin monsun (Kesimpulan, hlm. 94–95).
- Tidak cocok dengan abstrak: abstrak menulis MSE validasi 14,92 (tingkat kepercayaan 95%), tetapi isi artikel menulis MSE 0,0129 (validasi), 0,0116 (testing), dan 0,07 (prediksi, Gambar 5). Angka 14,92 hanya ada di abstrak. Karena itu angka MSE **tidak dipakai** di Tabel 2.1; yang dipakai adalah puncak periodogram 11,97 ≈ 12 bulan.
- Tambahan: jaringan saraf tiruan (ANN backpropagation 1-20-1) dipakai untuk prediksi, lalu FFT pada galat ANN menunjukkan siklus 71,68 bulan (sekitar 5–6 tahun). Dua temuan inilah yang mendukung kalimat Bab II 2.2 bahwa bentuk pola musiman dapat berubah antarperiode (bersama Darmawan dkk., 2017).
- Teks juga menyebut bahwa di Koto Tabang, Padang Panjang, dan Sicincin pola berosilasi sekitar 12 bulan, sedangkan Bandung punya siklus 6 bulan yang kuat (mengutip penelitian lain).

Naik ke: [[Tabel 2.1 Penelitian Terdahulu]]
