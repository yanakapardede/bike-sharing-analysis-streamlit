# Proyek Analisis Data: Bike Sharing Dataset

## Informasi Diri

- **Nama:** Yanaka Sofia Pardede
- **Email:** 24031554065@mhs.unesa.ac.id
- **ID Dicoding:** yanaka_sofia_pardede

---

## Deskripsi Proyek

Proyek ini merupakan analisis data penyewaan sepeda (*Bike Sharing Dataset*) yang bertujuan untuk memahami pola penggunaan sepeda berdasarkan faktor lingkungan, seperti musim dan kondisi cuaca, serta perbedaan pola penyewaan antara hari kerja (*workingday*) dan hari libur atau akhir pekan (*weekend*).

Analisis dilakukan menggunakan Python melalui beberapa tahapan, mulai dari *data wrangling*, *exploratory data analysis* (EDA), hingga *visualization and explanatory analysis*. Hasil analisis digunakan untuk mengidentifikasi faktor-faktor yang berkaitan dengan jumlah penyewaan sepeda, karakteristik pengguna *casual* dan *registered*, serta pola permintaan berdasarkan waktu.

Sebagai pelengkap, proyek ini juga dilengkapi dengan dashboard interaktif menggunakan Streamlit. Dashboard tersebut menyajikan ringkasan data, perbandingan penyewaan berdasarkan kategori pengguna, serta visualisasi tren penyewaan sepeda sehingga hasil analisis dapat dipahami dengan lebih mudah.

## Pertanyaan Bisnis

Proyek ini berfokus pada dua pertanyaan bisnis utama:

1. Bagaimana perbandingan pola jumlah penyewaan sepeda antara pengguna *casual* dan *registered* berdasarkan kondisi cuaca (*weathersit*) dan musim (*season*) sepanjang tahun 2011–2012?

2. Bagaimana perbandingan rata-rata volume penyewaan sepeda per jam antara hari kerja (*workingday*) dan hari libur atau akhir pekan (*weekend*), khususnya dalam mengidentifikasi lonjakan atau penurunan permintaan minimal 20% pada jam-jam sibuk (*rush hour*) sepanjang tahun 2011–2012 untuk mendukung optimalisasi armada?

## Struktur Direktori

Berikut merupakan struktur direktori proyek:

```text
.
├── dashboard.py          # Source code dashboard Streamlit
├── main_data.csv         # Dataset hasil preprocessing dan cleaning
├── notebook.ipynb        # Notebook analisis data
├── requirements.txt      # Daftar library yang dibutuhkan
└── README.md             # Dokumentasi proyek
```

## Teknologi dan Library

Beberapa teknologi dan library yang digunakan dalam proyek ini antara lain:

- **Python** – Bahasa pemrograman yang digunakan untuk pengolahan dan analisis data.
- **Pandas** – Digunakan untuk manipulasi, pembersihan, dan pengolahan dataset.
- **NumPy** – Mendukung operasi numerik dan perhitungan statistik.
- **Matplotlib** – Digunakan untuk membuat visualisasi data.
- **Seaborn** – Membantu menghasilkan visualisasi statistik.
- **Streamlit** – Digunakan untuk membangun dashboard interaktif.
- **Jupyter Notebook** – Digunakan sebagai lingkungan untuk menjalankan proses analisis data.

## Tahapan Analisis Data

Proyek ini dilakukan melalui beberapa tahapan sebagai berikut:

### 1. Data Wrangling

Tahap ini dilakukan untuk mempersiapkan data sebelum masuk ke proses analisis.

Beberapa proses yang dilakukan meliputi:

- **Gathering Data:** Memuat dua dataset, yaitu dataset harian (`day_df`) dan dataset per jam (`hour_df`).
- **Assessing Data:** Memeriksa struktur data, tipe data, nilai yang hilang (*missing values*), dan data duplikat.
- **Cleaning Data:** Mengonversi kolom tanggal (`dteday`) menjadi tipe data datetime serta memetakan nilai numerik pada kolom `season` dan `weathersit` menjadi kategori yang lebih mudah dipahami.
- **Export Data:** Menyimpan hasil pengolahan data ke dalam file `main_data.csv` untuk digunakan pada tahap analisis selanjutnya.

