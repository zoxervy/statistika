---
tipe: gambar
tags: [statistika, regresi-harmonik, laporan]
---

# Gambar 2.1 Kerangka Pemikiran

Alur konseptual pemodelan regresi harmonik univariat. Versi gambar di PDF dibuat ulang oleh `build/buat_docx.py` dengan alur yang sama tetapi lebih ringkas (5 kotak: data; pembagian latih/uji; statistik deskriptif; sin/cos, OLS, dan uji F; ramalan 2025 dengan RMSE dan MAE). Diagram di bawah memecah alur itu lebih rinci:

```mermaid
flowchart TD
    D72["Data Sekunder BPS 72 Bulan (2020-2025)"] --> SPLIT["Pembagian Partisi Temporal"]
    SPLIT --> TR["Data Latih 60 Bulan (2020-2024)"]
    SPLIT --> TE["Data Uji 12 Bulan (2025)"]
    
    TR --> DESK["Statistik Deskriptif"]
    DESK --> FEAT["Variabel Sin dan Cos (periode 12 bulan)"]
    FEAT --> OLS["Estimasi OLS dan Uji F"]
    OLS --> FCAST["Peramalan Out-Sample 12 Bulan (Tahun 2025)"]
    
    TE --> EVAL["Evaluasi Kinerja Ramalan"]
    FCAST --> EVAL
    EVAL --> METRIC["RMSE dan MAE terhadap ramalan sederhana"]
```

**Keterangan Gambar 2.1:**  
Kerangka pemikiran penelitian peramalan curah hujan bulanan Kota Mataram menggunakan Regresi Harmonik.  
*Sumber:* Diadaptasi dari alur Purnama (2021) dan Kusdarwati (2023).

Terkait: [[Bab II Kajian Pustaka]] (2.7), [[K08 Sumber gambar kerangka pikir]], [[Alur Regresi Harmonik]].
