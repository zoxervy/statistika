---
tipe: panduan
tags: [statistika, regresi-harmonik, konsep]
---

# Konsep: RMSE (MAE tidak dipakai lagi)

**Satu kalimat:** RMSE adalah ukuran seberapa jauh kurva model meleset dari data, dalam satuan yang sama dengan data (mm).

Sejak 25 Nov 2026, RMSE dihitung pada 72 bulan yang dipakai membuat model, bersama R² ([[Keputusan Ramal 2026 dan Dasar Penelitian]]). MAE dan perbandingan dengan tebakan sederhana dibuang.

## Contoh rekaan, tiga bulan
| Bulan | Data (Y) | Nilai duga model (Ŷ) | Selisih Y − Ŷ |
|---|---|---|---|
| 1 | 100 | 110 | −10 |
| 2 | 200 | 190 | 10 |
| 3 | 300 | 340 | −40 |

**RMSE** (kuadratkan, rata-ratakan, akarkan):
Kuadrat: 100, 100, 1600 → rata-rata 600 → akar ≈ **24,49**. Kurva rata-rata meleset sekitar 24 mm.

Selisih −40 menarik RMSE naik karena dikuadratkan dulu. Pada hujan Mataram, bulan puncak hujan biasanya paling sulit diikuti gelombang, jadi bulan-bulan itulah yang paling menaikkan RMSE.

## Cara membaca
Makin kecil makin baik. Tidak ada batas baku untuk "bagus". Kotarumalos dkk. (2025) memakai RMSE kecil bersama R² besar sebagai tanda model paling akurat menggambarkan pola hujan.

## Rumus (Bab II 2.5)
RMSE = √( Σ(Y_t − Ŷ_t)² / n ), dengan n = 72 bulan.

## Batas
RMSE ini mengukur kecocokan pada data 2020–2025. Akurasi ramalan 2026 belum bisa diukur ([[Konsep Data Latih dan Data Uji]]).

## Kenapa MAE dibuang
MAE (rata-rata selisih tanpa tanda) dulu dipakai bersama RMSE untuk menilai ramalan 2025. Setelah data uji ditiadakan, satu ukuran meleset (RMSE) cukup, sesuai Kotarumalos dkk. (2025) dan Permata dkk. (2024).

## Perhatian
Nilai RMSE model kita baru ada setelah analisis dijalankan dan tidak dimuat di laporan.

Rujukan: Kotarumalos dkk. (2025); Permata dkk. (2024). Dipakai di: [[Bab II Kajian Pustaka]] (2.5), [[Bab III Metode Penelitian]] (3.9 langkah 4). Kembali: [[00 Mulai Di Sini]].
