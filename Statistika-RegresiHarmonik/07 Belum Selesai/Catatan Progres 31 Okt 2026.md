---
tipe: progres
tags: [statistika, regresi-harmonik, tugas]
---

# Catatan Progres 31 Okt 2026

Rekam keputusan dan temuan sesi ini. Urutan kerja lengkap: [[Riwayat Pekerjaan]]. Tidak ada PDF/docx yang dibangun ulang ([[Aturan Kerja]]).

## 1. Lingkup dipotong sampai Bab III
- Bab IV, Bab V, hasil model, dan bahan presentasi dipindah ke `arsip_di_luar_bab3/` (di luar vault, tidak dihapus).
- Angka hasil model dihapus dari Panduan, Konsep, Peta, kanvas, dan Keputusan Metode.
- Folder `05 Data dan Hasil` diganti nama jadi `05 Data`.
- Skrip pembuat laporan disalin ke `build/` ([[README]]).

## 2. Perbaikan isi (31 Okt)
Bab I par. 1, 2, 6; Bab II 2.1 dan 2.6; rata-rata 2024 = 150,73; entri BPS tanpa penerbit; audit Aulia (2019), Khikmah & Sofro (2025), Mulsandi (2024). Rincian di [[Log Verifikasi]].

## 3. Penggantian dua artikel di Tabel 2.1 (pilihan A)
| Dikeluarkan | Alasan | Pengganti |
|---|---|---|
| Bimaprawira & Rejeki (2021) | PDF tidak bisa diunduh; abstrak tidak melaporkan periode 12 bulan | [[Zega 2025]] |
| Pratiwi dkk. (2020) | PDF tidak bisa diunduh; PCR dengan prediktor suhu muka laut, jauh dari metode | [[Kotarumalos 2025]] |

- Susilokarti (2016) tetap: PDF teksnya rusak karena font, tetapi abstrak dan metadata terverifikasi Crossref.
- Pengelompokan Tabel 2.1 sekarang 5 Fourier/harmonik + 6 spektral + 3 Mataram/NTB metode lain + 1 musim = 15. Artikel berlokasi di Kota Mataram atau NTB: 4 (Astuti, Hadinata, Aulia Putri, Azmi).
- Daftar Pustaka 27 entri pada tahap ini (jadi 26 setelah Wei dilepas, bagian 6).
- Bab III 3.7 tidak lagi mengutip Bimaprawira. Bab II 2.6 sudah disamakan; skripnya kini `build/buat_docx.py` (bagian 7).
- Catatan: DOI Kotarumalos yang tercetak di artikel (`10.63822/8wxe0007`) belum aktif saat dicek; rujukan memakai tautan halaman artikel. Cek ulang sebelum dikumpulkan.

## 4. Temuan uji hipotesis pada artikel (bahan keputusan Bab III 3.9)
Dibaca dari PDF penuh. Koreksi atas rekap lisan sebelumnya ditandai (koreksi).

| Artikel | Uji yang dipakai |
|---|---|
| Purnama (2021) | Hipotesis musiman tertulis (H₀: α = β = 0; H₁: α ≠ 0 atau β ≠ 0; α = 0,05) dengan uji periodogram; ADF; uji Portmanteau untuk white noise (koreksi: bukan disebut Ljung-Box) |
| Darmawan (2017) | Hipotesis sama seperti Purnama, uji periodogram (rasio ordinat maksimum) |
| Zega & Mardiningsih (2025) | Phillips-Perron (H₀ akar unit); uji Fisher pada periodogram, T = 0,2053 > 0,1132, H₀ ditolak |
| Azmi (2020) | Membaca "Significance F" dari keluaran regresi Excel, dibandingkan dengan taraf nyata |
| Anandari (2022) | Uji signifikansi parameter simultan dan parsial, lalu uji asumsi error; tidak menyebut nama "uji F" (koreksi) |
| Kotarumalos (2025) | Uji F disebut untuk model spline, bukan Fourier; R², AIC, RMSE |
| Kusdarwati (2023) | Ljung-Box pada residual (p > 0,05 berarti model layak) |
| Habinuddin (2019) | Ljung-Box |
| Aulia Putri (2026) | ADF dengan H₀ dan H₁ tertulis; Ljung-Box |
| Astuti (2018), Hadinata (2026), Syendra Wanti (2026), Tulak (2022), Permata (2024) | Tidak ada uji hipotesis |

Belum terbaca penuh: Susilokarti (PDF rusak), Pratiwi dan Bimaprawira (sudah dikeluarkan).

Kesimpulan: uji hipotesis "ada musim atau tidak" dengan H₀: koefisien gelombang = 0 punya contoh di Purnama, Darmawan, dan Zega. Uji F dari keluaran Excel punya contoh di Azmi. Lima dari 12 artikel yang terbaca tidak memakai uji sama sekali, jadi laporan yang ringan sejalan dengan literatur.

