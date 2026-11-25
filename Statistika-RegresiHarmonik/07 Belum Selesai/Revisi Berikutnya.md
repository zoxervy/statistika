---
tipe: tugas
status: "Semua selesai kecuali build ulang PDF/docx"
tags: [statistika, regresi-harmonik, tugas]
---


> Catatan: berkas ini rekaman lama sebelum 31 Okt 2026. Skrip `analisis/buat_pdf_harmonik.py` dan xlsx regresi di bawah sudah diganti `build/buat_docx.py` dan `build/buat_xlsx.py`. Urutan terbaru: [[Riwayat Pekerjaan]].
# Revisi Berikutnya (dicatat 30 Okt 2026; poin 1–4 selesai, PDF dibangun ulang)

Hasil pengecekan PDF `hasil/Laporan_RegresiHarmonik_Bab1-3.pdf` terhadap arahan [[Konsul 27 Okt 2026]].

## Sudah sesuai
- Abstrak 4 paragraf; Abstrak dan Kata Pengantar di halaman terpisah.
- Latar belakang 7 paragraf, semuanya bersitasi.
- Semua subbab Bab II bersitasi.
- Tabel 2.1 berisi 15 artikel Indonesia, terbit 2016–2026.
- Gambar 2.1 punya baris sumber.
- Lampiran A (6 tangkapan tabel BPS) ada.

## Belum
- [x] **1. Lampiran B kosong.** PDF masih bertulisan "[Tangkapan lembar kerja Excel regresi harmonik menyusul.]".
  - Kerjakan: tangkapan layar 3 sheet `hasil/Regresi_Harmonik_Curah_Hujan_Mataram.xlsx` disimpan sebagai `hasil/lampiran/harmonik_excel_*.png`, lalu jalankan `.venv/bin/python analisis/buat_pdf_harmonik.py` (skrip otomatis memasukkan Gambar B.1, B.2, …).
  - Arahan: [[K09 Lampiran tangkapan BPS dan Excel]].
- [x] **2. Tiga rujukan terbit sebelum 2016.** Arahan dosen: rujukan ≥ 2016.
  - Bloomfield (2000): ganti dengan Wilks (2019) untuk deret Fourier dan OLS.
  - Dickey & Fuller (1979): ganti dengan Wei (2019) untuk uji ADF.
  - Ljung & Box (1978): ganti dengan Wei (2019) untuk uji Ljung-Box.
  - Hapus ketiganya dari Daftar Pustaka (31 → 28 entri), lalu cek ulang sitasi ↔ pustaka.
  - Arahan: [[K10 Bab II wajib bersitasi]].
- [x] **3. Rumusan masalah masih dua pertanyaan dalam satu kalimat** ("model terbaik … dan seberapa akurat …"). Arahan dosen: rumusan dan tujuan masing-masing 1.
  - Usulan rumusan: "Bagaimana hasil peramalan curah hujan bulanan Kota Mataram dengan model regresi harmonik?"
  - Usulan tujuan: "Mengetahui hasil peramalan curah hujan bulanan Kota Mataram dengan model regresi harmonik."
  - Ubah juga paragraf 2 Abstrak dan [[Bab I Pendahuluan]] di vault.
  - Arahan: [[K04 Rumusan dan tujuan satu]].
- [x] **4. Daftar isi tidak bisa diklik (masih seperti teks manual).** Dikonfirmasi kelompok: yang dimaksud "daftar hadir" adalah **daftar isi**.
  - Hasil cek berkas (30 Okt):
    - `.docx`: field TOC ada (`TOC \o "1-2" \h \z \u`), tetapi isinya teks biasa yang ditulis skrip: 0 hyperlink, 0 bookmark di judul bab, 0 `PAGEREF`. Jadi entri tidak bisa diklik sampai field di-update di Word.
    - `.pdf`: 0 tautan (`/Link`), jadi daftar isi, daftar tabel, dan daftar gambar tidak bisa diklik sama sekali.
  - Penyebab: `field()` di `analisis/buat_laporan_revisi.py` menulis entri sebagai teks + nomor halaman, tanpa `w:hyperlink` ke bookmark `_Toc…` di tiap judul/keterangan.
  - Perbaikan:
    1. Pasang bookmark `_Toc…` di setiap judul bab/subbab dan keterangan tabel/gambar.
    2. Tulis tiap entri daftar isi/tabel/gambar sebagai `w:hyperlink w:anchor="_Toc…"` dengan nomor halaman `PAGEREF _Toc… \h`.
    3. Ekspor PDF LibreOffice dengan tautan internal aktif, lalu cek jumlah `/Link` di PDF ≥ jumlah entri (36).
    4. Cek manual: klik "BAB II KAJIAN PUSTAKA" di PDF → pindah ke halaman 3.
  - Sementara: di Word, klik kanan daftar isi → Update Field → Update entire table; entri jadi bisa di-Ctrl+klik. PDF tetap tidak bisa sampai poin 1–3 dikerjakan.
  - Arahan: [[K06 Daftar isi otomatis]].