### 2. Exploratory Data Analysis (EDA)

Tahap EDA dilakukan untuk memahami karakteristik dan pola dalam dataset melalui eksplorasi statistik dan visualisasi.

Beberapa analisis yang dilakukan meliputi:

- Mengeksplorasi ringkasan statistik jumlah penyewaan sepeda.
- Menganalisis perbedaan jumlah penyewaan berdasarkan musim (*season*).
- Mengidentifikasi hubungan antara kondisi cuaca (*weathersit*) dan jumlah penyewaan sepeda.

### 3. Visualization and Explanatory Analysis

Pada tahap ini, data divisualisasikan untuk menjawab pertanyaan bisnis yang telah ditentukan.

Analisis difokuskan pada:

- Membandingkan jumlah penyewaan pengguna *casual* dan *registered* berdasarkan musim dan kondisi cuaca.
- Membandingkan pola penyewaan sepeda per jam antara hari kerja dan hari libur atau akhir pekan.
- Mengidentifikasi jam-jam sibuk (*rush hour*) berdasarkan perubahan volume penyewaan.

### 4. Analisis Lanjutan

Sebagai analisis tambahan, dilakukan eksplorasi terhadap:

- Tren pertumbuhan penyewaan sepeda secara bulanan.
- Hubungan antara faktor lingkungan, seperti suhu, kelembapan, dan kecepatan angin, dengan jumlah penyewaan sepeda.
- Analisis korelasi untuk melihat hubungan antarvariabel dalam dataset.

## Hasil Analisis dan Insight

Berdasarkan proses eksplorasi dan analisis yang telah dilakukan, diperoleh beberapa temuan utama berikut.

### 1. Pola Penyewaan Berdasarkan Musim

- Musim gugur (*Fall*) mencatatkan rata-rata penyewaan tertinggi, yaitu sekitar 5.644 sepeda.
- Musim panas (*Summer*) berada di urutan berikutnya dengan rata-rata sekitar 4.992 sepeda.
- Musim dingin (*Winter*) mencatatkan rata-rata sekitar 4.728 sepeda.
- Musim semi (*Spring*) memiliki rata-rata penyewaan terendah, yaitu sekitar 2.604 sepeda.

Hasil ini menunjukkan bahwa musim memiliki keterkaitan dengan tingkat permintaan penyewaan sepeda.

### 2. Pola Penyewaan Berdasarkan Kondisi Cuaca

- Kondisi cuaca cerah atau sedikit berawan (*Clear/Few Clouds*) memiliki rata-rata penyewaan tertinggi, yaitu sekitar 4.876 sepeda.
- Kondisi cuaca buruk, seperti hujan atau salju ringan (*Light Snow/Rain*), memiliki rata-rata penyewaan yang jauh lebih rendah, yaitu sekitar 1.803 sepeda.

Temuan ini menunjukkan bahwa kondisi cuaca menjadi salah satu faktor lingkungan yang berkaitan dengan keputusan masyarakat untuk menggunakan layanan penyewaan sepeda.

### 3. Perbandingan Pengguna Casual dan Registered

Berdasarkan analisis berdasarkan musim dan kondisi cuaca, pengguna *registered* secara konsisten mendominasi jumlah penyewaan dibandingkan pengguna *casual*.

Hal ini menunjukkan bahwa pengguna terdaftar memiliki kontribusi yang lebih besar terhadap total aktivitas penyewaan sepeda selama periode pengamatan.

### 4. Pola Penyewaan pada Hari Kerja dan Akhir Pekan

- Pada hari kerja (*workingday*), pola penyewaan menunjukkan dua puncak aktivitas (*double peaks*), yaitu pada pagi hari sekitar pukul 07.00–09.00 dan sore hari sekitar pukul 17.00–19.00.
- Pada hari libur atau akhir pekan (*weekend*), penyewaan cenderung lebih merata dan meningkat pada siang hari, terutama sekitar pukul 10.00–16.00.

