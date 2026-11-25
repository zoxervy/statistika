---
tipe: artikel
tags: [statistika, regresi-harmonik, artikel]
---

# Kusdarwati 2023

**Rujukan (APA 7):** Kusdarwati, H. (2023). Model hibrid harmonik, ARMA dan outlier curah hujan di Surabaya, Malang dan Banyuwangi. *Jurnal Statistika dan Aplikasinya*, *7*(1), 14–25. https://doi.org/10.21009/jsa.07102
**Berkas PDF:** [[Kusdarwati 2023.pdf]] (di `Berkas/Artikel/`)

| Data | Metode | Hasil |
|---|---|---|
| Curah hujan bulanan Surabaya, Malang, dan Banyuwangi | Periodogram; model hibrid harmonik + ARMA + outlier aditif | Periode musiman 1 tahun (monsun). Surabaya: harmonik orde 2; Malang dan Banyuwangi: harmonik orde 1 |

**Peran untuk penelitian ini:** Model harmonik sebagai komponen musiman deterministik; residual diperiksa autokorelasinya.

**Dasar penelitian (sejak 25 Nov 2026, [[Keputusan Ramal 2026 dan Dasar Penelitian]]).** Dibaca dari teks PDF:
- Data: curah hujan bulanan Surabaya dan Banyuwangi dari situs BMKG; Malang Januari 2015 sampai Desember 2020 dari BPS Malang.
- Langkah: (1) analisis periodesitas dengan periodogram, (2) model harmonik orde k sesuai banyaknya periodesitas yang nyata, (3) ARMA dan pencilan AO pada sisaan, (4) penggabungan. Diolah dengan RStudio.
- Pendahuluan: "Jika suatu daerah hanya memiliki satu periodesitas misalkan periode ulang 1 tahun maka pemodelan curah hujan dapat dimodelkan dengan harmonik orde satu." Dipakai untuk alasan k = 1 (Bab II 2.4).
- Penilaian tanpa data uji: plot kesesuaian data curah hujan dan nilai duga (Gambar 8, Surabaya: model "sudah dapat menjangkau nilai curah hujan rendah tetapi belum mampu menjangkau nilai curah hujan yang tinggi") dan perbandingan AIC dengan SARIMA (Tabel 3).
- Banyuwangi: parameter cos dan sin "tidak nyata karena pengaruh outlier yang sangat besar". Dipakai untuk catatan pencilan Desember 2024 (Bab III 3.5).
- Yang diikuti penelitian ini: periode 12 bulan, harmonik orde satu, dan plot nilai duga. Yang tidak diikuti: ARMA, pencilan AO, AIC.

*Isi diringkas dari abstrak resmi artikel (https://doi.org/10.21009/jsa.07102).*

Naik ke: [[Tabel 2.1 Penelitian Terdahulu]]
