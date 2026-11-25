---
tipe: panduan
tags: [statistika, regresi-harmonik, konsep]
---

# Konsep: R-Squared (R²)

**Satu kalimat:** R² menunjukkan berapa bagian naik-turunnya hujan yang berhasil dijelaskan oleh model gelombang.

## Cara membaca
R² bernilai 0 sampai 1.
- Dekat 0: gelombang hampir tidak menjelaskan apa-apa.
- Dekat 1: gelombang menjelaskan hampir semuanya.

Rumus: R² = 1 − SSE/SST.
- **SST:** total naik-turun data terhadap rata-ratanya (jumlah kuadrat selisih data dari mean).
- **SSE:** sisa naik-turun yang tidak terjelaskan model (jumlah kuadrat galat).

## Contoh rekaan
Misalkan SST = 100 dan SSE = 40. Maka R² = 1 − 40/100 = 0,6. Artinya 60 persen naik-turun data dijelaskan model, dan 40 persen sisanya adalah variasi antartahun dan faktor lain yang tidak dimodelkan (mis. El Niño, [[Konsep Monsun dan El Nino]]).

## Dua batas penting
- R² dihitung pada **72 bulan yang dipakai membuat model**. Itu mengukur seberapa cocok kurva dengan data itu, bukan seberapa akurat ramalan 2026. Ramalan 2026 baru bisa dinilai setelah data 2026 terbit.
- Tidak ada angka R² yang otomatis "bagus". Penelitian terdahulu melaporkan R² sangat berbeda (mis. 61,2% pada Bengkulu dan 97,30% pada Jawa Barat) karena data dan modelnya berbeda; jangan dibandingkan mentah-mentah.

## Dipakai di laporan
Sejak 25 Nov 2026, R² menjadi ukuran kecocokan di Bab II 2.5 dan Bab III 3.9 langkah 4, bersama RMSE ([[Keputusan Ramal 2026 dan Dasar Penelitian]]). Rumus dan kriterianya mengikuti Kotarumalos dkk. (2025): model dengan R² terbesar dan RMSE terkecil dianggap paling akurat. Astuti dkk. (2018) juga memakai R² untuk memilih model deret Fourier hujan Kota Mataram.

Nilai R² model kita baru ada setelah analisis dijalankan dan tidak dimuat di laporan (berhenti di Bab III).

Terkait: [[Konsep Varians Sampel]]. Kembali: [[00 Mulai Di Sini]].
