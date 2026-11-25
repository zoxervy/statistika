---
tipe: panduan
tags: [statistika, regresi-harmonik, panduan]
---

# Panduan 02: Bab I Pendahuluan

Naskah asli: [[Bab I Pendahuluan]]. Prasyarat: [[00 Mulai Di Sini]].

Bab I menjawab satu pertanyaan: **kenapa penelitian ini perlu dilakukan?** Dosen minta latar belakang minimal 7 paragraf, rumusan masalah 1, tujuan 1 ([[K03 Latar belakang minimal tujuh paragraf]], [[K04 Rumusan dan tujuan satu]]). Susunannya dari luas ke sempit: hujan secara umum, lalu Mataram, lalu metode, lalu celah penelitian.

## 1.1 Latar belakang, paragraf demi paragraf

### Paragraf 1: hujan itu penting
- **Isi:** Hujan memengaruhi pertanian, air, dan bencana. Hujan deras lama memicu banjir dan longsor; hujan sangat sedikit lama memicu kekeringan. Karena itu perkiraan hujan bulanan diperlukan.
- **Artinya:** Orang butuh tahu kapan hujan banyak dan kapan sedikit, untuk bercocok tanam dan bersiap bencana.
- **Alasan:** Pembuka harus menunjukkan masalahnya nyata. Sumber: Hadinata dkk. (2026) untuk pertanian; Aulia Putri dkk. (2026) untuk sumber daya air, banjir, longsor, dan kekeringan (sudah dicek ke teks aslinya).

### Paragraf 2: pola monsun
- **Isi:** Iklim Indonesia didominasi hujan monsunal: musim hujan sekitar November–April, kemarau Mei–Oktober. Data Mataram 2020–2025 cocok: rata-rata Nov–Apr 260,5 mm, Mei–Okt 89,1 mm.
- **Artinya:** Angin musiman membuat hujan naik-turun mengikuti kalender. Angka kita membuktikan itu juga terjadi di Mataram.
- **Cara angka itu muncul:** Nov–Apr terdiri dari 36 data (6 tahun × 6 bulan), dirata-ratakan = 260,52. Mei–Okt 36 data = 89,07. Rasionya sekitar 2,9 banding 1.
- **Alasan:** Kalimat tentang pola dipasangkan dengan angka sendiri, jadi pembaca melihat teori dan data selaras. Klaim khusus NTB sudah dihapus karena sumbernya tidak mendukung. Lihat [[Konsep Monsun dan El Nino]].

### Paragraf 3: Mataram dan sumber data
- **Isi:** Mataram adalah pusat sosial-ekonomi NTB. Datanya terbuka di buku BPS (asal BMKG). Peneliti lain juga memakai data hujan dari buku BPS (Kusdarwati, 2023; Purnama, 2021).
- **Artinya:** Data kami sah, mudah diperiksa siapa saja, dan ada contoh peneliti lain yang memakai sumber serupa.
- **Alasan:** Dosen bisa menanyakan "datanya dari mana". Jawaban disiapkan di sini dan dirinci di Bab III. Lihat [[Konsep Sumber Data BPS]].

### Paragraf 4: deret waktu berpola berulang
- **Isi:** Data hujan bulanan adalah deret waktu. Analisis spektral di Subang dan satu kota di Jawa Barat menemukan pola berulang tiap sekitar 12 bulan. Pola begini lebih cocok digambar dengan fungsi periodik daripada garis lurus.
- **Artinya:** Kalau dilihat dari waktu ke waktu, hujan seperti ombak yang kembali ke bentuk semula tiap tahun. Garis lurus tidak bisa menggambar ombak.
- **Alasan:** Paragraf ini menjembatani "ada pola 12 bulan" menuju "pakai gelombang". Sumber: Susilokarti dkk. (2016), Darmawan dkk. (2017). Lihat [[Konsep Deret Waktu dan Pola Musiman]].

### Paragraf 5: regresi harmonik
- **Isi:** Regresi harmonik memodelkan pola periodik dengan sinus dan kosinus, sudah dipakai pada data curah hujan Indonesia (Kusdarwati, 2023; Zega dan Mardiningsih, 2025). Puncak musim hujan dan lembah kemarau digambar sebagai satu gelombang. Periode sekitar 12 bulan juga ditemukan di Bandung, Jayapura, dan tiga kota Jawa Timur.
- **Artinya:** Gelombang sinus-kosinus adalah alat bawaan untuk menggambar ombak. Peneliti lain di kota lain sudah menemukan periode yang sama.
- **Alasan:** Memperkuat bahwa metode ini wajar dipakai, bukan ide asal-asalan. Lihat [[Konsep Regresi Harmonik dan Gelombang Sinus Kosinus]].

