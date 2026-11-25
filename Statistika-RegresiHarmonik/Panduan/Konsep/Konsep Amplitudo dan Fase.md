---
tipe: panduan
tags: [statistika, regresi-harmonik, konsep]
---

# Konsep: Amplitudo dan Fase

**Satu kalimat:** Amplitudo adalah tinggi ayunan gelombang dari garis tengahnya; fase adalah bulan ke berapa puncak gelombang terjadi.

## Dua pertanyaan yang dijawab
1. Seberapa jauh hujan naik-turun dari rata-ratanya? → **amplitudo (A)**.
2. Kapan puncaknya? → **fase (φ)**.

## Rumus
- A = √(b₁² + b₂²). Puncak = b₀ + A, lembah = b₀ − A. Jarak puncak ke lembah = 2A.
- φ = atan2(b₁, b₂). Puncak terjadi pada t = φ/ω, dengan ω = 2π/12.

## Istilah di rumus fase, satu per satu
- **Radian:** satuan sudut, seperti derajat. Satu putaran penuh = 360° = 2π radian ≈ 6,2832 radian.
- **ω = 2π/12 ≈ 0,5236:** sudut yang ditempuh "jarum jam" tiap bulan. Dua belas bulan × 0,5236 = satu putaran penuh.
- **atan2(b₁, b₂):** fungsi kalkulator yang mengubah pasangan b₁ dan b₂ menjadi satu sudut φ, yaitu posisi jarum jam saat gelombang di puncak. (Di Excel urutannya terbalik: `ATAN2(b₂; b₁)`.)
- **t = φ ÷ ω:** mengubah sudut menjadi nomor bulan. t = 0 berarti Januari, t = 1 Februari, dan seterusnya sampai t = 11 Desember.
- **Kalau t negatif:** atan2 bisa memberi sudut negatif. Tambahkan 12 pada t supaya jatuh di antara 0 dan 12. Contoh: t = −1,5 menjadi 10,5, yaitu pertengahan November.

## Contoh rekaan (bukan hasil penelitian)
Misalkan b₁ = 3 dan b₂ = 4.
- A = √(9 + 16) = 5. Hujan berayun 5 satuan ke atas dan ke bawah dari garis tengah.
- φ = atan2(3, 4) ≈ 0,64 radian. Puncak pada t ≈ 0,64 ÷ 0,5236 ≈ 1,2, yaitu sekitar sebulan lebih setelah Januari (awal Februari).

Cek rumusnya: dengan b₁ = 3 dan b₂ = 4, kurva 3·sin + 4·cos memang menjadi 5·cos(ωt − φ), karena cos φ = 4/5 dan sin φ = 3/5.

## Mengapa penting
Dua angka ini mengubah tiga koefisien yang abstrak menjadi kalimat yang bisa dipahami orang awam: "puncak hujan jatuh sekitar bulan X, dengan ayunan sebesar Y mm". Itu yang disebut di Bab I par. 6: model "dapat ditafsirkan melalui amplitudo dan fase".

## Perhatian
Nilai A dan φ baru ada setelah analisis dijalankan. Laporan berhenti di Bab III, jadi angkanya tidak dimuat. Jangan menuliskan nilai A atau φ di naskah.

Rujukan: Zega dan Mardiningsih (2025) untuk istilah amplitudo pada analisis harmonik. Rumus A dan φ adalah identitas trigonometri, bukan kutipan. Dipakai di: [[Bab II Kajian Pustaka]] (2.4). Terkait: [[Konsep Regresi Harmonik dan Gelombang Sinus Kosinus]]. Kembali: [[00 Mulai Di Sini]].
