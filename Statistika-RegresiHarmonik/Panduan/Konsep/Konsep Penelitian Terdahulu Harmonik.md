---
tipe: panduan
tags: [statistika, regresi-harmonik, konsep]
---

# Konsep: Penelitian Terdahulu (Tabel 2.1)

**Satu kalimat:** 15 artikel Indonesia tahun 2016–2026 yang menunjukkan bahwa hujan punya siklus sekitar 12 bulan dan bahwa deret Fourier/harmonik sudah dipakai untuk menggambarkannya.

## Untuk apa tabel ini
Dosen minta tabel minimal 15 artikel dengan rujukan tahun 2016 ke atas. Fungsinya: menunjukkan apa yang sudah dikerjakan orang lain dan di mana penelitian kita berbeda. Isi tiap artikel diambil dari abstrak resminya; angka tambahan hanya dari PDF artikel.

## Empat kelompok

**1. Regresi deret Fourier atau harmonik (5)**
- Astuti dkk. (2018): Kota Mataram, tiga stasiun, regresi nonparametrik Fourier.
- Kusdarwati (2023): tiga kota Jawa Timur, harmonik plus ARMA.
- Anandari dkk. (2022): Jawa Barat, Fourier dengan prediktor cuaca.
- Syendra Wanti dkk. (2026): Kota Bengkulu, Fourier.
- Kotarumalos dkk. (2025): Kota Ambon, Fourier dan Spline.

**2. Analisis spektral atau periodogram (6)**
Mencari periode dominan data. Susilokarti dkk. (2016, Subang); Darmawan dkk. (2017, Jawa Barat); Tulak dkk. (2022, Jayapura); Zega dan Mardiningsih (2025, Serdang Bedagai); Habinuddin dkk. (2019, Bandung); Purnama (2021, Parigi Moutong).

**3. Mataram dan NTB, metode lain (3)**
Hadinata dkk. (2026, LSTM data harian Mataram); Aulia Putri dkk. (2026, SARIMA vs AMBP untuk NTB); Azmi dkk. (2020, ARDL hari hujan NTB). Azmi dkk. ditulis bersama dosen pengampu, Siti Soraya, M.Si.

**4. Pembagian musim dan kriteria RMSE (1)**
Permata dkk. (2024): enam pos di Surabaya; model dipilih lewat RMSE terkecil.

5 + 6 + 3 + 1 = 15. Karena Astuti (2018) juga berlokasi di Mataram, artikel yang berlokasi di Mataram atau NTB berjumlah empat.

## Yang bisa disimpulkan
- Periode dominan sekitar 12 bulan muncul di banyak kota (Subang, Jayapura, Bandung, Serdang Bedagai, tiga kota Jawa Timur).
- Komponen harmonik atau Fourier sudah dipakai pada hujan Indonesia, termasuk Mataram dan Ambon.
- Sebagian besar studi peramalan memakai SARIMA atau pembelajaran mesin.

## Perbedaan penelitian kita
Data bulanan resmi BPS Kota Mataram enam tahun; regresi harmonik k = 1 dengan tiga parameter yang ditafsirkan lewat amplitudo dan fase; ramalan diuji pada 12 bulan 2025 terhadap tebakan sederhana. Kalimat aman: "model harmonik parametrik univariat pada data bulanan BPS Kota Mataram belum kami temukan". Jangan menulis "belum pernah ada".

## Hati-hati
- Baris Zega dan Aulia Putri menyebut ADF atau stasioneritas. Itu isi artikel mereka, bukan metode kita.
- Purnama dan Darmawan memakai uji periodogram. Jangan menulis mereka memakai uji F.

Daftar lengkap: [[Tabel 2.1 Penelitian Terdahulu]]. Dipakai di: [[Bab II Kajian Pustaka]] (2.6). Kembali: [[00 Mulai Di Sini]].