### Paragraf 6: kenapa tidak SARIMA
- **Isi:** SARIMA banyak dipakai untuk meramal hujan, antara lain oleh Purnama (2021) dan Aulia Putri dkk. (2026). Kusdarwati (2023) memodelkan pola musiman dulu dengan fungsi harmonik, baru memeriksa sisanya. Dibandingkan model SARIMA, regresi harmonik orde pertama hanya butuh tiga parameter, bisa ditafsirkan lewat amplitudo dan fase, dan kurvanya tetap mengikuti siklus tahunan (Kusdarwati, 2023; Zega & Mardiningsih, 2025).
- **Artinya:** SARIMA adalah model peramalan yang menebak bulan ini dari bulan-bulan sebelumnya, dengan banyak angka pengatur. Model rumit tidak otomatis lebih baik. Untuk data musiman, tiga angka sudah cukup untuk menggambar siklus.
- **Alasan:** Menjelaskan pilihan metode. Kata "banyak dipakai" dan nama Purnama (2021), Aulia Putri dkk. (2026) dipakai agar tidak mengklaim "paling sering". Kusdarwati dan Zega menjadi sumber bahwa model harmonik memang dipakai dengan cara ini.
- **Hati-hati:** jangan bilang SARIMA "lebih buruk". Yang tertulis hanya bahwa model kita lebih sederhana (tiga parameter). Klaim "ramalan SARIMA cenderung konstan" dibuang karena sumbernya (Aulia dkk., 2019) dilepas.

### Paragraf 7: celah penelitian
- **Isi:** Penelitian hujan di Mataram sebelumnya memakai LSTM data harian (Hadinata dkk., 2026) dan regresi nonparametrik deret Fourier tiga stasiun (Astuti dkk., 2018). Kami memakai regresi harmonik parametrik univariat, OLS, 72 data bulanan BPS, diuji pada 2025 dengan RMSE dan MAE.
- **Artinya:** Orang sudah meneliti hujan Mataram, tetapi dengan cara lain. Kami mengerjakan versi sederhana dengan data resmi bulanan.
- **Alasan:** Bab I wajib menunjukkan "apa bedanya penelitian ini". *Parametrik* = bentuk rumus ditentukan dulu (sinus-kosinus), tinggal cari angkanya. *Nonparametrik* = bentuk rumus dibiarkan mengikuti data. *Univariat* = hanya satu variabel (curah hujan).

## 1.2 Rumusan masalah
**"Bagaimana hasil peramalan curah hujan bulanan Kota Mataram dengan model regresi harmonik?"** Satu pertanyaan.

## 1.3 Batasan masalah
Lima batas: (1) hanya Kota Mataram; (2) Januari 2020–Desember 2025, 72 bulan; (3) data sekunder dari buku BPS, bukan unduhan langsung BMKG; (4) hanya regresi harmonik, tanpa suhu atau ENSO; (5) 60 bulan latih, 12 bulan uji. Batasan melindungi dari pertanyaan "kenapa tidak pakai X".

## 1.4 Tujuan
Satu kalimat, sama dengan rumusan, diubah ke bentuk pernyataan: mengetahui hasil peramalan curah hujan bulanan Kota Mataram dengan model regresi harmonik.

## 1.5 Manfaat
Dua manfaat: contoh penerapan regresi harmonik dari data mentah sampai uji ramalan (lengkap dengan sumber dan keterbatasan), dan gambaran pola musiman (kapan puncak dan lembah, seberapa besar ayunan) untuk perencanaan pertanian dan kesiapsiagaan bencana.

## Kalau ditanya dosen
- *Kenapa regresi harmonik?* Hujan berpola 12 bulan; sinus-kosinus adalah alat paling sederhana untuk pola berulang; hanya tiga parameter.
- *Apa bedanya dengan penelitian sebelumnya?* Data bulanan resmi BPS Kota Mataram enam tahun, model parametrik k = 1 yang bisa ditafsirkan, diuji pada 12 bulan terakhir.
- *Apa batasannya?* Satu variabel saja; faktor seperti El Niño tidak dimasukkan.

Berikutnya: [[03 Bab II Kajian Pustaka]]
