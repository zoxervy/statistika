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
- R² dihitung pada **data latih**. Itu mengukur seberapa cocok kurva dengan data yang dipakai membuatnya, bukan seberapa akurat ramalan 2025. Akurasi ramalan dinilai dengan RMSE dan MAE ([[Konsep RMSE dan MAE]]).
- Tidak ada angka R² yang otomatis "bagus". Penelitian terdahulu melaporkan R² sangat berbeda (mis. 61,2% pada Bengkulu dan 97,30% pada Jawa Barat) karena data dan modelnya berbeda; jangan dibandingkan mentah-mentah.

## Perhatian
R² model kita baru ada setelah analisis dijalankan dan tidak dimuat di laporan (berhenti di Bab III). R² belum menjadi bagian dari rencana analisis Bab III 3.9; kalau dosen meminta, bisa ditambahkan dari keluaran regresi yang sama.

Terkait: [[Konsep Varians Sampel]]. Kembali: [[00 Mulai Di Sini]].
