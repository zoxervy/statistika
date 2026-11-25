# statistika

Tugas Statistika Kelompok 3, S1 Ilmu Komputer, Universitas Bumigora: curah hujan bulanan Kota Mataram dengan regresi harmonik. Dosen pengampu: Siti Soraya, M.Si.

## Tempat kerja
- Root kerja ada di serverarm: `/home/ubuntu/statistika`. Semua perintah dan edit file lewat tool serverarm, bukan di container cloud.
- Vault Obsidian: `Statistika-RegresiHarmonik/`. Mulai baca dari `START.md.md`, `Aturan Kerja.md`, dan `Riwayat Pekerjaan.md`.

## Aturan kerja (ringkasan `Statistika-RegresiHarmonik/Aturan Kerja.md`)
1. Jangan jalankan `build/buat_docx.py`, `build/buat_xlsx.py`, atau generator lain tanpa perintah eksplisit. `buat_xlsx.py` akan menimpa xlsx yang sudah dirapikan pengguna.
2. Jangan jalankan skrip lama `analisis/*.py`.
3. Isi artikel hanya dari abstrak resmi atau PDF artikelnya. Jangan mengarang.
4. Rujukan: penelitian Indonesia, terbit 2016 ke atas, yang memuat sesuatu yang bisa dirujuk. Buku luar negeri tidak dipakai.
5. Laporan berhenti di Bab III. Tidak ada angka hasil model (koefisien, F, R², RMSE, ramalan) di naskah.
6. Docx laporan diedit pengguna di Windows. Jangan ubah docx tanpa perintah.

## Keputusan metode yang berlaku (25 Nov 2026)
- Arahan dosen: seluruh 72 bulan (Jan 2020 – Des 2025) dipakai menyusun model, lalu langsung meramal 12 bulan tahun 2026. Tidak ada pembagian data latih dan data uji.
- Dasar penelitian: Kusdarwati (2023) untuk alur metode harmonik dan penilaian kecocokan model; Astuti dkk. (2018) sebagai penelitian di Kota Mataram yang dilanjutkan dengan data lebih baru.
- Model: regresi harmonik orde k = 1, periode 12 bulan, estimasi OLS, uji F ($H_0: b_1 = b_2 = 0$, α = 0,05).
- Penilaian model: R² dan RMSE pada 72 bulan data sendiri, serta plot data terhadap nilai duga. Tidak ada RMSE/MAE data uji dan tidak ada ramalan pembanding.
- Pencilan Desember 2024 (672,5 mm) dicatat sebagai keterbatasan, tidak dimodelkan.

## Git
- Commit tanpa baris atribusi (tanpa Co-Authored-By atau Claude-Session).
- Push ke branch `ccr-25c97064-q2zd9s`.
- Repo publik. PDF artikel dan halaman BPS, plugin `.obsidian`, dan NIM anggota tidak di-commit (lihat `.gitignore`).
- NIM hanya ada di dua berkas lokal: `build/anggota.json` (dibaca `buat_docx.py` untuk sampul) dan `08 Presentasi/NIM Anggota (lokal).md`. Jangan tulis NIM di berkas lain.
- Satu commit per paket revisi supaya mudah dibatalkan.

## Skill
- `humanizer` terpasang di `~/.claude/skills/humanizer`. Polanya untuk teks Inggris; pada naskah Indonesia pakai sebagai pedoman gaya saja, dan jangan ubah isi, angka, atau sitasi.
