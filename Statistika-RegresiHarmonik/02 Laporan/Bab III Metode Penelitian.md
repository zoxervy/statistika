---
tipe: bab
tags: [statistika, regresi-harmonik, laporan]
---

# Bab III Metode Penelitian

## 3.1 Jenis Penelitian
Penelitian kuantitatif dengan data sekunder deret waktu; analisisnya deskriptif (merangkum data) dan prediktif (memodelkan pola musiman dan meramalkan dengan regresi harmonik).

## 3.2 Lokasi dan Waktu Penelitian
Kota Mataram, Provinsi Nusa Tenggara Barat, data Januari 2020 sampai Desember 2025. Pengumpulan dan pengolahan data dilakukan pada Oktober 2026.

## 3.3 Metode Pengumpulan Data
Studi dokumen: kolom jumlah curah hujan (mm) pada Tabel 1.2.1 dibaca dari publikasi *Kota Mataram dalam Angka* edisi 2021 sampai 2026 (Badan Pusat Statistik Kota Mataram, 2021, 2022, 2023, 2024, 2025, 2026). Satu edisi memuat satu tahun, sehingga edisi N berisi data tahun N−1 (Tabel 3.1; tangkapan halaman pada Lampiran A). Data tidak diunduh dari portal data online BMKG karena unduhan dibatasi dua tahun per permintaan dan memerlukan akun.

**Tabel 3.1 Sumber data tiap tahun**

| Tahun data | Publikasi | Halaman PDF | Stasiun pada judul tabel |
|---|---|---|---|
| 2020 | Kota Mataram dalam Angka 2021 | 78 | BMKG Lombok Barat |
| 2021 | Kota Mataram dalam Angka 2022 | 84 | BMKG Lombok Barat |
| 2022 | Kota Mataram dalam Angka 2023 | 79 | BMKG Lombok Barat |
| 2023 | Kota Mataram dalam Angka 2024 | 80 | tidak disebut |
| 2024 | Kota Mataram dalam Angka 2025 | 73 | BMKG Lombok Barat |
| 2025 | Kota Mataram dalam Angka 2026 | 73 | BMKG Lombok Barat |

## 3.4 Populasi dan Sampel Penelitian
Populasi adalah seluruh curah hujan bulanan Kota Mataram sepanjang waktu. Sampel adalah curah hujan bulanan Januari 2020 sampai Desember 2025 (72 pengamatan), diambil seluruhnya karena semua bulan tersedia dan urutan waktu harus utuh.

## 3.5 Jenis dan Sumber Data
Data sekunder, kuantitatif, berskala rasio, dari publikasi resmi BPS Kota Mataram (data asal BMKG). Rata-rata 12 bulan hasil hitungan tiap tahun dicocokkan dengan baris "Kota Mataram" pada tabel BPS (selisih 0,01 mm pada 2024 karena pembulatan: 150,725 pada hitungan, 150,73 pada tabel), dan 72 nilai dicocokkan satu per satu dengan halaman PDF. Pemeriksaan ini mengurangi kemungkinan salah baca, tetapi tidak membuktikan bahwa angka BPS benar. Catatan atas data:
- Judul Tabel 1.2.1 edisi 2021, 2022, 2023, 2025, dan 2026 menyebut stasiun BMKG Lombok Barat; edisi 2024 tidak menyebut stasiun. Lokasi stasiun pengamatan tidak dapat dipastikan berada di dalam Kota Mataram.
- Nilai 0,00 mm pada Juli 2021 dan Agustus 2023 tercetak bersama 6 hari hujan dan 1 hari hujan. Teks bahasa Inggris edisi 2024 menulis "almost 0.00 mm" untuk Agustus 2023, sehingga diduga hujan di bawah batas ukur tercatat 0; salah cetak belum bisa dikesampingkan. Angka tidak diubah.
- Edisi 2026 mencatat rata-rata 2024 sebesar 166,82 mm (edisi 2025: 150,73 mm); data bulanan 2024 tetap dari edisi 2025 karena edisi 2026 tidak memuat rincian bulanannya.
- Presisi angka berbeda antaredisi, dan angka tidak diverifikasi silang ke portal BMKG.

## 3.6 Teknik dan Alat Pengolahan Data
Berkas PDF diubah ke teks dengan *pdftotext*, lalu 12 nilai tiap edisi disalin ke satu berkas CSV (72 baris) dan dicek dengan rata-rata tahunan. Statistik deskriptif dihitung di Microsoft Excel (Lampiran B); regresi harmonik dan uji F dihitung dengan Python 3 (pandas, SciPy, statsmodels, matplotlib).

## 3.7 Identifikasi dan Klasifikasi Variabel
Variabel terikat adalah curah hujan bulanan ($Y_t$), kuantitatif kontinu berskala rasio. Variabel bebasnya dibentuk dari waktu $t$, yaitu $\sin(2\pi t/12)$ dan $\cos(2\pi t/12)$.

Pola musiman curah hujan Indonesia digerakkan oleh monsun, yang membagi tahun menjadi musim hujan November sampai April dan kemarau Mei sampai Oktober (Kusdarwati, 2023; Tulak dkk., 2022; Permata dkk., 2024). Variabilitas antartahun curah hujan monsun Indonesia dipengaruhi pula oleh fenomena global seperti *El Niño-Southern Oscillation* (ENSO) (Kusdarwati, 2023; Aulia Putri dkk., 2026). Faktor itu tidak dimasukkan ke model.

## 3.8 Definisi Operasional Variabel
Curah hujan bulanan adalah jumlah curah hujan satu bulan kalender yang dicatat BMKG dan dimuat pada kolom "Jumlah Curah Hujan" Tabel 1.2.1 publikasi *Kota Mataram dalam Angka*, dalam milimeter (mm).

## 3.9 Teknik Analisis Data dan Uji Hipotesis
1. Mengelompokkan 72 data ke matriks tahun × bulan.
2. Menghitung mean, median, modus, dan simpangan baku sampel ($n-1$), per tahun dan seluruh data.
3. Membentuk $X_{1t} = \sin(2\pi t/12)$ dan $X_{2t} = \cos(2\pi t/12)$ dengan $t = 0$ pada Januari 2020, menaksir $b_0, b_1, b_2$ dengan OLS pada 60 bulan data latih, lalu menguji pengaruh gelombang tahunan dengan uji F: $H_0: b_1 = b_2 = 0$ (tidak ada pola musiman) melawan $H_1$: paling sedikit satu dari $b_1$, $b_2$ tidak nol (ada pola musiman), dengan $\alpha = 0{,}05$.
4. Meramal 12 bulan tahun 2025, menghitung RMSE dan MAE terhadap data aktual, lalu membandingkannya dengan ramalan rata-rata data latih dan rata-rata per bulan kalender. Data dibagi menurut urutan waktu.

Bentuk hipotesis pada langkah 3 mengikuti Darmawan dkk. (2017) dan Purnama (2021), dan uji F dari keluaran regresi mengikuti Azmi dkk. (2020). Pengujian ramalan pada 12 bulan terakhir mengikuti Purnama (2021) dan RMSE sebagai ukuran akurasi mengikuti Permata dkk. (2024) dan Hadinata dkk. (2026).
