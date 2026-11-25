---
tipe: riwayat
tags: [statistika, regresi-harmonik, riwayat]
---

# Riwayat Pekerjaan

Catatan urut kerja 31 Okt sampai 1 Nov 2026, supaya jelas apa yang sudah dikerjakan, di mana hasilnya, dan apa yang tersisa. Rincian keputusan dan temuan: [[Catatan Progres 31 Okt 2026]]. Pemeriksaan: [[Log Verifikasi]]. Status: [[Daftar Tugas]].

Aturan yang berlaku: tidak ada build PDF/docx ke `hasil/` tanpa perintah ([[Aturan Kerja]]).

## Tahap 1: Audit vault
- Vault diekstrak dan dibaca seluruhnya; 72 statistik dihitung ulang dan cocok.
- Ditemukan sembilan masalah: PDF tertinggal dari vault, Wei (2019) bermasalah, tiga rujukan belum diaudit, klaim berlebihan, SARIMA, rata-rata 2024 (150,72 vs 150,73), hitungan Tabel 2.1, Daftar Pustaka, dan substansi lemah.

## Tahap 2: Perbaikan isi
- Bab I par. 1, 2, 6 diperbaiki. Klaim NTB tanpa sumber dihapus. "Paling sering" diganti "banyak dipakai".
- Bab II 2.6 dan Tabel 2.1: hitungan dibuat konsisten.
- Rata-rata 2024 diseragamkan 150,73 (hitungan CSV 150,725).
- Daftar Pustaka: BPS tanpa penerbit, DOI Aulia (2019) dan Khikmah ditambahkan.
- Tiga rujukan diaudit ke teks aslinya: Aulia (2019), Khikmah & Sofro (2025), Mulsandi (2024). Yang tidak didukung sumber: "air baku" (Aulia) dan klaim NTB (Mulsandi).
- Catatan baru: `Aulia 2019`, `Khikmah 2025`, `Mulsandi 2024`.

## Tahap 3: Lingkup dipotong sampai Bab III
- Bab IV, Bab V, hasil model, perbandingan metode, bahan presentasi, dan semua angka hasil dipindah ke `arsip_di_luar_bab3/` (tidak dihapus).
- `05 Data dan Hasil` diganti nama jadi `05 Data`.
- Angka hasil dan sebutan Bab IV/V dibersihkan dari naskah, Peta, kanvas, dan Panduan.
- Aturan baru: [[Aturan Kerja]] ("jangan build ulang jika tidak disuruh").

## Tahap 4: Penggantian artikel di Tabel 2.1
- Lima PDF dikirim pengguna dan dibaca bersama tujuh lainnya: 12 dari 15 artikel terbaca penuh.
- Bimaprawira & Rejeki (2021) dan Pratiwi dkk. (2020) diganti [[Zega 2025]] dan [[Kotarumalos 2025]].
- Susilokarti (2016) tetap (PDF rusak, abstrak terverifikasi Crossref).
- Pengelompokan: 5 Fourier/harmonik + 6 spektral + 3 Mataram/NTB metode lain + 1 musim = 15.

## Tahap 5: Keputusan penyederhanaan
- ADF dan Ljung-Box dibuang. Uji t dibuang. Uji hipotesis uji F saja: H₀: b₁ = b₂ = 0, H₁: paling sedikit satu tidak nol, α = 0,05.
- Wei (2019) dilepas. Definisi deret waktu disitasi ke Aulia dkk. (2019) dan Zega & Mardiningsih (2025). Daftar Pustaka jadi 26 entri.
- Sheet sin/cos di Excel tidak dibuat.
- Lampiran B dikerjakan pengguna sendiri.
- Teks disamakan di vault: Abstrak par. 3 dan 4, Bab II 2.2/2.4/2.7, Bab III 3.9 (4 langkah), Gambar 2.1, [[Alur Regresi Harmonik]].

## Tahap 6: Excel sampai Bab III
- Berkas: `hasil/Data_Curah_Hujan_Mataram_Bab3.xlsx` (salinan di `hasil/kirim/`).
- Dua sheet: Data (matriks 6×12, rata-rata, cek terhadap BPS, dua grafik) dan Ringkasan (mean, median, modus, simpangan baku, min, maks, n, musim, grafik).
- Hanya rumus aktif dan angka, palet slate monokrom. Dihitung ulang di LibreOffice: 0 sel error.
- Enam rata-rata BPS dicocokkan ke PDF: 155,12; 182,18; 222,75; 136,58; 150,73; 201,42.
- Xlsx lama berisi hasil regresi disalin ke `arsip_di_luar_bab3/hasil/`.

## Tahap 7: Skrip build
- `build/` kini hanya berisi `buat_xlsx.py`, `buat_docx.py`, dan `README.md`.
- Lima skrip lama digabung jadi `buat_docx.py` (30 dari 42 metode yang dipakai); tidak lagi bergantung ke `ringkasan.json`.
- Teks di skrip disamakan dengan vault.
- Diuji di folder sementara, bukan di `hasil/`: PDF 27 halaman, 36 tautan, 26 entri pustaka; istilah yang dibuang = 0.

