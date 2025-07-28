# Judul Kasus
> *Stock Price Sentiment*

---

## Anggota Kelompok & NIM

| Nama Lengkap         | NIM          |
|----------------------|--------------|
| Dzulkifli Faiz Nurmufid         | 714220030   |
| Ghaida Fasya Yuthika Afifah       | 714220031   |
| Irgi Achmad Fauzi       | 714220035   |
| Kresnanda Randyansyah       | 714220052   |

---

## Deskripsi Kasus

Kasus ini membahas tentang 

---

## Sumber Dataset

- Sumber: [IHSG](https://finance.yahoo.com/quote/%5EJKSE/history/) dan [ID-SMSA](https://data.mendeley.com/datasets/tn4vzs8tdw/3)
- Format: CSV 
- Jumlah data: xxxx entri

---

## Langkah Preprocessing

1. Menghapus nilai kosong (missing values)
2. Case folding (mengubah seluruh teks menjadi huruf kecil)
3. Menghapus tanda baca, angka, dan karakter khusus
4. Tokenisasi
5. Stopword removal
6. Stemming
7. Split data menjadi data latih dan data uji (contoh: 80:20)

---

## Algoritma yang Digunakan

- Naive Bayes
- Support Vector Machine (SVM)


---

## Evaluasi & Hasil

Metode evaluasi yang digunakan:

- Akurasi
- Precision
- Recall
- F1-Score
- Confusion Matrix


| Algoritma         | Akurasi | Precision | Recall | F1-Score |
|-------------------|---------|-----------|--------|----------|
| Naive Bayes       |    |      |   |     |
| SVM               |    |      |   |     |

---

## Cara Menjalankan

## ⚙️ Persiapan

### 1. Clone repositori

git clone https://github.com/username/tugas-besar-datamining-kelompok7.git
cd tugas-besar-datamining-kelompok7

### 2. Buat dan aktifkan virtual environment

python -m venv .venv

Windows:
.venv\Scripts\activate

Linux/macOS:
source .venv/bin/activate

### 3. Install semua dependensi

pip install -r requirements.txt

---

## 🧪 Menjalankan Pipeline

Pastikan dua file berikut tersedia:

- data/processed/IHSG_final.csv
- data/processed/IDSMSA_Final.csv

Lalu jalankan pipeline dengan:

./run.sh

Atau jika kamu menggunakan Windows PowerShell:

.\run.sh

---

