---
tipe: panduan
tags: [statistika, regresi-harmonik, konsep]
---

# Konsep: Varians Sampel

**Satu kalimat:** Varians adalah rata-rata kuadrat jarak data dari mean (pembagi n − 1 untuk sampel); simpangan baku adalah akar varians.

## Hitung langkah demi langkah
Data: 2, 4, 6. Mean = 4.
1. Selisih dari mean: −2, 0, 2.
2. Kuadratkan (supaya minus tidak menghapus plus): 4, 0, 4.
3. Jumlahkan: 8.
4. Bagi n − 1 = 2: varians = **4**.
5. Akar: simpangan baku = **2**.

Rumus: s² = Σ(xᵢ − x̄)² / (n − 1) dan s = √s².

## Pada data kita
Varians sampel 72 data = 18.318,84 mm². Satuannya mm² (kuadrat), sehingga sulit dibayangkan; karena itu yang dilaporkan akarnya (simpangan baku, 135,35 mm) yang satuannya kembali mm.

## Apakah wajib?
Tidak. Varians bukan variabel penelitian. Ia bekerja di belakang layar: pada R² ([[Konsep R-Squared dan Goodness of Fit]]) dan pada uji F ([[Konsep Hipotesis dan Uji F]]), yang membandingkan jumlah kuadrat galat. Belum ditampilkan di laporan atau Excel; tambahkan hanya bila dosen meminta (baris `=VAR(...)` di sheet Ringkasan, rumus di Bab II 2.3).

Terkait: [[Konsep Simpangan Baku]], [[Konsep Populasi dan Sampel]]. Kembali: [[00 Mulai Di Sini]].
