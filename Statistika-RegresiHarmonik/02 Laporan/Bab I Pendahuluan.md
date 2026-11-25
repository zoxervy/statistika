---
tipe: bab
tags: [statistika, regresi-harmonik, laporan]
---

# Bab I Pendahuluan

## 1.1 Latar Belakang (7 paragraf, [[K03 Latar belakang minimal tujuh paragraf]])

**Paragraf 1 (Dampak curah hujan):**  
Curah hujan adalah unsur iklim yang berpengaruh pada pertanian (Hadinata dkk., 2026), pengelolaan sumber daya air, dan risiko bencana hidrometeorologi (Aulia Putri dkk., 2026). Curah hujan tinggi dalam waktu lama dapat memicu banjir dan tanah longsor (Aulia Putri dkk., 2026), sedangkan musim kemarau yang panjang membuat wilayah rentan kekeringan (Aulia Putri dkk., 2026). Karena itu, gambaran dan perkiraan curah hujan bulanan diperlukan untuk perencanaan, mitigasi bencana, dan pengelolaan sumber daya air (Aulia Putri dkk., 2026).

**Paragraf 2 (Pola monsun di NTB dan Mataram):**  
Iklim Indonesia didominasi pola hujan monsunal (Kusdarwati, 2023; Tulak dkk., 2022), dengan musim hujan sekitar November sampai April dan kemarau sekitar Mei sampai Oktober (Permata dkk., 2024). Data Kota Mataram 2020–2025 menunjukkan pola yang sama: rata-rata November sampai April 260,5 mm, sedangkan Mei sampai Oktober 89,1 mm. Pola naik-turun ini berulang setiap tahun.

**Paragraf 3 (Kota Mataram dan sumber data BPS):**  
Kota Mataram adalah pusat kegiatan sosial dan ekonomi Provinsi Nusa Tenggara Barat, sehingga informasi curah hujan dibutuhkan untuk perencanaan wilayah (Hadinata dkk., 2026). Data curah hujan bulanan Kota Mataram tersedia secara terbuka pada publikasi tahunan *Kota Mataram dalam Angka* yang diterbitkan BPS dengan data asal BMKG. Data curah hujan bulanan dari BPS juga dipakai sebagai sumber data penelitian peramalan curah hujan di daerah lain (Kusdarwati, 2023; Purnama, 2021).

**Paragraf 4 (Deret waktu berpola periodik):**  
Data curah hujan bulanan adalah deret waktu, yaitu pengamatan yang berurutan menurut waktu. Analisis spektral pada curah hujan bulanan di Subang dan di satu kota di Jawa Barat menunjukkan pola yang berulang dengan periode sekitar 12 bulan, meskipun bentuk pola musimannya dapat berubah antarperiode (Susilokarti dkk., 2016; Darmawan dkk., 2017). Pola berulang seperti ini lebih tepat digambarkan dengan fungsi periodik daripada garis lurus terhadap waktu.

**Paragraf 5 (Regresi harmonik dan periode 12 bulan):**  
Regresi harmonik memodelkan pola periodik dengan fungsi sinus dan kosinus dari waktu, dan sudah dipakai pada data curah hujan Indonesia (Kusdarwati, 2023; Zega & Mardiningsih, 2025). Model ini menggambarkan puncak musim hujan dan lembah musim kemarau sebagai satu gelombang (Kusdarwati, 2023; Syendra Wanti dkk., 2026). Analisis spektral pada curah hujan Kota Bandung dan Kota Jayapura juga menemukan periode dominan sekitar 12 bulan (Habinuddin dkk., 2019; Tulak dkk., 2022), dan periodogram curah hujan bulanan tiga kota di Jawa Timur menunjukkan periode musiman satu tahun (Kusdarwati, 2023).

**Paragraf 6 (SARIMA dan regresi harmonik):**  
Model ARIMA musiman (SARIMA) banyak dipakai dalam peramalan curah hujan, antara lain oleh Purnama (2021) dan Aulia Putri dkk. (2026). Kusdarwati (2023) memodelkan komponen musiman lebih dulu dengan fungsi harmonik. Dibandingkan model SARIMA, regresi harmonik orde pertama (k = 1) hanya memerlukan tiga parameter, dapat ditafsirkan melalui amplitudo dan fase, serta menghasilkan kurva ramalan yang tetap mengikuti siklus tahunan (Kusdarwati, 2023; Zega & Mardiningsih, 2025).

**Paragraf 7 (Penelitian di Mataram dan posisi penelitian ini):**  
Penelitian curah hujan di Kota Mataram sebelumnya memakai LSTM dengan data harian BMKG (Hadinata dkk., 2026) dan regresi nonparametrik deret Fourier pada tiga stasiun untuk prediksi tahun 2017 (Astuti dkk., 2018). Penelitian ini memakai regresi harmonik parametrik univariat dengan estimasi *Ordinary Least Squares* (OLS) pada 72 data bulanan resmi BPS (2020–2025). Ramalannya diuji pada 12 bulan terakhir (tahun 2025) seperti pada Purnama (2021), lalu akurasinya diukur dengan RMSE dan MAE dan dibandingkan dengan ramalan sederhana. Laporan ini memuat Bab I sampai Bab III.

---

## 1.2 Rumusan Masalah ([[K04 Rumusan dan tujuan satu]])
Bagaimana hasil peramalan curah hujan bulanan Kota Mataram dengan model regresi harmonik?

## 1.3 Batasan Masalah
1. Lokasi hanya Kota Mataram, Provinsi Nusa Tenggara Barat.
2. Periode Januari 2020 sampai Desember 2025, 72 pengamatan bulanan.
3. Data sekunder dari publikasi BPS Kota Mataram (*Kota Mataram dalam Angka* edisi 2021–2026), tidak diunduh langsung dari portal BMKG.
4. Metode hanya regresi harmonik univariat; variabel meteorologi lain seperti suhu, tekanan udara, dan indeks ENSO tidak dimasukkan.
5. Data latih Januari 2020 sampai Desember 2024 (60 bulan), data uji 2025 (12 bulan).

## 1.4 Tujuan Penelitian ([[K04 Rumusan dan tujuan satu]])
Mengetahui hasil peramalan curah hujan bulanan Kota Mataram dengan model regresi harmonik.

## 1.5 Manfaat Penelitian
Memberi contoh penerapan regresi harmonik pada data curah hujan bulanan resmi, dari data mentah sampai pengujian ramalan, lengkap dengan sumber dan keterbatasan data, serta gambaran pola musiman curah hujan Kota Mataram (waktu puncak dan lembah, serta besar ayunannya) yang dapat dipakai untuk perencanaan pertanian dan kesiapsiagaan bencana.

Berikutnya: [[Bab II Kajian Pustaka]]