## Tahap 8: Panduan diperdalam
- Panduan 00–04 ditulis ulang: Isi, Artinya, Alasan, Kalau ditanya dosen, Belum beres.
- 20 catatan Konsep dengan analogi dan contoh angka kecil; dua konsep baru ([[Konsep Estimasi OLS]], [[Konsep Hipotesis dan Uji F]]).
- Konsep lama yang menyebut uji t dihapus. Kata Panduan naik dari sekitar 4.000 jadi sekitar 9.700. Mulai dari [[00 Mulai Di Sini]].

## Tahap 9: Berkas hasil regresi dipindah (1 Nov 2026)
- 57 berkas dipindah dalam tiga gelombang (bukan dihapus) ke `arsip_di_luar_bab3/`. Daftar lengkap dan jalur asal: `arsip_di_luar_bab3/DAFTAR PINDAHAN 1 Nov 2026.txt`.
- Yang dipindah: `Laporan_Revisi_*` (v1, v2), `Laporan_Sampai_Bab3_*` (semua varian), `Regresi_Harmonik_Curah_Hujan_Mataram.xlsx` (hasil/ dan hasil/kirim/), tangkapan Excel `harmonik_excel_3` sampai `_7` (koefisien, F, R², RMSE, MAE, ramalan 2025), dan folder `hasil_harmonik/` (keluaran regresi, ramalan 2025, grafik).
- Gambar `harmonik_excel_1` dan `_2` tetap di `hasil/lampiran/`: isinya hanya data dan statistik deskriptif.
- Tahap lanjutan (disetujui pengguna): laporan era ARMA (`Laporan_Curah_Hujan_Mataram`, `Laporan_Ringkas_*`), `Panduan_Presentasi_*`, `Curah_Hujan_Mataram.xlsx`, `r.txt`, `ringkasan.json`, `lampiran/excel.xlsx`, grafik `ramalan_uji` dan `acf_pacf`, serta semua zip lama di `hasil/` dan `hasil/kirim/` ikut dipindah (total 57 berkas).
- Sisa di `hasil/` sekarang: `Data_Curah_Hujan_Mataram_Bab3.xlsx`, grafik deskriptif (`boxplot_bulan`, `deret_waktu`, `histogram`), dan `lampiran/` (tangkapan BPS, `harmonik_excel_1` dan `_2`). `hasil/kirim/` hanya berisi Excel Bab III.

## Tahap 10: Laporan lama dihapus (1 Nov 2026)
- Dihapus permanen (bukan dipindah), atas perintah pengguna: berkas lama yang memuat ADF, Ljung-Box, atau isi di atas Bab III.
- `Laporan_RegresiHarmonik_Bab1-3.docx` dan `.pdf` di `hasil/` dan `hasil/kirim/` (versi 31 Okt 19:52: memuat ADF, Ljung-Box, Dickey, Bab IV, Bab V, dan angka hasil di abstrak). 4 berkas.
- Gambar `kerangka_harmonik.png` dan `kerangka_univariat.png` di `hasil/grafik/` (kotak ADF, Ljung-Box, uji t; versi ARMA). Gambar versi baru dibuat ulang `build/buat_docx.py` saat build.
- Sebelum dihapus, semua berkas dokumen di `hasil/` dan `vault/.../Berkas/` dipindai: hanya empat laporan itu dan Excel Bab III yang tersisa, dan Excel Bab III bersih.
- Akibatnya `hasil/` dan `hasil/kirim/` tidak lagi punya PDF/docx. Laporan baru baru ada setelah build dijalankan atas perintah ([[Aturan Kerja]]).
- Berkas lama berisi hasil regresi dan ARMA yang dipindah di tahap 9 tetap ada di `arsip_di_luar_bab3/` dan tidak dihapus.

## Tahap 11: PDF BPS dihapus, halaman yang dipakai diamankan (1 Nov 2026)
- Sebelum dihapus, tujuh halaman yang benar-benar dipakai disimpan (PDF satu halaman di `Berkas/BPS/`, teksnya di `data_mentah/bps_halaman/`): Tabel 1.2.1 edisi 2021 (hal. 78), 2022 (84), 2023 (79), 2024 (80), 2025 (73), 2026 (73), serta hal. 69 edisi 2024 (kalimat "almost 0.00 mm" yang dikutip di Bab III 3.5). Ada `README.txt` di folder itu.
- Semua 72 nilai di `curah_hujan_bulanan_bps_bmkg.csv` dicocokkan lagi dengan teks halaman tersimpan: 0 selisih.
- Teks penuh tiap buku (`dda2021` sampai `dda2026.txt`, hasil pdftotext) tetap disimpan; jumlah halaman teks sama dengan PDF-nya.
- Dihapus permanen: 26 PDF, sekitar 383 MB. Terdiri dari enam buku Kota Mataram dalam Angka (`bps_pdf/dda20XX.pdf`) dan 20 PDF kabupaten lain (`bps_pdf_lombok/` untuk Lombok Timur, Utara, Tengah dan `bps_pdf_lombok_barat/`) yang tidak dipakai laporan. Teks (.txt) semuanya masih ada.
- Ditahan: `bps_pdf_lombok/lt2023.pdf` (pdfinfo gagal; tidak ada teksnya). Tidak dipakai laporan.
- Tautan unduh asli tiap buku ada di Daftar Pustaka. Kalau halaman lain dibutuhkan, unduh ulang dari tautan itu (halaman nomor sama dengan teks `dda20XX.txt`).
- Tangkapan Lampiran A (`hasil/lampiran/crop_bps*.png`, `bps*.png`) tidak diubah.

