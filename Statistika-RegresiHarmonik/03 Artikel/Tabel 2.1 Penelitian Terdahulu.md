---
tipe: indeks
tags: [statistika, regresi-harmonik, artikel]
---

# Tabel 2.1 Penelitian Terdahulu

15 artikel, seluruhnya penelitian di Indonesia dan terbit 2016–2026. Kolom Data, Metode, dan Hasil diringkas dari abstrak resmi masing-masing artikel; rincian jumlah data Hadinata, Purnama, hasil ADF Aulia Putri, dan R² serta AIC Kotarumalos dari abstrak atau isi PDF artikel (Hadinata, Purnama, Aulia Putri ditandai di catatannya).

| No | Artikel | Data | Metode | Hasil |
|---|---|---|---|---|
| 1 | [[Astuti 2018]] | Kota Mataram, tiga stasiun (Selaparang, Ampenan, Cakranegara); prediksi tahun 2017 | Regresi nonparametrik deret Fourier, pemilihan jumlah knot dengan GCV | Model terbaik: 101, 101, dan 106 knot; R² 0,959; 0,967; dan 0,988 |
| 2 | [[Kusdarwati 2023]] | Curah hujan bulanan Surabaya, Malang, dan Banyuwangi | Periodogram; model hibrid harmonik + ARMA + outlier aditif | Periode musiman 1 tahun (monsun). Surabaya: harmonik orde 2; Malang dan Banyuwangi: harmonik orde 1 |
| 3 | [[Anandari 2022]] | Curah hujan bulanan Jawa Barat 2015–2019; prediktor kelembapan, tekanan, angin, suhu | Regresi nonparametrik deret Fourier, estimasi OLS, pemilihan K dengan GCV | K = 13; GCV 549,92; MSE 462,09; R² 97,30% |
| 4 | [[Syendra Wanti 2026]] | Kota Bengkulu 2021–2025, stasiun Meteorologi dan Klimatologi | Regresi nonparametrik deret Fourier; GCV, MSE, MAPE, R² | Osilasi terbaik K = 5; R² 61,2% dan 60,9%; MAPE 52,2% dan 74,09% |
| 5 | [[Susilokarti 2016]] | Selatan Jatiluhur, Subang; curah hujan bulanan 1975–2012 | Fast Fourier Transform (analisis spektral) | Pola curah hujan berulang setiap 12 bulan (puncak periodogram 11,97) |
| 6 | [[Darmawan 2017]] | Deret curah hujan satu kota di Jawa Barat | Periodogram standar (R) | Curah hujan berpola musiman (umumnya periode 12); pola musiman berubah antarperiode |
| 7 | [[Tulak 2022]] | Kota Jayapura, bulanan dan dasarian | Fast Fourier Transform dan analisis statistik | Periode dominan 11,63 ≈ 12 bulan; curah hujan ekstrem terjadi hampir setiap bulan |
| 8 | [[Zega 2025]] | Curah hujan bulanan Kab. Serdang Bedagai, Januari 2014–Desember 2023 (120 data) | Analisis harmonik (pendekatan Fourier), periodogram; uji stasioneritas Phillips-Perron | Frekuensi dominan 0,524, setara periode 12 bulan; ada pola musiman |
| 9 | [[Habinuddin 2019]] | Kota Bandung, Januari 2006–Desember 2015 | Periodogram (analisis spektral), lalu SARIMA | Periode 12 bulan; model SARIMA(0,1,1)(0,1,1)12; maksimum Desember, minimum Agustus |
| 10 | [[Purnama 2021]] | Kab. Parigi Moutong, 82 bulan (Jan 2014–Okt 2020); latih 70, uji 12 | Regresi spektral untuk cek musiman, lalu SARIMA | SARIMA(1,1,0)(0,1,1)12; MAPE latih 12,02%, uji 16,46% |
| 11 | [[Kotarumalos 2025]] | Curah hujan bulanan Kota Ambon, Januari 2020–Desember 2024; prediktor suhu, kelembapan, kecepatan angin, tekanan udara | Regresi nonparametrik Spline Truncated dan deret Fourier; knot dengan GCV, jumlah harmonik dengan AIC | Fourier dua harmonik terbaik: R² 0,5719, AIC 820,8226; kelembapan, tekanan udara, dan sinus(2) berpengaruh signifikan |
| 12 | [[Hadinata 2026]] | Kota Mataram, harian BMKG 2019–2023 (1.824 data) | LSTM multivariat (suhu, kelembapan, angin, tekanan) | MAE 4,020 mm; RMSE 7,915 mm pada data uji |
| 13 | [[Aulia Putri 2026]] | NTB, bulanan NASA POWER 1981–2025; 8 blok, latih 120 bulan, ramal 12 bulan | SARIMA vs AMBP; uji ADF | Stasioner pada level (ADF p = 8,91 × 10⁻⁷); SARIMA lebih stabil (RRMSE 49,18%, R² 68,13%) |
| 14 | [[Azmi 2020]] | Jumlah hari hujan NTB 2006–2010 | Autoregressive Distributed Lag (ARDL) | Prediksi 2011: 226 hari hujan; dievaluasi MAD, MSE, RMSE, MAPE |
| 15 | [[Permata 2024]] | Curah hujan harian enam pos Surabaya | ARIMAX (variabel musiman) dan SVR | Model terbaik dipilih dari RMSE terkecil; hujan dominan Januari–April dan November–Desember |