- [ ] **5. (Opsional) Varians sampel.** Tambahkan hanya jika dosen meminta: lihat [[Konsep Varians Sampel]].

## Hasil rebuild (30 Okt 2026)
- PDF `hasil/Laporan_RegresiHarmonik_Bab1-3.pdf`: **27 halaman** (sebelumnya 23).
- **Lampiran B** berisi 7 tangkapan workbook (Gambar B.1–B.7), lebar maks 13,3 cm, semua di dalam margin.
- Daftar Pustaka **28 entri**: Bloomfield (2000), Dickey & Fuller (1979), dan Ljung & Box (1978) dihapus; sitasinya diganti Wilks (2019) atau Wei (2019). Tidak ada sitasi tanpa entri.
- **Rumusan:** "Bagaimana hasil peramalan curah hujan bulanan Kota Mataram dengan model regresi harmonik?" **Tujuan:** "Mengetahui hasil peramalan curah hujan bulanan Kota Mataram dengan model regresi harmonik." Abstrak paragraf 2 ikut diubah.
- **Daftar isi, tabel, gambar bisa diklik:** 36 tautan di PDF, semuanya menuju halaman yang benar (contoh: BAB II → hal. 3). Di `.docx` tiap entri berupa hyperlink ke bookmark `_Toc…` di judul/keterangan.
- Skrip: `analisis/buat_pdf_harmonik.py` (bookmark + hyperlink, Lampiran B otomatis dari `hasil/lampiran/harmonik_excel_*.png`).

## Audit artikel 30 Okt 2026 (malam): vault sudah diperbaiki, PDF/DOCX BELUM
Vault sekarang lebih baru daripada `hasil/Laporan_RegresiHarmonik_Bab1-3.pdf`. Rincian cek: [[Log Verifikasi]].

- [x] **6. Samakan generator PDF dengan vault** (selesai 31 Okt 2026) (`analisis/buat_pdf_harmonik.py`) sebelum rebuild berikutnya:
  - Bab I par. 1: sitasi "(Aulia dkk., 2019; Permata dkk., 2024)" → "sumber daya air … (Aulia dkk., 2019; Aulia Putri dkk., 2026)".
  - Bab I par. 5 dan paragraf penutup 2.6: hapus "Jawa Timur … Bimaprawira & Rejeki, 2021" dari klaim 12 bulan; ganti "tiga kota di Jawa Timur (Kusdarwati, 2023)".
  - 2.6: kalimat "Isi tabel diringkas dari abstrak masing-masing artikel" → tambah "beberapa angka rincian data diambil dari isi artikel".
  - 3.7: ganti kalimat ENSO (BMKG t.t.) dengan teks 3.7 di [[Bab III Metode Penelitian]].
  - `assert len(PUSTAKA_H) == 28` → 27 (entri BMKG dihapus).
- [x] **7. Wei (2019):** dilepas 31 Okt 2026; ADF dan Ljung-Box dibuang, definisi deret waktu disitasi ke Aulia (2019) dan Zega (2025). Lihat [[Artikel Tidak Dipakai]].
- [x] **8. Sudaryono (2021):** tidak ada nomor bab/halaman di laporan, jadi tidak ada yang perlu dicek ([[Sudaryono 2021]]).

## Setelah semua dikerjakan
1. ~~Build ulang PDF dan docx; salin ke `hasil/kirim/`.~~ Selesai.
2. Perbarui [[Status Laporan Revisi]], [[Daftar Tugas]], dan [[Log Verifikasi]].
3. Cek wikilink, lalu buat ulang ZIP vault.

Kembali: [[Daftar Tugas]] · [[00 Peta Proyek]]

## Perbaikan 31 Okt 2026
Poin 6 selesai; PDF/docx dibangun ulang (sebelum pemotongan Bab IV/V) (27 halaman, 36 tautan, 27 entri). Tambahan: Bab I par. 6 dilunakkan, hitungan 2.6 dirapikan, rata-rata 2024 diseragamkan, tiga rujukan diaudit, entri BPS tanpa penerbit. Rincian: [[Log Verifikasi]]. Tersisa: poin 5 opsional.

Catatan 31 Okt 2026: Bab IV dan V dikeluarkan dari proyek. PDF/docx di `hasil/kirim/` masih versi sebelum pemotongan sampai ada perintah build.
