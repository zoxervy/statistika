---
tipe: keputusan
status: "Final"
tags: [statistika, regresi-harmonik, konsul]
---

# Keputusan Ramal 2026 dan Dasar Penelitian

**Catatan Dosen / Pertimbangan:** arahan dosen pengampu kepada kelompok (dilaporkan kelompok, 25 Nov 2026): langsung meramal 2026, bukan memakai 2025 sebagai data uji. Kelompok memilih satu atau dua penelitian terdahulu sebagai dasar, lalu mengikuti atau melanjutkan penelitian itu dengan data yang berbeda.

**Keputusan:**
1. Seluruh 72 bulan (Januari 2020 sampai Desember 2025, t = 0 sampai 71) dipakai menaksir model. Tidak ada pembagian data latih dan data uji. Ramalan dibuat untuk Januari sampai Desember 2026 (t = 72 sampai 83).
2. Dasar penelitian ada dua. [[Kusdarwati 2023]] untuk alur metode: periode ulang dicari dulu, lalu model harmonik orde k dibentuk dan dinilai dengan plot data terhadap nilai duga. [[Astuti 2018]] adalah penelitian deret Fourier curah hujan Kota Mataram yang memprediksi tahun 2017; penelitian ini melanjutkannya dengan data BPS 2020–2025 dan meramal 2026.
3. Kecocokan model dinilai dengan R² dan RMSE pada 72 bulan data serta plot data terhadap nilai duga ([[Kotarumalos 2025]]: R² = 1 − SSE/SST; model dengan R² terbesar dan RMSE terkecil dianggap paling akurat). MAE dan dua ramalan pembanding (rata-rata data latih dan rata-rata per bulan kalender) dibuang.
4. Orde tetap k = 1. Kusdarwati (2023): daerah yang hanya memiliki satu periode ulang, misalnya satu tahun, dapat dimodelkan dengan harmonik orde satu. Uji F kini berderajat bebas (2, 69); F kritis α = 0,05 sekitar 3,13 (nilai tabel, bukan hasil).
5. Rumusan masalah dan tujuan tetap satu, ditambah "tahun 2026".

**Alasan memilih dua artikel ini:** keduanya sudah ada di Tabel 2.1 dan sudah dibaca dari PDF, jadi Daftar Pustaka tetap 22 entri dan Tabel 2.1 tetap 15 artikel. Kusdarwati (2023) menilai model tanpa data uji (plot nilai duga dan AIC), sesuai arahan dosen. Astuti dkk. (2018) meneliti kota yang sama.

**Akibat yang harus diakui:**
- R² dan RMSE mengukur kecocokan pada data 2020–2025, bukan akurasi ramalan 2026. Data aktual 2026 belum terbit.
- Desember 2024 (672,5 mm) di atas batas pencilan 590,0 mm. Nilai tetap dipakai dan dicatat sebagai keterbatasan di Bab III 3.5. Kusdarwati (2023) mencatat pencilan yang sangat besar dapat membuat parameter sinus dan kosinus tidak nyata (kasus Banyuwangi).
- Model hibrid harmonik, ARMA, dan pencilan seperti pada Kusdarwati (2023) tidak dipakai; laporan tetap berhenti di Bab III.

**Status:** Final. Vault sudah diubah (Abstrak, Bab I–III, Gambar 2.1, Alur, Data, Tabel 2.1, Panduan). Docx belum diubah dan menunggu perintah ([[Aturan Kerja]]).

**Terkait:** [[Bab I Pendahuluan]], [[Bab II Kajian Pustaka]], [[Bab III Metode Penelitian]], [[Gambar 2.1 Kerangka Pemikiran]], [[Alur Regresi Harmonik]].

Induk: [[Konsul 27 Okt 2026]]
