---
tipe: log
tags: [statistika, regresi-harmonik, tugas]
---

# Log Verifikasi

| Unsur | Hasil | Cara cek |
|---|---|---|
| 72 data BPS | Cocok | Dicocokkan dengan 6 PDF BPS |
| 15 DOI Tabel 2.1 | Aktif | Crossref API, 30 Okt 2026 |
| Isi Tabel 2.1 | Ditulis ulang | Hanya dari abstrak resmi (`referensi/artikel_final_crossref.json`) |
| Sudibyakto (2016) | Dikeluarkan | Data tahunan 1951–1988, terbitan lama |
| Wahyuni dkk. (2016) | Dikeluarkan | Data stasiun Chicago, AS (dicek di PDF) |
| Habinuddin dkk. | Tahun 2019 | Sesuai label terbitan jurnal (Vol. 11 No. 1, 2019) |
| Astuti dkk. (2018) | Volume 1(2) – selesai | Header PDF dan halaman terbitan jurnal sama-sama Vol. 1 No. 2 Desember 2018; 2(2) hanya di template sitasi otomatis |
| Sitasi ↔ Daftar Pustaka | Cocok | Dicek skrip: semua sitasi Bab I–III punya entri (28 entri) |

Generator lama (`analisis/build_all_harmonik.py` dkk.) **jangan dijalankan lagi**: akan menimpa perbaikan ini. Jangan build ulang PDF/docx jika tidak disuruh: [[Aturan Kerja]].

Kembali: [[00 Peta Proyek]]

## Rebuild PDF 30 Okt 2026
| Cek | Hasil |
|---|---|
| Tautan daftar isi/tabel/gambar | 36 tautan, 0 tanpa tujuan |
| Gambar keluar margin | 0 (cek posisi gambar di PDF) |
| Rujukan < 2016 | 0 (kecuali BMKG t.t.) |
| Sitasi tanpa entri pustaka | 0; Daftar Pustaka 28 entri |
| Teks "menyusul" | 0 |

## Audit artikel 30 Okt 2026 (malam), hanya vault
| Cek | Hasil |
|---|---|
| DOI, judul, penulis, volume, nomor, halaman 15 artikel vs Crossref | Cocok; beda hanya Tulak (Crossref hal. 44, jurnal 47–54; dipakai 47–54) dan Habinuddin (terbitan 2019, daring Maret 2020; dipakai 2019) |
| Isi Tabel 2.1 vs abstrak | Cocok; 3 angka dari isi PDF (Hadinata, Purnama, Aulia Putri) kini ditandai |
| Klaim "12 bulan di Jawa Timur" (Bimaprawira) | Tidak didukung abstrak; diganti Kusdarwati (2023): periodogram tiga kota Jawa Timur, periode 1 tahun |
| Klaim "El Niño mengurangi curah hujan" (BMKG t.t.) | Halaman BMKG nonaktif; kalimat diganti Mulsandi (2024) dan Kusdarwati (2023); entri BMKG dihapus, DP 27 entri |
| Bab I par. 1 "air baku" (Aulia 2019; Permata 2024) | Diganti "sumber daya air" (Aulia dkk., 2019; Aulia Putri dkk., 2026) |
| Abstrak, Bab I–III vault vs PDF | Ditulis ulang mengikuti teks PDF + perbaikan di atas; bahasa promosi lama dihapus |
| Wei (2019) | Cetak ulang edisi 2006; menunggu keputusan |
| Sudaryono (2021) | Buku ada; ISBN/bab/halaman dihapus karena belum dicek |