## Tahap 12: Data 72 bulan dimasukkan ke vault (1 Nov 2026)
- `05 Data/Data BPS 72 Bulan.md` ditulis ulang: matriks tahun × bulan 2020–2025 (72 nilai), cek rata-rata hitungan terhadap baris Kota Mataram BPS, daftar panjang 72 baris dengan nomor t dan label latih/uji, ringkasan statistik, rata-rata per tahun.
- Semua angka dibuat dari `curah_hujan_bulanan_bps_bmkg.csv` oleh skrip, bukan diketik tangan. Ke-72 nilai dicocokkan lagi dengan teks halaman BPS di `data_mentah/bps_halaman/`: 0 selisih.
- Baris lama "Tren Sekuler (kemiringan 0,105 mm/bulan, p = 0,89; data stasioner)" dibuang: itu hasil uji yang tidak ada dalam rencana Bab III, dan klaim stasioner terkait ADF yang sudah dibuang.
- `Berkas/curah_hujan_bulanan_bps_bmkg.csv` dan `Berkas/Data_Curah_Hujan_Mataram_Bab3.xlsx` di vault identik dengan versi di `data_mentah/` dan `hasil/`.
- Backup catatan lama: `~/.hermes/cache/scratch/Data_BPS_72_Bulan.bak.md`.
- PDF tujuh halaman BPS dipindah dari `data_mentah/bps_halaman/` ke `Berkas/BPS/` (di dalam vault, dengan `README.txt`); hash dicek sebelum sumber dihapus. Teks halaman tetap di `data_mentah/bps_halaman/`. `Data BPS 72 Bulan` kini menautkan ke tiap PDF. Catatan tahap 11 di atas menyebut jalur lama; jalur yang berlaku: `Berkas/BPS/`.

## Tahap 13: Lampiran B, Gambar 2.1, vault lama, Wilks (1 Nov 2026)
- `build/buat_docx.py`: judul Gambar B diganti 4 judul sesuai `Data_Curah_Hujan_Mataram_Bab3.xlsx` (Sheet Data dan Ringkasan); kalimat pengantar B tidak lagi menyebut `Regresi_Harmonik_*.xlsx`, SIN/COS, LINEST. Lolos kompilasi; tidak dijalankan.
- `02 Laporan/Lampiran.md`: bagian B ditulis ulang (B.1–B.4 berisi data dan statistik deskriptif, tanpa hasil regresi). `build/README.md` disesuaikan.
- `02 Laporan/Gambar 2.1`: "lag 12" dan "Baseline Mean" diganti istilah yang benar.
- Dua vault lama (`Statistika Curah Hujan Mataram` dan `.bak`, era ARMA) dipindah (bukan dihapus) ke `arsip_di_luar_bab3/vault_lama/`. `vault/` sekarang hanya berisi `Statistika-RegresiHarmonik`. Tidak ada skrip aktif yang merujuknya (hanya skrip lama di `analisis/`).
- Wilks (2019): nomor bab diverifikasi dari daftar isi (Bab 5, 7, 10); isi halaman belum dibaca. Pertanyaan baru No. 4 di [[Pertanyaan Terbuka]].
- Cadangan sebelum diedit: `~/.hermes/cache/scratch/` (`buat_docx.sebelum_lampiran.py`, `Lampiran.sebelum.md`, `Gambar21.sebelum.md`).

