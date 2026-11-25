---
tipe: panduan
tags: [statistika, regresi-harmonik, panduan]
---

# Panduan 03: Bab II Kajian Pustaka

Naskah asli: [[Bab II Kajian Pustaka]]. Prasyarat: [[02 Bab I Pendahuluan]].

Bab II adalah "kotak peralatan": semua teori yang dipakai di Bab III dijelaskan di sini, lengkap dengan sumber. Dosen minta setiap subbab bersitasi ([[K10 Bab II wajib bersitasi]]) dan penelitian terdahulu berbentuk tabel minimal 15 artikel dengan rujukan tahun 2016 ke atas.

## 2.1 Curah hujan
- **Isi:** Hujan = jatuhnya butiran air ke bumi. 1 mm curah hujan = air setinggi 1 mm di permukaan datar 1 m² = 1 liter per m². Musim hujan sekitar Nov–Apr, kemarau Mei–Okt.
- **Artinya:** Angka di data (mis. 350 mm) berarti 350 liter air jatuh di tiap satu meter persegi dalam bulan itu.
- **Alasan:** Pembaca perlu tahu satuan data sebelum membaca statistiknya. Sumber: Habinuddin dkk. (2019); Permata dkk. (2024).
- Konsep: [[Konsep Curah Hujan dan Milimeter]].

## 2.2 Deret waktu
- **Isi:** Deret waktu = data yang dikumpulkan berurutan menurut waktu. Dianalisis untuk mengenali pola dan meramal nilai berikutnya. Data hujan bulanan termasuk deret waktu.
- **Artinya:** Urutan itu penting. Januari 2020, Februari 2020, dan seterusnya tidak boleh diacak.
- **Alasan:** Karena itu data latih/uji dibagi menurut waktu, bukan diacak. Sumber: Habinuddin dkk. (2019); Zega & Mardiningsih (2025).
- Konsep: [[Konsep Deret Waktu dan Pola Musiman]].

## 2.3 Statistika deskriptif
- **Isi:** Merangkum data dengan ukuran pemusatan (mean, median, modus) dan penyebaran (simpangan baku). Rumus: x̄ = Σxᵢ / n dan s = √( Σ(xᵢ − x̄)² / (n−1) ).
- **Artinya:** Ringkas 72 angka menjadi beberapa angka perwakilan, dan satu angka yang bilang "angkanya berserakan sejauh apa".
- **Alasan pembagi n−1:** 72 bulan hanyalah sampel dari seluruh hujan Mataram, jadi dipakai rumus sampel.
- **Sumber:** Sudaryono (2021) untuk definisi dan rumus. Kotarumalos dkk. (2025) dan Syendra Wanti dkk. (2026) hanya contoh penelitian hujan Indonesia yang memulai dengan rata-rata, simpangan baku, minimum, dan maksimum; keduanya tidak mendefinisikan, dan tidak ada artikel Tabel 2.1 yang menyebut median atau modus.
- Konsep: [[Konsep Mean Median Modus]], [[Konsep Simpangan Baku]], [[Konsep Varians Sampel]], [[Konsep Populasi dan Sampel]].

## 2.4 Regresi harmonik
Inti laporan. Dibaca pelan-pelan.

**Modelnya.** Y_t = b₀ + b₁·sin(2πt/12) + b₂·cos(2πt/12) + ε_t
- Y_t = hujan pada bulan ke-t (t = 0 untuk Januari 2020, t = 1 Februari 2020, dst.).
- b₀ = tinggi rata-rata gelombang (garis tengah).
- b₁ dan b₂ = angka pengatur tinggi dan posisi gelombang. Dicari dari data.
- ε_t = sisa yang tidak bisa dijelaskan gelombang (hujan tidak pernah persis mengikuti rumus).
- 2π/12 = pengatur supaya gelombang selesai satu putaran tiap 12 bulan.

**Mengapa sinus dan kosinus berdua.** Sinus saja selalu mulai dari nol, kosinus saja selalu mulai dari puncak. Digabung dengan pengali b₁ dan b₂, puncak bisa digeser ke bulan mana pun. Itu sebabnya dua-duanya selalu dipertahankan, walau salah satu koefisien kecil.

**Cara membaca gelombang (amplitudo dan fase).**
- A = √(b₁² + b₂²): setengah jarak puncak ke lembah. Puncak = b₀ + A, lembah = b₀ − A.
- φ = atan2(b₁, b₂), puncak pada t = φ/ω dengan ω = 2π/12: bulan berapa puncaknya.
- Konsep: [[Konsep Amplitudo dan Fase]].

**Cara mencari b₀, b₁, b₂.** Dengan OLS: cari tiga angka yang membuat jumlah kuadrat selisih antara data dan kurva sekecil mungkin. Sumber: Astuti dkk. (2018) dan Kotarumalos dkk. (2025). Konsep: [[Konsep Estimasi OLS]].