## Pengelompokan
- **Regresi deret Fourier / harmonik (5):** Astuti dkk. (2018); Kusdarwati (2023); Anandari dkk. (2022); Syendra Wanti dkk. (2026); Kotarumalos dkk. (2025)
- **Analisis spektral / periodogram (6):** Susilokarti dkk. (2016); Darmawan dkk. (2017); Tulak dkk. (2022); Zega & Mardiningsih (2025); Habinuddin dkk. (2019); Purnama (2021)
- **Wilayah Mataram dan NTB dengan metode lain (3):** Hadinata dkk. (2026); Aulia Putri dkk. (2026); Azmi dkk. (2020)
- **Musim dan kriteria evaluasi (1):** Permata dkk. (2024)

Tiap artikel masuk satu kelompok menurut metode utamanya (5 + 6 + 3 + 1 = 15). Astuti dkk. (2018) juga berlokasi di Kota Mataram, sehingga artikel berlokasi di Kota Mataram atau NTB berjumlah empat (Astuti, Hadinata, Aulia Putri, Azmi).

## Yang dapat disimpulkan dari tabel
- Periode dominan sekitar 12 bulan dilaporkan di Subang, Jayapura, Bandung, Serdang Bedagai, dan tiga kota di Jawa Timur (Susilokarti dkk., 2016; Tulak dkk., 2022; Habinuddin dkk., 2019; Zega & Mardiningsih, 2025; Kusdarwati, 2023).
- Komponen harmonik/Fourier sudah dipakai pada curah hujan Indonesia, termasuk Kota Mataram (Astuti dkk., 2018; Kusdarwati, 2023) dan Kota Ambon (Kotarumalos dkk., 2025).
- Sebagian besar studi peramalan memakai SARIMA atau model mesin; model harmonik parametrik univariat pada data bulanan BPS Kota Mataram belum ditemukan.

## Pembeda penelitian ini
1. Data: 72 bulan publikasi resmi BPS Kota Mataram (2020–2025).
2. Model: regresi harmonik k = 1 (3 parameter, OLS), dengan amplitudo dan fase sebagai interpretasi.
3. Evaluasi: uji 12 bulan tahun 2025 terhadap pembanding rata-rata data latih.

Diganti saat audit 30 Okt 2026: Sudibyakto (2016) dan Wahyuni dkk. (2016); alasan di [[Artikel Tidak Dipakai]]. Diganti 31 Okt 2026: Bimaprawira & Rejeki (2021) dan Pratiwi dkk. (2020) oleh Zega & Mardiningsih (2025) dan Kotarumalos dkk. (2025).


Dipakai di: [[Bab II Kajian Pustaka]] (2.6), [[Bab I Pendahuluan]]. Keputusan: [[K05 Penelitian terdahulu jadi tabel minimal 15 artikel]]