## Tahap 14: Wilks dilepas, rujukan hanya penelitian Indonesia (1 Nov 2026)
- Kriteria proyek (dari pengguna): hanya artikel dari Indonesia dan yang paling berkaitan dengan tugas. Wilks (2019), buku luar negeri, satu-satunya rujukan asing yang tersisa, dilepas. Daftar Pustaka jadi 25 entri, semuanya penelitian Indonesia.
- Pengganti, hanya dari kalimat yang terbaca di teks artikel: model harmonik dengan cos dan sin untuk curah hujan Indonesia, [[Kusdarwati 2023]] (persamaan 1 dan 2) dan [[Zega 2025]] (persamaan Fourier, "frekuensi dan amplitudo"); OLS, [[Astuti 2018]] (Kota Mataram) dan [[Kotarumalos 2025]] ("meminimalkan jumlah kuadrat kesalahan"); uji F, [[Darmawan 2017]] (F berderajat bebas (2, n−3), kriteria tolak H₀) dan [[Azmi 2020]] ("Significance F").
- Kalimat uji F di Bab II 2.4 tidak lagi bersitasi Wilks; ditambah satu kalimat tentang Darmawan.
- Rumus amplitudo A dan fase φ tidak ada di artikel Indonesia yang sudah dibaca. Naskah kini menyebutnya "diturunkan dari identitas trigonometri", bukan kutipan.
- Diubah: Bab I par. 5, Bab II 2.4, Daftar Pustaka, `build/buat_docx.py` (tidak dijalankan), Panduan 02, 03, 04, lima Konsep, Peta, K10, Pertanyaan Terbuka No. 4 (selesai), Artikel Tidak Dipakai (butir 9), `Wilks 2019` (diberi catatan "tidak dipakai lagi").
- Cadangan sebelum diedit: `~/.hermes/cache/scratch/wilks_bak/`.
- Penegasan pengguna: yang penting rujukan itu menunjang tugas dan ada yang bisa dirujuk di dalamnya. Sudaryono (2021) tetap dipakai (buku Indonesia untuk statistika deskriptif). Kriteria dicatat sebagai butir 4 di [[Aturan Kerja]].
- ISBN Sudaryono (2021) dicari dan diverifikasi: 978-623-01-16-42-1 (cocok di Google Books dan katalog Telkom University; checksum benar; 396 halaman, terbit 20 Agustus 2021). Dicatat di `Sudaryono 2021`. Entri Daftar Pustaka tidak berubah karena APA 7 tidak memuat ISBN untuk buku.
- Keputusan pengguna: rumus mean, median, modus, dan simpangan baku tidak perlu dicarikan nomor bab atau halaman, karena dihitung sendiri dari data. Item itu tidak lagi terbuka. Sitasi Sudaryono tetap karena Bab II 2.3 wajib bersitasi (K10).

## Tahap 15: Memori dan ringkasan akhir sesi (1 Nov 2026)
- Aturan kerja disimpan juga di memori asisten supaya berlaku di sesi berikutnya: laporan berhenti di Bab III, build hanya lewat `build/buat_docx.py` dan `build/buat_xlsx.py` dan hanya atas perintah, metode regresi harmonik k = 1 dengan uji F saja, `analisis/*.py` dianggap usang.
- Urutan kerja satu sesi (31 Okt – 1 Nov): audit, perbaikan isi, pemotongan sampai Bab III, penggantian dua artikel, penyederhanaan metode, Excel, penyatuan skrip build, Panduan, pemindahan dan penghapusan berkas lama, data 72 bulan ke vault, Lampiran B dan Gambar 2.1, pelepasan Wilks, ISBN Sudaryono. Rincian tiap tahap di atas.
- Keputusan pengguna yang berlaku: ADF dan Ljung-Box dibuang; uji F saja; rujukan hanya penelitian Indonesia yang menunjang tugas (cukup ada yang bisa dirujuk); rumus statistik deskriptif tidak perlu dicarikan halaman; build tidak dijalankan tanpa perintah; Lampiran B dikerjakan pengguna.

## Tahap 16: Sitasi Bab I paragraf 1 (1 Nov 2026)
- Kalimat lama mengutip Aulia dkk. (2019) untuk "sumber daya air", padahal artikel itu hanya menyebut pertanian, banjir, dan longsor; kalimat kekeringan tanpa sitasi.
- Teks Aulia Putri dkk. (2026) dibaca ulang; Pendahuluannya memuat ketiganya: "pengelolaan sumber daya air, ketahanan pangan, mitigasi bencana banjir dan kekeringan, serta perencanaan infrastruktur wilayah"; NTB "rentan terhadap kekeringan berkepanjangan pada musim kemarau serta banjir dan tanah longsor pada puncak musim hujan"; model dibutuhkan untuk "mitigasi bencana dan optimalisasi pengelolaan sumber daya air".
- Pertanian: Aulia dkk. (2019) dan Hadinata dkk. (2026) ("pertanian, industri, dan perdagangan"; di Lombok, "pertanian, pariwisata, maupun pengelolaan lingkungan"). Banjir dan longsor: Aulia dkk. (2019) dan Aulia Putri dkk. (2026).
- Kalimat ditulis ulang per klaim, tiap klaim punya sumber yang menyebutnya. Diubah: `02 Laporan/Bab I Pendahuluan.md`, `build/buat_docx.py` (tidak dijalankan), catatan `Aulia Putri 2026`, `Hadinata 2026`, `Aulia 2019`. Cadangan: `~/.hermes/cache/scratch/par1_bak/`.

## Tahap 17: PDF artikel dimasukkan ke vault (1 Nov 2026)
- 17 PDF = 15 artikel Tabel 2.1 + 2 rujukan pendukung di luar tabel (Aulia 2019, Khikmah 2025). Disalin ke `Berkas/Artikel/` (sekitar 10 MB), tiap berkas bernama sama dengan catatannya di `03 Artikel/`.
- Sebelum disalin, tiap PDF dicocokkan dengan judul dan penulis di Daftar Pustaka (17 dari 17 cocok), dan hash salinan dicek sama dengan sumber.
- Sumber PDF tersebar di tiga tempat sementara (folder kerja `art15`, kiriman pengguna di Telegram, unduhan sendiri); semuanya kini punya satu salinan tetap di vault.
- Tidak ada PDF untuk Mulsandi (2024, disertasi) dan Sudaryono (2021, buku).
- Catatan artikel di `03 Artikel/` diberi tautan ke PDF-nya.

