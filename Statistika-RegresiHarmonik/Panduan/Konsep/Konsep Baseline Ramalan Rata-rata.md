---
tipe: panduan
tags: [statistika, regresi-harmonik, konsep]
---

# Konsep: Baseline (Tebakan Orang Malas)

**Satu kalimat:** Baseline adalah pembanding paling sederhana; model yang rumit hanya berguna kalau mengalahkannya.

## Mengapa perlu
RMSE 80 mm terdengar besar atau kecil? Tidak ada yang tahu tanpa pembanding. Pembandingnya adalah tebakan yang tidak butuh model sama sekali.

## Dua pembanding di Bab III 3.9 langkah 4
1. **Rata-rata seluruh data latih.** Semua 12 bulan 2025 ditebak dengan satu angka yang sama: rata-rata 60 bulan 2020–2024. Tebakan paling malas; mengabaikan musim.
2. **Rata-rata tiap bulan kalender pada data latih.** Januari 2025 ditebak dengan rata-rata lima Januari (2020–2024), Februari 2025 dengan rata-rata lima Februari, dan seterusnya. Tebakan ini sudah menghormati musim, tanpa gelombang.

## Cara menilai
Hitung RMSE dan MAE untuk model harmonik, pembanding 1, dan pembanding 2 pada 12 bulan 2025. Model dianggap lebih baik jika nilainya lebih kecil.

## Sikap jujur
Pembanding 2 bukan lawan enteng. Ia memakai 12 angka (satu per bulan), sedangkan model harmonik hanya 3 angka. Bisa saja pembanding 2 menang atau seri. Kalau begitu, nilai model harmonik ada pada ringkasnya (3 parameter) dan kemudahan menafsirkan amplitudo-fase, bukan pada akurasi. Jangan menjanjikan bahwa model harmonik pasti menang.

Hasil perbandingan belum ada di laporan (berhenti di Bab III).

Rujukan: Purnama (2021); Hadinata dkk. (2026). Dipakai di: [[Bab II Kajian Pustaka]] (2.5), [[Bab III Metode Penelitian]] (3.9). Terkait: [[Konsep RMSE dan MAE]]. Kembali: [[00 Mulai Di Sini]].
