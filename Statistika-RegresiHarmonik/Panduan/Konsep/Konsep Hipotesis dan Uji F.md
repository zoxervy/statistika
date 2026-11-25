---
tipe: panduan
tags: [statistika, regresi-harmonik, konsep]
---

# Konsep: Hipotesis dan Uji F

**Satu kalimat:** Uji F memeriksa apakah gelombang musiman yang kita pasang benar-benar menjelaskan hujan, atau hanya kebetulan.

## Hipotesis
Hipotesis adalah dugaan yang diuji dengan data. Selalu ada dua:
- **H₀ (hipotesis nol):** b₁ = b₂ = 0. Artinya tidak ada gelombang musiman; hujan tidak bergantung pada bulan.
- **H₁:** paling sedikit satu dari b₁, b₂ tidak nol. Artinya ada gelombang musiman.

Seperti sidang: H₀ = terdakwa tidak bersalah, dan data harus cukup kuat sebelum H₀ ditolak.

## Taraf α = 0,05
Batas kesalahan yang kita relakan: 5 persen risiko menyimpulkan "ada pola" padahal sebenarnya tidak.

## Cara kerja uji F
F membandingkan dua hal:
- seberapa banyak naik-turun hujan yang dijelaskan gelombang, dengan
- seberapa banyak yang tersisa (galat).

Bentuknya: F = [ (jumlah kuadrat yang dijelaskan) ÷ 2 ] ÷ [ (jumlah kuadrat galat) ÷ (n − 3) ]. Angka 2 = jumlah koefisien yang diuji (b₁ dan b₂). n − 3 = 60 − 3 = 57. Jika gelombang menjelaskan banyak, F besar.

## Istilah yang dipakai saat memutuskan
- **Derajat bebas (2, 57):** dua angka yang menentukan baris dan kolom tabel F yang dibaca. Angka 2 = jumlah koefisien yang diuji (b₁, b₂). Angka 57 = 60 data latih dikurangi 3 angka yang ditaksir (b₀, b₁, b₂).
- **F kritis:** garis batas. Kalau sebenarnya tidak ada pola musiman, nilai F hanya melewati garis ini 5 kali dari 100 karena kebetulan. Untuk (2, 57) dan α = 0,05, garisnya ≈ **3,16** (dari tabel F, atau Excel `F.INV.RT(0,05; 2; 57)`).
- **Nilai-p:** peluang mendapat F setinggi itu (atau lebih) kalau sebenarnya tidak ada pola. Makin kecil, makin sulit menyebutnya kebetulan. Python dan Excel menampilkannya langsung (di Excel namanya *Significance F*).

## Cara memutuskan
- F lebih besar dari 3,16, atau nilai-p lebih kecil dari 0,05 (dua cara ini selalu memberi kesimpulan sama) → **H₀ ditolak**: ada pola musiman.
- Selain itu → H₀ tidak ditolak: belum cukup bukti adanya pola musiman.

## Mengapa uji F saja
Pertanyaannya cuma satu: ada pola musiman atau tidak. Sinus dan kosinus bekerja berpasangan untuk membentuk satu gelombang, jadi dinilai bersama. Uji t terpisah untuk tiap koefisien tidak perlu dan sudah dibuang. Bentuk hipotesis ini mengikuti Darmawan dkk. (2017) dan Purnama (2021); uji F dibaca dari keluaran regresi pada Azmi dkk. (2020).

## Yang tidak dibuktikan uji F
- Menolak H₀ **tidak** berarti ramalan akurat. Akurasi dinilai terpisah dengan RMSE dan MAE ([[Konsep RMSE dan MAE]]).
- Tidak menolak H₀ bukan bukti bahwa tidak ada pola, hanya bahwa buktinya belum cukup.

## Keterbatasan yang jujur
Uji F mengandaikan galat antarbulan saling bebas. Pada deret waktu, galat bulan berdekatan bisa berkaitan. Pemeriksaan itu (uji Ljung-Box) dibuang demi sederhana, jadi kalau dosen bertanya, akui sebagai keterbatasan, jangan diklaim sudah diperiksa.

## Perhatian
Nilai F dan nilai-p baru ada setelah analisis dijalankan. Laporan berhenti di Bab III dan tidak memuat angkanya.

Rujukan: Darmawan dkk. (2017) (statistik F berderajat bebas (2, n − 3) untuk pasangan koefisien kosinus dan sinus) dan Azmi dkk. (2020) (membaca Significance F dari keluaran regresi). Dipakai di: [[Bab II Kajian Pustaka]] (2.4), [[Bab III Metode Penelitian]] (3.9 langkah 3). Kembali: [[00 Mulai Di Sini]].