## Tahap 18: Rujukan pendukung dipangkas, 25 jadi 22 entri (1 Nov 2026)
- Tiga rujukan di luar Tabel 2.1 dilepas: Aulia dkk. (2019), Khikmah & Sofro (2025), Mulsandi (2024). Daftar Pustaka 22 entri; PDF di `Berkas/Artikel/` jadi 15, sama dengan Tabel 2.1. Dua PDF dipindah ke `arsip_di_luar_bab3/artikel_dilepas/`.
- Tiap kalimat yang mengutip ketiganya dialihkan ke artikel Tabel 2.1 yang teksnya sudah dibaca: definisi 1 mm dan deret waktu, Habinuddin (2019: "serangkaian pengamatan ... yang diukur dalam urutan waktu"; "Jika curah hujan dikatakan 1 mm, artinya air hujan ... setinggi 1 mm") dan Zega (2025); banjir/longsor, Aulia Putri (2026); musim November–April dan Mei–Oktober, Permata (2024); monsun, Kusdarwati (2023) dan Tulak (2022); ENSO, Kusdarwati (2023) dan Aulia Putri (2026); akurasi pada data uji dan RMSE, Hadinata (2026); data hujan dari buku BPS, Kusdarwati, 2023; Purnama, 2021.
- Dua bagian dibuang karena tidak ada sumber pengganti: kalimat "ramalan SARIMA cenderung konstan" (Bab I par. 6) dan penyebutan IOD (Bab III 3.7). Isi laporan selebihnya tidak berubah.
- Diubah: Bab I, II, III, Daftar Pustaka, `build/buat_docx.py` (tidak dijalankan), Panduan 02–04, enam catatan Konsep, K10, catatan tiga artikel yang dilepas.
- Cadangan sebelum diedit: `~/.hermes/cache/scratch/lepas3_bak/`.

## Tahap 19: Pendamping sitasi Sudaryono (1 Nov 2026)
- Sudaryono (2021) satu-satunya sumber mean, median, modus, dan pembagi n − 1 di Bab II 2.3. Dicek apakah artikel Tabel 2.1 bisa menggantikan: tidak ada yang menuliskan rumus, dan tidak ada yang menyebut median atau modus. Hanya Kotarumalos (2025) dan Syendra Wanti (2026) yang memakai rata-rata, simpangan baku, minimum, maksimum.
- Keputusan pengguna: Sudaryono tetap; ditambah satu kalimat pendamping dengan dua artikel itu. Kalimat memakai "juga memulai" dan menyebut lokasi (Ambon, Bengkulu), karena hanya dua artikel yang diperiksa, bukan semua.
- Daftar Pustaka tetap 22 entri. Diubah: Bab II 2.3, `build/buat_docx.py` (tidak dijalankan), Panduan 03, Konsep Mean Median Modus, Konsep Simpangan Baku, catatan `Sudaryono 2021`. Cadangan: `~/.hermes/cache/scratch/sudaryono_bak/`.

## Tahap 20: DOI Kotarumalos dan OCR Susilokarti (1 Nov 2026)
- **DOI Kotarumalos:** `10.63822/8wxe0007` tercetak di PDF dan di metadata halaman jurnal, dan awalan 10.63822 milik Indo Publishing (Crossref). Namun `doi.org` mengembalikan 404 dan Crossref tidak memuat artikelnya. Jadi DOI sudah dicetak tetapi belum didaftarkan. Tautan halaman jurnal (HTTP 200) dipertahankan. Keputusan: tidak ada perubahan di Daftar Pustaka; cek ulang sebelum dikumpulkan.
- **OCR Susilokarti:** Tesseract dipasang (`apt`, bahasa Indonesia dan Inggris) dan 7 halaman di-OCR; hasil di `Berkas/Artikel/Susilokarti 2016 (OCR).txt`. Isi cocok dengan Tabel 2.1 (data 1975–2012, FFT, puncak periodogram 11,97 ≈ 12 bulan), kecuali **MSE 14,92 hanya ada di abstrak**; isi artikel menulis MSE 0,0129 (validasi), 0,0116 (testing), 0,07 (prediksi). Hasil di Tabel 2.1 dan catatan diganti menjadi "puncak periodogram 11,97". Naskah Bab I–III tidak memuat angka MSE itu, jadi tidak ada perubahan di naskah.
- Diubah: catatan `Susilokarti 2016` dan `Kotarumalos 2025`, Tabel 2.1, README Berkas/Artikel, Daftar Tugas. Cadangan: `~/.hermes/cache/scratch/susi_kota_bak/`.

