---
tipe: panduan
tags: [statistika, regresi-harmonik, konsep]
---

# Konsep: Regresi Harmonik dan Gelombang Sinus-Kosinus

**Satu kalimat:** Regresi harmonik adalah regresi biasa yang variabel bebasnya diganti sinus dan kosinus dari waktu, supaya bisa menggambar pola yang berulang.

## Mulai dari jam dinding
Bayangkan jarum jam yang berputar satu putaran penuh tiap 12 bulan. Tinggi ujung jarum dilihat dari samping naik-turun seperti gelombang. Itu sinus. Kalau dilihat dari arah lain, itu kosinus. Dua-duanya gelombang yang sama, hanya bergeser seperempat putaran.

## Isi tabel sinus dan kosinus (periode 12 bulan)
Waktu diberi nomor t: Januari 2020 = 0, Februari = 1, dan seterusnya.

| t (bulan dalam setahun) | 0 Jan | 1 Feb | 2 Mar | 3 Apr | 4 Mei | 5 Jun | 6 Jul | 7 Agu | 8 Sep | 9 Okt | 10 Nov | 11 Des |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| sin(2πt/12) | 0 | 0,5 | 0,87 | 1 | 0,87 | 0,5 | 0 | −0,5 | −0,87 | −1 | −0,87 | −0,5 |
| cos(2πt/12) | 1 | 0,87 | 0,5 | 0 | −0,5 | −0,87 | −1 | −0,87 | −0,5 | 0 | 0,5 | 0,87 |

Pada t = 12 (Januari tahun berikutnya) nilainya kembali seperti t = 0. Itu sebabnya gelombangnya berulang tiap 12 bulan, tanpa kita memaksa.

## Rumus model (k = 1)
Y_t = b₀ + b₁·sin(2πt/12) + b₂·cos(2πt/12) + ε_t

Dibaca: hujan bulan ke-t = garis tengah + (b₁ kali sinus) + (b₂ kali kosinus) + sisa yang tidak bisa dijelaskan.
- **b₀:** tinggi garis tengah gelombang (kira-kira rata-rata hujan).
- **b₁, b₂:** mengatur tinggi ayunan dan bulan puncaknya.
- **ε_t:** galat, yaitu bedanya hujan sebenarnya dengan kurva. Hujan tidak pernah persis mengikuti rumus.

## Mengapa harus berdua
Sinus saja selalu mulai dari nol, kosinus saja mulai dari puncak. Dengan b₁ dan b₂ yang bisa diatur, jumlah keduanya adalah satu gelombang yang puncaknya bisa digeser ke bulan mana saja. Karena itu keduanya selalu dipertahankan, walau salah satu koefisien kecil ([[Konsep Amplitudo dan Fase]]).

## Apa arti k = 1
k = banyaknya "harmonik" (gelombang) yang dipakai. k = 1 satu gelombang yang selesai tiap 12 bulan. k = 2 menambah gelombang kedua yang selesai tiap 6 bulan untuk membentuk lekukan lebih rumit. Kita memakai **k = 1** supaya sederhana (hanya 3 angka yang dicari), dan Kusdarwati (2023) memakai orde 1 untuk Malang dan Banyuwangi, dan orde 2 untuk Surabaya.

## Mengapa ini masih disebut "regresi linear"
Rumusnya bukan garis lurus terhadap waktu, tetapi **linear terhadap b₀, b₁, b₂**. Sinus dan kosinus sudah dihitung dulu menjadi dua kolom angka biasa, lalu dipakai seperti variabel X biasa. Karena itu cara mencari angkanya bisa memakai OLS ([[Konsep Estimasi OLS]]).

Rujukan: Kusdarwati (2023) dan Zega dan Mardiningsih (2025); keduanya menuliskan persamaan sinus-kosinus untuk curah hujan Indonesia. Dipakai di: [[Bab I Pendahuluan]] (par. 5), [[Bab II Kajian Pustaka]] (2.4). Kembali: [[00 Mulai Di Sini]].
