---
tipe: pertanyaan
tags: [statistika, regresi-harmonik, tugas]
---

# Pertanyaan Terbuka dan Jawaban

Hanya pertanyaan yang berkaitan dengan data dan isi Bab I–III. Pertanyaan tentang hasil model diarsipkan di `arsip_di_luar_bab3/`.

1. **Tabel BPS menulis "Stasiun BMKG Lombok Barat". Apakah mewakili Kota Mataram?**
   Angka diambil dari publikasi resmi BPS Kota Mataram dan dipakai apa adanya. Lokasi alat tidak dapat dipastikan, sehingga ini dicatat sebagai keterbatasan di Subbab 3.5.

2. **Ada 0,00 mm padahal tercatat hari hujan (Juli 2021, Agustus 2023).**
   Angka dipertahankan sesuai sumber dan dicatat sebagai keterbatasan. Teks BPS edisi 2024 menyebut "almost 0.00 mm".

3. **Rata-rata 2024 direvisi BPS (150,73 → 166,82 mm).**
   Edisi 2026 hanya memuat rata-rata tahunan; data 12 bulan 2024 hanya tersedia di edisi 2025, jadi itu yang dipakai.

4. **(Selesai 1 Nov 2026) Wilks (2019): apakah benar memuat uji F untuk H₀: b₁ = b₂ = 0?**
   Tidak perlu dijawab: Wilks (2019) dilepas karena buku luar negeri, sedangkan kriteria proyek hanya penelitian Indonesia. Kutipannya diganti Kusdarwati (2023), Zega dan Mardiningsih (2025), Astuti dkk. (2018), Kotarumalos dkk. (2025), Darmawan dkk. (2017), dan Azmi dkk. (2020). Rincian: Wilks 2019, [[Riwayat Pekerjaan]] tahap 14.

5. **(Persiapan jawaban lisan) Uji F mengandaikan galat saling bebas. Bagaimana jika residual curah hujan bulanan berautokorelasi?**
   ADF dan Ljung-Box sudah dibuang (keputusan 31 Okt), jadi naskah tidak menguji autokorelasi residual. Jika ditanya dosen: ini diakui sebagai keterbatasan; bila residual berautokorelasi, nilai p uji F cenderung terlalu kecil. Kusdarwati (2023) memodelkan komponen harmonik lebih dulu, baru memeriksa autokorelasi residualnya; langkah itu bisa jadi lanjutan di luar Bab III. Belum perlu mengubah naskah kecuali dosen minta.

6. **(Persiapan jawaban lisan) Tanpa data uji, bagaimana tahu ramalan 2026 bagus?**
   Belum bisa diketahui sampai data 2026 terbit (*Kota Mataram dalam Angka 2027*). R² dan RMSE di Bab II 2.5 hanya menilai kecocokan pada 2020–2025. Ini sesuai arahan dosen ([[Keputusan Ramal 2026 dan Dasar Penelitian]]) dan sejalan dengan Kusdarwati (2023) yang menilai model dari plot nilai duga dan AIC tanpa data uji.

7. **(Persiapan jawaban lisan) Desember 2024 = 672,5 mm. Apakah merusak model?**
   Nilai itu di atas batas pencilan 590,0 mm dan tetap dipakai (Bab III 3.5). Satu pencilan menarik koefisien dan menaikkan RMSE. Kusdarwati (2023) menangani pencilan dengan model hibrid ARMA dan outlier; itu di luar lingkup Bab III.

Kembali: [[00 Peta Proyek]]