## Tahap 21: Build docx (1 Nov 2026, atas perintah pengguna)
- `build/buat_docx.py` dijalankan: `hasil/Laporan_RegresiHarmonik_Bab1-3.docx` (1,4 MB) dan `.pdf` (24 halaman; PDF ikut dibuat karena skrip memakainya untuk nomor halaman daftar isi). Daftar Pustaka 22 entri, Bab I mulai hal. 7.
- Pemeriksaan teks PDF: tidak ada Ljung, Dickey, Wilks, Mulsandi, Khikmah, Bab IV/V, uji t, IOD, dan angka hasil model (0,4603; 24,30; 73,37; 62,82; 133,45). "ADF" tersisa 2x hanya di Tabel 2.1 (isi artikel Aulia Putri).
- Temuan: skrip menulis angka "169,47 mm" (rata-rata data latih) di Bab II 2.5 padahal naskah vault tidak memuatnya (angka hasil). Skrip disamakan dengan vault, lalu build diulang (2 kali build hari ini).
- Lampiran B masih berisi 2 tangkapan lama (`harmonik_excel_1`, `_2`); menunggu tangkapan dari pengguna.

## Tahap 22: Tautan Daftar Pustaka bisa diklik (1 Nov 2026)
- Pengecekan: di docx tahap 21 hanya ada hyperlink internal (daftar isi); tautan eksternal 0, jadi DOI belum bisa diklik.
- `build/buat_docx.py`: metode `runs_url` mengubah URL di Daftar Pustaka menjadi hyperlink eksternal (biru, bergaris bawah). Satu baris catatan ditambahkan di bawah judul Daftar Pustaka ("tautan ... dapat diklik"); catatan yang sama di `02 Laporan/Daftar Pustaka.md`. Cadangan skrip: `~/.hermes/cache/scratch/buat_docx.sebelum_link.py`.
- Build ulang: 15 tautan eksternal di docx dan 15 anotasi URI di PDF (14 DOI + halaman jurnal Kotarumalos); enam entri BPS dan Sudaryono memang tanpa tautan. 24 halaman; tidak ada Ljung, Wilks, Mulsandi, Khikmah, Bab IV, atau angka hasil model.

## Tahap 23: Perbaikan isi vault tanpa build (1 Nov 2026)
- Hanya berkas .md yang diubah; `build/buat_docx.py` dan `build/buat_xlsx.py` tidak disentuh dan tidak dijalankan.
- Bab I par. 6: kalimat keunggulan regresi harmonik k = 1 diberi sitasi (Kusdarwati, 2023; Zega & Mardiningsih, 2025).
- Bab II 2.3: definisi mean, median, modus diberi sitasi (Sudaryono, 2021). Bab II 2.5: kalimat dua ramalan pembanding ditulis ulang sebagai pilihan penulis, dinilai dengan RMSE/MAE pada data uji (Purnama, 2021; Hadinata dkk., 2026); tidak ada sumber baru.
- Bab III 3.6: "Tabel data dan perhitungan" diganti "Tabel data dan statistik deskriptif" (xlsx hanya 2 sheet, tanpa regresi).
- Kata Pengantar: "Mataram, Oktober 2026" menjadi "November 2026".
- [[Status Laporan Revisi]]: Bab III 4 langkah, Lampiran B sesuai xlsx 2 sheet (tangkapan belum), catatan build 1 Nov. [[Pertanyaan Terbuka]] No. 5: autokorelasi residual (persiapan jawaban lisan). [[Daftar Tugas]] disesuaikan.
- Akibatnya PDF/docx hasil tahap 21–22 tertinggal dari vault; perlu build ulang atas perintah.

## Tahap 24: Panduan diselaraskan untuk pembaca nol statistika (1 Nov 2026)
- Hanya `Panduan/` (.md) yang diubah; tidak ada build, naskah tidak disentuh.
- 00 langkah 4: dua tebakan pembanding disebut (rata-rata semua bulan, rata-rata per bulan kalender).
- 02 par. 6: Isi disamakan dengan naskah; SARIMA dijelaskan dalam bahasa awam.
- 03 2.5: dua pembanding masuk Isi; "harus lebih baik" diganti "belum tentu menang"; sumber Purnama, Hadinata, Permata.
- 04 3.6: Excel hanya data dan statistik deskriptif; regresi, uji F, ramalan di Python saja.
- Konsep Amplitudo dan Fase: arti radian, ω = 0,5236, atan2, t = 0 Januari, t negatif ditambah 12.
- Konsep Hipotesis dan Uji F: arti derajat bebas, F kritis, nilai-p; tautan ke [[Pertanyaan Terbuka]].
- Konsep Baseline dan Konsep RMSE dan MAE: rujukan disamakan dengan Bab II 2.5.
- Tautan rusak: 0.


## Tahap 25: Docx siap kumpul (2 Nov 2026, Claude Code di Windows)
Pemegang kerja pindah dari Hermes ke Claude Code. Folder kerja baru: `Desktop/Claude/Statistika-RH/Build_RegresiHarmonik/`. Skrip `build/buat_docx.py` dan `buat_xlsx.py` **tidak dijalankan**; docx diedit langsung (XML di dalam docx) lalu dicek lewat Microsoft Word.

