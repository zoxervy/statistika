---
tipe: bab
tags: [statistika, regresi-harmonik, laporan]
---

# Bab II Kajian Pustaka

Semua subbab bersitasi ([[K10 Bab II wajib bersitasi]]).

## 2.1 Curah Hujan
Hujan adalah peristiwa jatuhnya butiran air dalam bentuk cair atau padat ke permukaan bumi. Curah hujan diukur dalam milimeter (mm); curah hujan 1 mm berarti air hujan setinggi 1 mm tertampung pada permukaan datar seluas 1 m² tanpa meresap, mengalir, atau menguap (Habinuddin dkk., 2019); volume itu setara dengan 1 liter per meter persegi. Di Indonesia, musim hujan umumnya terjadi sekitar November sampai April dan kemarau sekitar Mei sampai Oktober (Permata dkk., 2024); pembagian ini dipakai untuk membandingkan rata-rata musiman.

## 2.2 Deret Waktu
Deret waktu (data runtun waktu) adalah serangkaian pengamatan terhadap suatu peubah yang diukur menurut urutan waktu, misalnya harian atau bulanan (Habinuddin dkk., 2019). Pengamatan yang dibuat berurutan sepanjang waktu itu dianalisis untuk mengenali pola dan meramalkan nilai berikutnya (Zega & Mardiningsih, 2025). Data curah hujan bulanan termasuk deret waktu (Habinuddin dkk., 2019; Zega & Mardiningsih, 2025).

## 2.3 Statistika Deskriptif
Statistika deskriptif merangkum data dengan ukuran pemusatan dan ukuran penyebaran (Sudaryono, 2021). Penelitian curah hujan di Kota Ambon dan Kota Bengkulu juga memulai analisis dengan rata-rata, simpangan baku, nilai minimum, dan nilai maksimum (Kotarumalos dkk., 2025; Syendra Wanti dkk., 2026). Mean adalah jumlah nilai dibagi banyaknya data, median nilai tengah data terurut, dan modus nilai yang paling sering muncul (Sudaryono, 2021). Simpangan baku sampel mengukur sebaran data terhadap mean, dengan pembagi $n-1$ karena data merupakan sampel (Sudaryono, 2021):
$$\bar{x} = \frac{\sum x_i}{n} \qquad s = \sqrt{\frac{\sum (x_i - \bar{x})^2}{n-1}}$$

## 2.4 Regresi Harmonik
Regresi harmonik memakai fungsi sinus dan kosinus (deret Fourier) untuk memodelkan pola periodik (Kusdarwati, 2023; Zega & Mardiningsih, 2025). Untuk data bulanan dengan periode $T = 12$ bulan, frekuensi sudutnya $\omega = 2\pi/12$, dan model orde pertama ($k = 1$) adalah:
$$Y_t = b_0 + b_1 \sin\left(\frac{2\pi t}{12}\right) + b_2 \cos\left(\frac{2\pi t}{12}\right) + \varepsilon_t$$
dengan $Y_t$ curah hujan bulan ke-$t$, $b_0$ intersep, $b_1$ dan $b_2$ koefisien sinus dan kosinus, serta $\varepsilon_t$ galat acak dengan rata-rata nol.

Koefisien ditaksir dengan *Ordinary Least Squares* (OLS), yaitu meminimalkan jumlah kuadrat galat (Astuti dkk., 2018; Kotarumalos dkk., 2025). Analisis harmonik memberikan informasi frekuensi dan amplitudo siklus (Zega & Mardiningsih, 2025). Bentuk gelombangnya ditafsirkan melalui amplitudo $A$ (setengah jarak puncak ke lembah) dan fase $\phi$ (letak puncak dalam setahun); rumusnya diturunkan dari identitas trigonometri:
$$A = \sqrt{b_1^2 + b_2^2} \qquad \phi = \operatorname{atan2}(b_1, b_2) \qquad \text{puncak pada } t = \phi/\omega$$