**Uji F.** Pertanyaannya: gelombang ini nyata, atau kebetulan saja?
- H₀: b₁ = b₂ = 0 (tidak ada pola musiman).
- H₁: paling sedikit satu dari b₁, b₂ tidak nol (ada pola musiman).
- Taraf α = 0,05 (kesalahan 5 persen yang kita relakan).
- Konsep: [[Konsep Hipotesis dan Uji F]].
- Bentuk hipotesis ini mengikuti Darmawan dkk. (2017) dan Purnama (2021); uji F dibaca dari keluaran regresi Excel oleh Azmi dkk. (2020).

**Tidak ada Ljung-Box, ADF, atau uji t.** Sudah dibuang agar laporan sederhana dan karena tidak bisa dihitung di Excel. Jangan menyebutnya lagi.

## 2.5 Ukuran akurasi ramalan
- **Isi:** Akurasi dinilai pada data uji (12 bulan 2025), yang tidak ikut menaksir parameter. Ukurannya RMSE dan MAE; makin kecil makin akurat. Sebagai pembanding, ditetapkan dua ramalan sederhana: rata-rata seluruh data latih untuk semua bulan, dan rata-rata tiap bulan kalender pada data latih. Keduanya dinilai dengan RMSE dan MAE pada data uji yang sama.
- **Artinya:** Rumus harus membuktikan diri pada soal yang belum pernah dilihat. Nilai RMSE baru bermakna kalau ditaruh di samping tebakan sederhana. Model harmonik **belum tentu** menang; kalau kalah atau seri, itu tetap hasil yang sah dan dilaporkan apa adanya.
- **Alasan:** Model bisa sangat cocok pada data yang dipakai membuatnya tetapi gagal pada data baru. Karena itu ujiannya pada 2025. Sumber: Purnama (2021) dan Hadinata dkk. (2026) untuk penilaian pada data uji; Permata dkk. (2024) untuk RMSE.
- Konsep: [[Konsep Data Latih dan Data Uji]], [[Konsep RMSE dan MAE]], [[Konsep Baseline Ramalan Rata-rata]].

## 2.6 Penelitian terdahulu (Tabel 2.1)
- **Isi:** 15 artikel Indonesia tahun 2016–2026 dalam empat kelompok: 5 regresi Fourier/harmonik, 6 analisis spektral/periodogram, 3 Mataram/NTB dengan metode lain, 1 pembagian musim dan kriteria RMSE.
- **Artinya:** Orang lain sudah menemukan periode sekitar 12 bulan di banyak kota, dan komponen Fourier sudah dipakai untuk hujan Indonesia. Penelitian kita berbeda pada data (bulanan BPS Mataram enam tahun), model (k = 1, tiga parameter), dan cara menguji (12 bulan 2025 terhadap ramalan sederhana).
- **Alasan:** Dosen minta tabel minimal 15 artikel. Isi tabel diambil dari abstrak resmi (beberapa angka dari isi PDF) dan tidak boleh dikarang.
- Konsep: [[Konsep Penelitian Terdahulu Harmonik]]. Daftar: [[Tabel 2.1 Penelitian Terdahulu]].

## 2.7 Kerangka pemikiran
- **Isi:** Alur kerja: 72 data → bagi latih/uji → rangkum → bentuk sinus-kosinus → OLS dan uji F → ramal 12 bulan → hitung RMSE dan MAE.
- **Alasan:** Bagian ini wajib bersumber (diadaptasi dari alur Purnama, 2021 dan Kusdarwati, 2023). Gambarnya: [[Gambar 2.1 Kerangka Pemikiran]]. Karena hanya satu variabel, X dan Y terpisah tidak wajib ([[K11 Variabel x dan y tidak wajib]]).

## Kalau ditanya dosen
- *Apa itu regresi harmonik?* Regresi biasa yang variabel bebasnya sinus dan kosinus dari waktu.
- *Kenapa 12?* Karena siklus musim berulang tiap 12 bulan.
- *Apa itu amplitudo?* Seberapa jauh hujan naik dari rata-rata saat puncak.
- *Untuk apa uji F?* Memeriksa gelombang itu nyata atau kebetulan.
- *Kenapa ukuran akurasi pada 2025, bukan data lama?* Agar jujur: model belum pernah melihat 2025.

## Belum beres
- Rumus amplitudo A dan fase φ diturunkan dari identitas trigonometri; belum ada artikel Indonesia yang sudah dibaca yang memuat rumusnya.
- Sudaryono (2021): ISBN terverifikasi; nomor bab dan halaman tidak diperlukan (rumus dihitung sendiri dari data).
- Lihat [[Pertanyaan Terbuka]].

Berikutnya: [[04 Bab III Metode Penelitian]]