1. **Docx Hermes disalin.** Docx 2 Nov dari Hermes (bersih, tanpa ADF/Ljung-Box) disalin ke folder Build. Docx dan PDF lama 31 Okt (memuat ADF, Ljung-Box, Bab IV) mula-mula diberi nama `_31Okt`, lalu dihapus atas perintah pengguna. Isi lain folder Build (`.venv`, `analisis`, `hasil`, `vault`, dan lain-lain) dibuang ke Recycle Bin.
2. **Xlsx rapi dari pengguna.** `Berkas/Data_Curah_Hujan_Mataram_Bab3.xlsx` diganti dengan versi yang dirapikan pengguna, berisi 3 sheet: Data, Ringkasan, Deret Waktu. Salinan di Downloads dihapus.
   - Ke-72 angka dicocokkan dengan CSV dan dengan 6 PDF halaman Tabel 1.2.1 di `Berkas/BPS/`: 0 selisih. Dua angka yang tertutup watermark dicek dari gambar dan benar.
   - Semua statistik berupa rumus Excel, bukan angka ketikan.
   - Jangan jalankan `build/buat_xlsx.py`, karena akan menimpa xlsx rapi ini.
3. **Audit docx.** Docx diperiksa: tidak ada ADF, Ljung-Box, Wilks, Bab IV/V, atau angka hasil model. Ada dua kalimat yang tertinggal dari vault, diperbaiki di langkah 5.
4. **Lampiran B diganti dengan tangkapan xlsx terbaru.**
   - Gambar diekspor langsung dari Excel (sheet dijadikan gambar, tepi kosong dipotong).
   - Gambar B.1 = Sheet Data: curah hujan bulanan 2020–2025 (tahun × bulan) beserta rata-rata tahunan dan bulanan.
   - Gambar B.2 = Sheet Ringkasan: statistik deskriptif, statistik per tahun, rata-rata per bulan, dan grafik.
   - Sheet Deret Waktu tidak dimasukkan.
   - Kalimat pengantar Lampiran B: "diekspor langsung dari Microsoft Excel. Angka biru disalin dari publikasi BPS; angka hitam dihitung dengan rumus Excel".
5. **Dua kalimat disamakan** (docx dan vault):
   - Bab I par. 6: anak kalimat "baru kemudian memeriksa autokorelasi residualnya" dibuang, karena Ljung-Box sudah tidak dipakai.
   - Bab III 3.6: "Statistik deskriptif dihitung di Microsoft Excel (Lampiran B); regresi harmonik dan uji F dihitung dengan Python 3 (pandas, SciPy, statsmodels, matplotlib)."
   - Vault yang diubah: `Bab I Pendahuluan`, `Bab III Metode Penelitian`, [[Lampiran]] bagian B (kini B.1–B.2; catatan lama B.1–B.4 dan B.1–B.7 di tempat lain adalah riwayat).
6. **Daftar Lampiran ditambahkan** setelah Daftar Gambar, di halaman sendiri, dengan judul DAFTAR LAMPIRAN.
   - Isinya field Word otomatis yang hanya membaca judul Lampiran A dan Lampiran B (`TOC \o "2-2" \b IsiLampiran`). Bisa diklik dan ikut diperbarui saat F9.
   - Daftar Isi kini juga memuat DAFTAR LAMPIRAN.
   - Spasi baris Daftar Isi dirapatkan supaya tetap muat satu halaman.
   - Field sudah diperbarui oleh Word sebelum disimpan, jadi nomor halaman benar.
7. **Hasil akhir:** `Build_RegresiHarmonik/Laporan_RegresiHarmonik_Bab1-3.docx`, 25 halaman. Isi teks dibandingkan dengan versi Hermes: yang berubah hanya butir 4–6.
8. **Cadangan:** `Desktop/Claude/Statistika-RH/cadangan_docx/`, berisi versi sebelum Lampiran B dan versi Lampiran B tanpa Daftar Lampiran.

Sisa untuk pengguna:
- Buka docx di Word dan periksa sekilas.
- Kalau ada yang diedit lagi, tekan Ctrl+A lalu F9 dan pilih "Update entire table".
- Save As PDF untuk dikumpulkan.
- Metadata Penulis masih "python-docx". Ganti lewat File → Info kalau perlu.

## Tahap 26: Cek docx v2 dan panduan presentasi (3 Nov 2026, Claude Code)
1. **Docx v2 pengguna dicek.** `Curah_Hujan_Regresi_Harmonik_v2.docx`: baris Lampiran A dan B dihapus dari Daftar Isi, jadi keduanya hanya tercantum di Daftar Lampiran. Teks lain sama dengan v1, tetap 25 halaman, dan hasilnya tidak berubah setelah update TOC. Dinyatakan benar.
2. **Panduan presentasi PDF.** `Build_RegresiHarmonik/Panduan_Presentasi.pdf` (6 halaman). Isinya:
   - usulan pembagian peran: Yusuf Bab I, Gracia Bab II, Raudhatul Bab III dan penutup;
   - alur 13 slide dengan contoh kalimat;
   - daftar hal yang tidak boleh diucapkan;
   - 16 pertanyaan yang mungkin diajukan dosen, diambil dari Panduan;
   - cek sebelum tampil.

   Panduan ini tidak memuat angka hasil model; yang dipakai hanya angka deskriptif dari Bab I/III. Sumber HTML-nya di folder temp, tidak disimpan di vault.
   - Ditambahkan bagian 3 "Cara membaca rumus": daftar 21 simbol beserta cara melafalkannya, misalnya "epsilon te", "fi", "omega", dan "sigma", lalu 8 rumus dari Bab II/III, masing-masing dengan lafal dan artinya. Diingatkan juga bahwa A punya dua arti: amplitudo, dan A_t sebagai nilai aktual di RMSE/MAE. PDF sekarang 8 halaman.