## Perbaikan 31 Okt 2026
| Unsur | Hasil | Cara cek |
|---|---|---|
| Bab I par. 6 | "paling sering" diganti "banyak dipakai ... antara lain oleh Purnama (2021) dan Aulia Putri dkk. (2026)" | Klaim superlatif tidak disokong dua sitasi |
| Bab II 2.6 | Hitungan dirapikan: 4 Fourier + 6 spektral + 4 wilayah non-harmonik + 1 musim = 15; artikel berlokasi di Mataram/Lombok/NTB ada 5 karena Astuti (2018) di kelompok Fourier | Kelompok Tabel 2.1 dijumlah |
| Rata-rata 2024 | 150,725 dari CSV; ditulis 150,73 di Bab III, Data BPS, dan Revisi BPS | Dihitung dari `data_mentah/*.csv` |
| Aulia dkk. (2019) | 1 mm = 1 liter/m², banjir/longsor, ramalan konstan Des 2018–Apr 2019: didukung. "Air baku"/"sumber daya air": tidak ada di artikel; Aulia dipakai untuk pertanian, banjir, longsor | Abstrak dan PDF; catatan `Aulia 2019` |
| Khikmah & Sofro (2025) | Data BPS (Kalimantan Tengah) dipakai untuk peramalan; evaluasi RMSE data uji (latih 80%, uji 20%): didukung | Abstrak dan PDF; catatan `Khikmah 2025` |
| Mulsandi (2024) | Musim hujan Nov–Apr, kemarau Mei–Okt, monsun, ENSO dan IOD: didukung. Klaim khusus NTB: tidak didukung, kalimat Bab I par. 2 diganti "Iklim Indonesia didominasi pola hujan monsunal" | Abstrak IPB Repository; PDF fulltext tidak dibuka (akses dibatasi) |
| Astuti dkk. (2018) | Halaman jurnal dan header PDF: Vol. 1 No. 2 Desember 2018, hal. 23–36. DOI `10.29303/emj.v2i2.16` dan templat sitasi OJS menulis 2(2); Crossref tanpa volume/nomor. Entri tetap 1(2) mengikuti terbitan | Halaman eigen.unram.ac.id dan Crossref. Keputusan akhir bisa berubah bila dosen mengecek DOI |
| Aulia (2019) dan Khikmah (2025) | Entri Daftar Pustaka memakai DOI (`10.25077/jmu.8.2.37-44.2019`, `10.26740/jram.v9n2.p199-207`) | Halaman jurnal |
| Entri BPS | Penerbit sama dengan penulis, dihapus dari entri (APA 7) | Aturan APA 7 |
| Sudaryono (2021) | Tidak ada ISBN/bab/halaman | Tidak dicek ulang ke buku |
| Generator `buat_pdf_harmonik.py` | Teks Bab I par. 1, 2, 5, 6, 2.1, 2.6, 3.7 disamakan dengan vault; `assert len(PUSTAKA_H) == 27` | Build ulang 27 halaman |
| PDF baru | 36 tautan; 27 entri pustaka; grep "menyusul", "t.t.", "paling sering", "air baku", "12 bulan ... Jawa Timur": 0 | `pdftotext` |
| Mulsandi, Kusdarwati dikutip untuk ENSO/IOD | Kusdarwati (2023) menyebut ENSO dan monsun; IOD hanya dari Mulsandi | Abstrak Kusdarwati |

## Pemotongan sampai Bab III, 31 Okt 2026
Bab IV, Bab V, hasil model, dan bahan presentasi dipindah ke `arsip_di_luar_bab3/` di luar vault. Angka hasil model dihapus dari catatan Panduan, Konsep, Peta, dan Keputusan Metode. Log pengecekan angka hasil (koefisien, RMSE, Excel LINEST) ada di salinan arsip. PDF/docx belum dibangun ulang (lihat [[Aturan Kerja]]).

## Penggantian artikel 31 Okt 2026
| Unsur | Hasil | Cara cek |
|---|---|---|
| Zega & Mardiningsih (2025) | PDF terbaca penuh; hipotesis dan uji Fisher tertulis; metadata cocok Crossref | PDF dan Crossref |
| Kotarumalos dkk. (2025) | PDF terbaca penuh; DOI tercetak belum aktif di doi.org dan Crossref; rujukan memakai tautan halaman | PDF dan doi.org |
| Bimaprawira (2021), Pratiwi (2020) | Dikeluarkan dari Tabel 2.1 dan Daftar Pustaka; catatan di [[Artikel Tidak Dipakai]] | – |
| Sitasi dan Daftar Pustaka | 27 entri, semua tersitasi | skrip |
| Skrip `build/buat_pdf_harmonik.py` | Disamakan dengan vault, lolos `py_compile`; tidak dijalankan | – |
| Xlsx Bab III | Angka cocok; rata-rata BPS enam tahun dicocokkan dengan PDF BPS (155,12; 182,18; 222,75; 136,58; 150,73; 201,42) | LibreOffice dan `pdftotext` |
| Skrip `build/buat_docx.py` | Gabungan 5 skrip lama; dijalankan di folder sementara: 27 halaman, 36 tautan, 26 entri; grep istilah yang dibuang = 0 | `pdftotext` |
| Wilks (2019) dilepas | Buku luar negeri. Pengganti dicek ke teks artikel: Kusdarwati (persamaan harmonik dengan cos dan sin), Zega (persamaan Fourier, 'frekuensi dan amplitudo'), Astuti dan Kotarumalos (OLS), Darmawan (F berderajat bebas (2, n−3)), Azmi (Significance F) | teks artikel (scratch/art15) |
Rekap uji pada 12 artikel yang terbaca: [[Catatan Progres 31 Okt 2026]].

Catatan skrip: nama `buat_pdf_harmonik.py` pada baris di atas adalah nama lama; sejak 31 Okt malam skrip itu digabung ke `build/buat_docx.py` ([[Riwayat Pekerjaan]], tahap 7). Hitungan 27 entri berlaku sebelum Wei dilepas; sekarang 26.