Pengaruh gelombang tahunan diuji dengan uji F. Hipotesis nolnya $H_0: b_1 = b_2 = 0$ (tidak ada pola musiman) dan hipotesis alternatifnya $H_1$: paling sedikit satu dari $b_1$, $b_2$ tidak nol (ada pola musiman), pada taraf $\alpha = 0{,}05$. Bentuk hipotesis yang sama dipakai untuk menguji ada atau tidaknya pola musiman pada curah hujan oleh Darmawan dkk. (2017) dan Purnama (2021), dan uji F dibaca dari keluaran regresi pada Excel oleh Azmi dkk. (2020). Darmawan dkk. (2017) memakai statistik F berderajat bebas (2, n − 3) untuk pasangan koefisien kosinus dan sinus.

## 2.5 Ukuran Akurasi Peramalan
Akurasi ramalan diukur pada data uji yang tidak dipakai saat menaksir parameter (Purnama, 2021; Hadinata dkk., 2026). Ukuran yang dipakai adalah *Root Mean Square Error* (RMSE) dan *Mean Absolute Error* (MAE) antara nilai aktual ($A_t$) dan ramalan ($F_t$) pada $m$ bulan data uji; makin kecil nilainya, makin akurat ramalannya. RMSE juga dipakai sebagai kriteria pemilihan model oleh Permata dkk. (2024).
$$\text{RMSE} = \sqrt{\frac{\sum (A_t - F_t)^2}{m}} \qquad \text{MAE} = \frac{\sum |A_t - F_t|}{m}$$

Sebagai pembanding, penulis menetapkan dua ramalan sederhana, yaitu rata-rata seluruh data latih untuk semua bulan dan rata-rata tiap bulan kalender pada data latih. Keduanya dinilai dengan RMSE dan MAE pada data uji yang sama, mengikuti cara penilaian ramalan pada data uji di atas (Purnama, 2021; Hadinata dkk., 2026).

## 2.6 Penelitian Terdahulu
[[Tabel 2.1 Penelitian Terdahulu]] merangkum 15 penelitian terdahulu di Indonesia yang terbit tahun 2016–2026. Sebelas di antaranya membahas deret Fourier, regresi harmonik, atau analisis spektral curah hujan; tiga lainnya berlokasi di Kota Mataram dan NTB dengan metode non-harmonik; satu menjadi acuan pembagian musim dan kriteria RMSE. Dengan Astuti dkk. (2018) yang masuk kelompok Fourier, empat penelitian berlokasi di Kota Mataram atau NTB. Isi tabel diringkas dari abstrak masing-masing artikel; beberapa angka rincian data diambil dari isi artikel.

Periode dominan sekitar 12 bulan dilaporkan di Subang, Jayapura, Bandung, Serdang Bedagai, dan tiga kota di Jawa Timur (Susilokarti dkk., 2016; Tulak dkk., 2022; Habinuddin dkk., 2019; Zega & Mardiningsih, 2025; Kusdarwati, 2023), dan komponen harmonik atau Fourier sudah dipakai pada curah hujan Indonesia, termasuk Kota Mataram dan Kota Ambon (Astuti dkk., 2018; Kusdarwati, 2023; Kotarumalos dkk., 2025). Sebagian besar studi peramalan memakai SARIMA atau model pembelajaran mesin. Penelitian ini berbeda dalam tiga hal: data bulanan resmi BPS Kota Mataram selama enam tahun, regresi harmonik k = 1 dengan tiga parameter yang ditafsirkan melalui amplitudo dan fase, serta pengujian ramalan pada 12 bulan tahun 2025 terhadap ramalan sederhana.

## 2.7 Kerangka Pemikiran
Penelitian ini memakai satu variabel, yaitu curah hujan bulanan (univariat), yang dijelaskan oleh fungsi sinus dan kosinus dari waktu. Alurnya ditunjukkan pada [[Gambar 2.1 Kerangka Pemikiran]]: data 72 bulan dibagi menjadi data latih dan data uji, data dirangkum, variabel sinus dan kosinus dibentuk lalu koefisiennya ditaksir dengan OLS dan diuji dengan uji F, kemudian model meramalkan 12 bulan data uji dan akurasinya dinilai dengan RMSE dan MAE.

Berikutnya: [[Bab III Metode Penelitian]]
