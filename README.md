# Car Price Prediction
__Kelompok 07__
* Hardy Valenthio Amansyah (18218004)
* Adi Hendro (18218009)
* Kanisius Sosrodimardito (18218044)
* Iman-Budi Pranakasih (10118004)

---

## Permasalahan
### 01. Deskripsi Organisasi / Perusahaan
__PT. Naga Alam Semesta__
* Perusahaan Jual/Beli Mobil Bekas, Melayani Tukar/Tambah dan Cash/Credit. 
* Terdiri atas 3 cabang fisik, seluruhnya terletak di Bekasi. 
* Terdapat 4 kepala cabang. 


### 02. Penentuan Masalah Bisnis
__Problem__

Perusahaan sering merugi karena tidak dapat menentukan harga jual yang cocok.
<!-- * Terkadang dialokasikan anggaran perbaikan yang terlalu tinggi pada mobil bekas dagangan sehingga rugi ketika dijual. -->
* Terkadang perusahaan menjual mobil dibawah harga beli + perbaikan sehingga rugi.

__Question__
<!-- * Bagaimana cara memprediksi biaya perbaikan mobil sesuai harga beli mobil untuk mendapat keuntungan optimal? -->
* Bagaimana cara memprediksi harga jual dari modal?

__Measurable Outcomes__
* Menekan angka kerugian
* Meningkatkan keuntungan

__Solusi yang Diajukan__
* Membuat aplikasi sederhana yang menganjurkan harga jual mobil berdasarkan anggaran modal mobil bekas itu. Harga modal mobil bekas = Harga beli + Harga perbaikan.

### 03. Menentukan Tugas Analitik dan Menentukan Kebutuhan Data
* __Tugas Analitik__: Untuk memprediksi harga jual mobil, dapat menggunakan __regresi__
* __Metriks Performansi__: Ukuran keberhasilan dari proses data tersebut menggunakan __Root Mean Squared Error__ dengan angka yang mendekati 1 semakin bagus.

__Struktur Data__

* __Modal (Harga Beli + Perbaikan)__: Harga modal merupakan harga mobil ketika dibeli oleh perusahaan, sedangkan harga perbaikan adalah biaya yang dialokasikan untuk memperbaiki mobil bekas yang akan dijual. 
* __Harga Jual__: Harga jual merupakan harga mobil yang akan dijual. Harga jual ini dapat dipatok oleh perusahaan.
* __Profit__: Selisih dari Harga Jual dan Modal adalah Profit. Selisih antara kedua data tersebut dapat bernilai positif (laba) atau bernilai negatif (rugi).

__Jumlah Data__

* Laporan penjualan, 200 entri

__Sumber Data__
* Internal: 
  * Data laporan penjualan bulanan, minimal 3 tahun terakhir
  * Data laporan pembelian bulanan, minimal 3 tahun terakhir atau data stok barang bulanan
* Eksternal: __Jika kurang dan diperlukan__, meminta data laporan jual-beli dari Perusahaan Jual-Beli Mobil Bekas Lainnya sebagai data referensi.

## Cara Akses
Gunakan URL http://aib-app.herokuapp.com/ untuk mengakses halaman demo. Perlu diingat bahwa demo dideploy menggunakan heroku sehingga membutuhkan waktu untuk "menyalakan" layanan tersebut. Kira-kira tunggu selama 1 hingga 5 menit.

## Data untuk dicobakan ke webnya
Data untuk dicobakan ke webnya hanya mengandung satu field saja, yaitu harga modal mobil bekas (harga beli + perbaikan) mobil dalam satuan rupiah (Rp). Untuk modal harga mobil bekas itu sendiri merupakan data __numerik__ dengan range rekomendasi harga dari Rp40.000.000 hingga Rp300.000.000.

Kami tidak memperhitungkan atribut-atribut mobil lainnya seperti tipe mobil, tahun mobil, tipe transmisi, dan lain sebagainya.

Anda dapat menggunakan harga beli mobil sebagai berikut:
* 60000000
* 100000000
* 132750000
* 188200000
* 255000000
* 297100000

## Links
* __Notebook__: https://colab.research.google.com/drive/1e9hsreBDfY_F8jzRHkarlVqjDvQPadsS?usp=sharing
* __Demo URL__: http://aib-app.herokuapp.com/ (Mohon menunggu mesin heroku menyala)
* __Source data mentah__: https://drive.google.com/drive/folders/1AkNrAXd5UTqfbehNZ8D7U-q5tiQaHlQk?usp=sharing 
* __Source data setelah diproses__: https://gist.githubusercontent.com/ibpme/e53a1b1a59028326da632c5b8d75b77c/raw/362bbb9f78bdc1f2f4fad604662ae69bc0814ca9/02-12-21-AIB-7.csv