## 5. Rencana xlsx (hanya sampai Bab III)
Excel wajib (keputusan pengguna): memuat data yang dikumpulkan, grafik, dan statistik (mean, median, modus, simpangan baku, dll).
- Sheet Data: tabel 6 tahun × 12 bulan, rata-rata per bulan, kolom cek terhadap rata-rata baris "Kota Mataram" BPS, grafik deret waktu dan rata-rata per bulan.
- Sheet Ringkasan: mean, median, modus, simpangan baku (n−1), min, maks, n per tahun dan total; rata-rata musim hujan dan kemarau; bulan terbasah dan terkering.
- Tidak ada: koefisien, ramalan, RMSE, MAE, ADF, Ljung-Box.
- Berkas baru `Data_Curah_Hujan_Mataram_Bab3.xlsx`, skrip baru di `build/`. Xlsx lama berisi hasil dipindah ke arsip.
- **Sudah dibuat** (31 Okt): `hasil/Data_Curah_Hujan_Mataram_Bab3.xlsx`, skrip `build/buat_xlsx.py` (sebelumnya bernama `buat_xlsx_bab3.py`). Dihitung ulang di LibreOffice: 0 sel error; mean 174,80, median 173,70, simpangan baku 135,35, musim hujan 260,52 dan kemarau 89,07, rata-rata hitungan cocok dengan baris Kota Mataram BPS (selisih maksimum 0,005 mm, 2024). Rata-rata BPS dibaca dari `data_mentah/bps_pdf/dda2021-2026.txt`. Dicetak landscape, muat satu halaman lebar.

## 6. Keputusan pengguna (31 Okt, setelah bagian 1-5)
1. ADF dan Ljung-Box: dibuang.
2. Uji hipotesis: uji F saja, $H_0: b_1 = b_2 = 0$, $H_1$: paling sedikit satu tidak nol, $\alpha = 0{,}05$. Uji t dibuang. Sumber: Darmawan (2017), Purnama (2021), Azmi (2020), Wilks (2019).
3. Sheet Fitur sin/cos: tidak dibuat. Xlsx 2 sheet (Data dan Ringkasan).
4. Lampiran B di PDF: dikerjakan pengguna sendiri.
5. Wei (2019): dilepas. Definisi deret waktu disitasi ke Aulia dkk. (2019) dan Zega & Mardiningsih (2025). Daftar Pustaka jadi 26 entri.
6. Build ulang PDF/docx: tetap menunggu perintah.

Perubahan teks yang sudah dikerjakan di vault: Abstrak par. 3; Bab II 2.2 (jadi "Deret Waktu"), 2.4, 2.7; Bab III 3.9 (6 langkah jadi 4); Gambar 2.1 (kotak ADF dan Ljung-Box dihapus, gambar PNG belum dibuat ulang); `Alur Regresi Harmonik`; Panduan; Konsep Ljung-Box dihapus; Wei 2019 dipindah ke `Artikel Tidak Dipakai`.

Kembali: [[00 Peta Proyek]]

## 7. Penyatuan skrip build (31 Okt malam)
- `build/` kini hanya berisi `buat_xlsx.py`, `buat_docx.py`, dan `README.md`. Lima skrip lama berantai (`buat_laporan*.py`, `buat_pdf_harmonik.py`) digabung jadi `buat_docx.py` dan dipangkas ke 30 dari 42 metode yang benar-benar dipakai; ketergantungan ke `hasil/ringkasan.json` (ARMA lama) hilang.
- Teks di `buat_docx.py` disamakan dengan vault: Abstrak par. 3 dan 4, Bab II 2.2 (Deret Waktu), 2.4 (uji F), 2.6, 2.7, Bab III 3.7 dan 3.9 (4 langkah), Gambar 2.1 (5 kotak), 26 entri pustaka.
- Uji coba dilakukan di folder sementara (`~/.hermes/cache/scratch/dry`), bukan `hasil/` asli: PDF 27 halaman, 36 tautan, 26 entri; grep Ljung-Box, Dickey, Wei, Bimaprawira, Pratiwi, uji t, menyusul, Bab IV, Bab V = 0. "ADF" tersisa hanya di Tabel 2.1 (baris Zega dan Aulia Putri, isi artikel orang lain).
- `hasil/` asli belum ditimpa; PDF/docx di `hasil/kirim/` masih versi lama.
- Backup skrip lama: `~/.hermes/cache/scratch/build_bak/` dan `analisis/`.

## 8. Panduan diperdalam (1 Nov 2026)
- Folder `Panduan/` ditulis ulang untuk pembaca yang belum tahu statistika: 5 catatan bab (pola Isi, Artinya, Alasan, Kalau ditanya dosen, Belum beres) dan 20 catatan Konsep dengan contoh angka kecil. Jumlah kata naik dari sekitar 4.000 menjadi sekitar 9.700.
- Konsep baru: `Konsep Estimasi OLS` dan `Konsep Hipotesis dan Uji F`. Konsep lama `Konsep Estimasi OLS dan Uji F t` dihapus karena menyebut uji t.
- Contoh rekaan (bukan hasil penelitian) diberi label. Tidak ada angka hasil model (b, R², F, RMSE, MAE, amplitudo) di Panduan; F kritis 3,16 untuk derajat bebas (2, 57) adalah nilai tabel, bukan hasil.
- Angka data dihitung ulang dari CSV: rata-rata per bulan, per tahun, bulan terbasah dan terkering per tahun, batas pencilan 590,0 mm.
- Backup Panduan lama: `~/.hermes/cache/scratch/panduan_bak/`.

## 9. Setelah bagian 8 (1 Nov 2026)
Berkas hasil regresi dipindah, laporan lama dihapus, PDF BPS dihapus dan tujuh halaman diamankan, data 72 bulan masuk vault, Lampiran B dan Gambar 2.1 disesuaikan, vault lama diarsipkan, Wilks dilepas, ISBN Sudaryono diverifikasi. Rincian, urutan, dan sisa pekerjaan ada di [[Riwayat Pekerjaan]] (tahap 9 sampai 15). Aturan rujukan: [[Aturan Kerja]] butir 4.