Perbedaan ini menunjukkan bahwa penyewaan sepeda pada hari kerja cenderung berkaitan dengan aktivitas dan mobilitas sehari-hari, sedangkan pada akhir pekan lebih banyak digunakan untuk aktivitas yang waktunya fleksibel.

### 5. Tren Pertumbuhan dan Korelasi

Analisis tambahan menunjukkan beberapa temuan berikut:

- Volume penyewaan sepeda mengalami peningkatan dari tahun 2011 ke tahun 2012.
- Variabel suhu (`temp` dan `atemp`) memiliki korelasi positif sekitar 0,63 terhadap jumlah penyewaan (`cnt`).
- Variabel kelembapan (`hum`) dan kecepatan angin (`windspeed`) menunjukkan korelasi negatif terhadap jumlah penyewaan.

Temuan ini memberikan gambaran mengenai hubungan antara kondisi lingkungan dan aktivitas penyewaan sepeda.

## Kesimpulan dan Rekomendasi

Berdasarkan hasil analisis, dapat disimpulkan bahwa musim dan kondisi cuaca berkaitan dengan perubahan jumlah penyewaan sepeda. Pengguna *registered* juga memberikan kontribusi yang lebih besar dibandingkan pengguna *casual*.

Selain itu, terdapat perbedaan pola penggunaan yang cukup jelas antara hari kerja dan akhir pekan. Hari kerja menunjukkan dua periode puncak penyewaan pada pagi dan sore hari, sedangkan akhir pekan memiliki pola penyewaan yang lebih merata pada siang hari.

Berdasarkan temuan tersebut, beberapa rekomendasi yang dapat dipertimbangkan adalah:

1. Mengembangkan program loyalitas dan langganan bagi pengguna *registered*, serta memberikan penawaran khusus untuk meningkatkan partisipasi pengguna *casual*.
2. Menjadwalkan pemeliharaan dan perbaikan armada pada periode dengan aktivitas penyewaan yang relatif rendah agar ketersediaan sepeda tetap terjaga pada jam-jam sibuk.
3. Menyesuaikan ketersediaan unit sepeda pada stasiun-stasiun strategis berdasarkan pola permintaan pada hari kerja dan akhir pekan.
4. Memanfaatkan informasi tren penyewaan dan kondisi lingkungan untuk membantu perencanaan kapasitas armada pada periode dengan permintaan tinggi.

## Memulai Proyek (Getting Started)

Untuk menjalankan proyek ini secara lokal, pastikan Python dan pip sudah terpasang pada perangkat.

### 1. Clone Repository

Unduh repository proyek menggunakan perintah berikut:

```bash
git clone https://github.com/yanakapardede/bike-sharing-analysis-streamlit.git
```

Masuk ke direktori proyek:

```bash
cd bike-sharing-analysis-streamlit
```

### 2. Setup Environment - Anaconda

Jika menggunakan Anaconda, buat environment baru dengan Python versi 3.9:

```bash
conda create --name main-ds python=3.9
```

Aktifkan environment:

```bash
conda activate main-ds
```

### 3. Install Dependencies

Install seluruh library yang dibutuhkan menggunakan file `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Setup Environment - Shell/Terminal

Jika tidak menggunakan Anaconda, cukup jalankan perintah berikut pada terminal atau PowerShell di direktori utama proyek:

```bash
pip install -r requirements.txt
```

## Menjalankan Dashboard

Setelah seluruh dependencies berhasil diinstal, jalankan dashboard Streamlit menggunakan perintah:

```bash
streamlit run dashboard.py
```

Setelah perintah dijalankan, aplikasi akan tersedia melalui browser pada alamat:

```text
http://localhost:8501
```

## Dashboard Streamlit

Dashboard analisis penyewaan sepeda juga telah di-deploy menggunakan Streamlit Community Cloud sehingga dapat diakses secara publik tanpa perlu menjalankan aplikasi secara lokal.

**Link Dashboard:**

[Bike Sharing Dashboard App](https://bike-sharing-analysis-app-kjbkxmzbbsnzhkgfqogr6a.streamlit.app/)

---

**Terima kasih telah mengunjungi repository proyek ini.**