3. Catatan: Kata Pengantar di docx masih "Oktober 2026", sedangkan vault "November 2026". Ubah manual di Word kalau perlu.

## Keadaan saat ini (diperbarui 1 Nov 2026)
- **Pembaruan 2 Nov 2026 (tahap 25):** docx siap kumpul ada di `Desktop/Claude/Statistika-RH/Build_RegresiHarmonik/`. Isinya sudah sama dengan vault, Lampiran B sudah diisi tangkapan xlsx terbaru, dan Daftar Lampiran sudah ada. Butir "Masih terbuka" 1 dan 2 di bawah selesai. Catatan di bawah ini keadaan 1 Nov.

- Naskah Bab I–III, Daftar Pustaka (22 entri), dan Panduan sudah mengikuti keputusan terbaru: uji F saja, rujukan hanya penelitian Indonesia, tanpa ADF, Ljung-Box, uji t, Wei, dan Wilks.
- PDF/docx laporan dibangun 1 Nov (tahap 21–22), tetapi belum memuat perbaikan tahap 23. Build ulang hanya atas perintah.
- Yang ada di `hasil/`: `Data_Curah_Hujan_Mataram_Bab3.xlsx` (juga di `hasil/kirim/`), grafik deskriptif, tangkapan BPS (Lampiran A), `harmonik_excel_1` dan `_2`.

## Masih terbuka
1. **Lampiran B**: tangkapan layar dari `Data_Curah_Hujan_Mataram_Bab3.xlsx`, dikerjakan pengguna. Skrip memasukkan semua `hasil/lampiran/harmonik_excel_*.png` berurutan; judul untuk 4 gambar pertama sudah ada.
2. **Build PDF/docx ke `hasil/`**: menunggu perintah ([[Aturan Kerja]]). Cek dulu bahwa tangkapan Lampiran B sudah ganti.
3. ~~DOI Kotarumalos~~ selesai: keputusan pengguna 1 Nov 2026, tautan halaman jurnal (HTTP 200) cukup; DOI belum terdaftar di Crossref.
4. ~~Susilokarti (2016) OCR~~ selesai (tahap 20).
5. Pembanding "rata-rata per bulan kalender" bisa mengalahkan model harmonik; jangan menjanjikan model menang.
6. Rumus amplitudo A dan fase φ tidak ada di artikel Indonesia yang sudah dibaca; naskah menyebutnya turunan identitas trigonometri.

Selesai dan tidak perlu dicari lagi: Wilks (dilepas), ISBN Sudaryono (978-623-01-16-42-1), nomor bab dan halaman rumus statistik deskriptif (dihitung sendiri dari data).

## Peta berkas
- **Vault** (`vault/Statistika-RegresiHarmonik/`): naskah `02 Laporan/`, artikel `03 Artikel/`, buku `04 Teori/`, data `05 Data/` (matriks 72 bulan), `Panduan/`, skrip `build/`. Aset di `Berkas/`: CSV 72 nilai, Excel Bab III, logo, PDF tujuh halaman BPS di `Berkas/BPS/`, dan 15 PDF artikel Tabel 2.1 di `Berkas/Artikel/`.
- **Di luar vault** (`kuliah/statistika/`): `hasil/` (Excel, grafik, lampiran), `data_mentah/` (CSV, teks tujuh halaman BPS di `bps_halaman/`, teks penuh enam buku di `bps_pdf/`), `arsip_di_luar_bab3/`, `analisis/` (skrip lama, jangan dijalankan).
- **Arsip** (`arsip_di_luar_bab3/`, tidak dihapus): berkas hasil regresi dan laporan era ARMA di `hasil/`, `hasil_harmonik/`, dan dua vault lama di `vault_lama/`. Daftar jalur asal: `DAFTAR PINDAHAN 1 Nov 2026.txt`.
- **Cadangan sementara** (`~/.hermes/cache/scratch/`): `vault_bak_*`, `build_bak`, `panduan_bak`, `wilks_bak`, `Data_BPS_72_Bulan.bak.md`. Folder ini dibersihkan otomatis setelah 24 jam tidak dipakai, jadi salin dulu kalau ingin disimpan.
- **Dihapus permanen**: laporan lama yang memuat ADF dan Ljung-Box (tahap 10), serta 26 PDF buku BPS penuh (tahap 11).

Kembali: [[00 Peta Proyek]]
