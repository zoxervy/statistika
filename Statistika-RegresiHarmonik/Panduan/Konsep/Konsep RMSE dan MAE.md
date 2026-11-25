---
tipe: panduan
tags: [statistika, regresi-harmonik, konsep]
---

# Konsep: RMSE dan MAE

**Satu kalimat:** Dua ukuran seberapa jauh ramalan meleset dari kenyataan, dalam satuan yang sama dengan data (mm).

## Contoh rekaan, tiga bulan
| Bulan | Sebenarnya (A) | Ramalan (F) | Selisih A − F |
|---|---|---|---|
| 1 | 100 | 110 | −10 |
| 2 | 200 | 190 | 10 |
| 3 | 300 | 340 | −40 |

**MAE** (rata-rata selisih tanpa tanda):
(10 + 10 + 40) ÷ 3 = **20**. Rata-rata meleset 20 mm.

**RMSE** (kuadratkan, rata-ratakan, akarkan):
Kuadrat: 100, 100, 1600 → rata-rata 600 → akar ≈ **24,49**.

## Mengapa RMSE lebih besar
RMSE mengkuadratkan selisih dulu, sehingga satu meleset besar (−40) menarik nilainya naik. RMSE selalu lebih besar atau sama dengan MAE. Kalau RMSE jauh di atas MAE, ada beberapa bulan yang melesetnya besar. Pada hujan Mataram, bulan-bulan puncak hujan sulit ditebak, sehingga RMSE cenderung lebih tinggi daripada MAE. Itu wajar.

## Cara membaca
Makin kecil makin baik. Satuannya mm, jadi bisa dibayangkan: "rata-rata meleset sekian mm per bulan". Tidak ada batas baku untuk "bagus"; nilainya bermakna ketika dibandingkan dengan tebakan sederhana ([[Konsep Baseline Ramalan Rata-rata]]).

## Rumus (Bab II 2.5)
RMSE = √( Σ(A_t − F_t)² / m ) dan MAE = Σ|A_t − F_t| / m, dengan m = 12 bulan data uji.

## Perhatian
Nilai RMSE dan MAE model kita baru ada setelah analisis dijalankan dan tidak dimuat di laporan.

Rujukan: Permata dkk. (2024); Hadinata dkk. (2026); Purnama (2021) untuk penilaian pada 12 bulan data uji. Dipakai di: [[Bab II Kajian Pustaka]] (2.5), [[Bab III Metode Penelitian]] (3.9 langkah 4). Kembali: [[00 Mulai Di Sini]].
