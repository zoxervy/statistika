---
tipe: panduan
tags: [statistika, regresi-harmonik, panduan]
---

# Panduan 01: Sampul, Abstrak, Kata Pengantar

Naskah asli: [[Abstrak dan Kata Pengantar]]. Prasyarat: [[00 Mulai Di Sini]].

## Sampul
- **Judul:** Analisis Curah Hujan Bulanan Kota Mataram Tahun 2020–2025 dan Peramalan dengan Model Regresi Harmonik.
- **Dosen pengampu:** Siti Soraya, M.Si.
- **Anggota:** Ahmad Yusuf, Gracia Yusti Euaggelion, Raudhatul Athfal. NIM: [[NIM Anggota (lokal)]].
- **Kampus:** S1 Ilmu Komputer, Fakultas Teknik, Universitas Bumigora.

Cara membaca judul: "Analisis" = bagian deskriptif (merangkum 72 angka). "Peramalan" = bagian menebak 2026. "Regresi Harmonik" = alat tebaknya.

## Abstrak
Abstrak adalah ringkasan satu halaman supaya pembaca tahu isi laporan tanpa membaca semuanya. Dosen minta **empat paragraf**, dan abstrak **terpisah** dari kata pengantar ([[K01 Abstrak dan Kata Pengantar dipisah]], [[K02 Abstrak empat paragraf]]).

### Paragraf 1: latar belakang
- **Isi:** Rata-rata Desember 350,9 mm, Juli 43,2 mm. Dampak ke pertanian, air, banjir, kekeringan.
- **Artinya:** Hujan di Mataram sangat tidak merata antarbulan, dan itu penting bagi banyak orang.
- **Alasan:** Dua angka itu memperlihatkan jaraknya (sekitar 8 kali lipat) sehingga alasan butuh model terasa nyata. Keduanya dihitung dari 6 nilai Desember dan 6 nilai Juli di data.

### Paragraf 2: tujuan
- **Isi:** Mengetahui hasil peramalan curah hujan bulanan Kota Mataram tahun 2026 dengan model regresi harmonik.
- **Artinya:** Satu pertanyaan saja: berapa tebakan model gelombang ini untuk tiap bulan 2026, dan seberapa cocok model itu dengan data yang ada.
- **Alasan:** Dosen minta rumusan dan tujuan masing-masing satu ([[K04 Rumusan dan tujuan satu]]). Kalimat tujuan sengaja sama dengan rumusan masalah di Bab I.

### Paragraf 3: metode
- **Isi:** 72 data, semuanya dipakai menyusun model; statistik deskriptif; variabel sinus dan kosinus periode 12 bulan; OLS dengan uji F; R² dan RMSE; ramalan 12 bulan 2026.
- **Artinya:** Urutan kerja dalam satu kalimat panjang. Detail tiap langkah ada di Bab III.
- **Alasan:** Tidak menyebut uji lain (ADF, Ljung-Box, uji t) karena sudah dibuang demi sederhana ([[Konsep Estimasi OLS]], [[Konsep Hipotesis dan Uji F]]).

### Paragraf 4: rencana hasil
- **Isi:** Laporan ini memuat Bab I–III. Hasil yang akan diperoleh: persamaan, amplitudo, fase, R², RMSE, dan ramalan 2026.
- **Artinya:** Jujur bahwa angka hasil belum ada di laporan ini.
- **Alasan:** Laporan berhenti di Bab III, jadi paragraf ini berbentuk rencana, bukan hasil. Jangan diubah menjadi kalimat berisi angka hasil.

**Kata kunci:** curah hujan, Kota Mataram, deret waktu, regresi harmonik, deret Fourier, RMSE. Fungsinya untuk pencarian dokumen.

## Kata Pengantar
- **Isi:** Syukur, nama laporan, kampus; isi tiga bab; seluruh data dari BMKG lewat BPS dan tidak ada angka yang diisi atau diperkirakan sendiri; keanehan data dicatat di Bab III; terima kasih ke dosen.
- **Alasan:** Kalimat "tidak ada angka diisi sendiri" adalah janji yang harus benar. Sudah dicek: 72 nilai dicocokkan satu per satu dengan halaman PDF BPS.

## Kalau ditanya dosen
- *Kenapa abstrak tidak ada angka hasil?* Karena laporan baru sampai Bab III; hasil akan dilaporkan setelah analisis dijalankan.
- *Data dari mana?* Buku BPS Kota Mataram dalam Angka 2021–2026, yang datanya berasal dari BMKG.

Berikutnya: [[02 Bab I Pendahuluan]]
