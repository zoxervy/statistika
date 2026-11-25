---
tipe: panduan
tags: [statistika, regresi-harmonik, konsep]
---

# Konsep: Populasi dan Sampel

**Satu kalimat:** Populasi adalah semua yang ingin kita ketahui; sampel adalah bagian yang benar-benar kita ukur.

## Analogi sup
Seluruh sup dalam panci = populasi. Satu sendok yang dicicipi = sampel. Kita menilai rasa panci dari sendok itu.

## Di penelitian ini
- **Populasi:** seluruh curah hujan bulanan Kota Mataram sepanjang waktu.
- **Sampel:** 72 bulan, Januari 2020–Desember 2025.
- **Semua bulan diambil, tanpa memilih atau mengacak,** karena deret waktu harus utuh. Melompati bulan merusak urutan.

## Pengaruhnya pada hitungan
Karena 72 bulan hanya sampel, simpangan baku dan varians memakai pembagi **n − 1**, bukan n.
- Rumus sampel (n − 1): 135,35 mm.
- Kalau dianggap populasi (n): 134,40 mm.

Bedanya kecil karena datanya banyak, tetapi rumus sampel yang benar menurut aturan. Di Excel: `STDEV` (sampel), bukan `STDEVP` (populasi).

## Jawaban pendek untuk dosen
"Populasinya seluruh curah hujan bulanan Kota Mataram. Sampelnya 72 bulan tahun 2020–2025, diambil semua. Karena sampel, simpangan baku memakai n − 1."

Terkait: [[Konsep Varians Sampel]], [[Konsep Simpangan Baku]]. Dipakai di: [[Bab III Metode Penelitian]] (3.4). Kembali: [[00 Mulai Di Sini]].
