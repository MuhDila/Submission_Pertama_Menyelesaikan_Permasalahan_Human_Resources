# Submission Pertama: Menyelesaikan Permasalahan Human Resources
- **Nama:** Muhammad Dila
- **Email:** muhammaddila.all@gmail.com
- **ID Dicoding:** muhdila

---

# Business Understanding

## Latar Belakang Bisnis

Jaya Jaya Maju adalah perusahaan multinasional yang telah berdiri sejak tahun 2000 dan memiliki lebih dari 1.000 karyawan. Walaupun perusahaan ini cukup besar, mereka menghadapi tantangan serius dalam hal manajemen karyawan, khususnya tingginya tingkat keluar karyawan (attrition) yang mencapai lebih dari 10%. Tingginya angka attrition berdampak langsung terhadap hilangnya talenta, menurunnya produktivitas, serta meningkatnya beban kerja bagi karyawan yang bertahan. 

Manajer departemen HR membutuhkan dukungan berbasis data untuk memahami faktor-faktor yang mendorong keputusan karyawan keluar, dan memerlukan sistem yang dapat memantau tren tersebut secara real-time.

---

## Permasalahan Bisnis

- Tingginya angka karyawan keluar tanpa pemahaman menyeluruh mengenai penyebab utamanya.
- HR kesulitan menganalisis data karyawan dalam jumlah besar secara manual.
- Belum tersedia sistem monitoring berbasis visualisasi data untuk memantau faktor penyebab attrition.
- Tidak adanya sistem prediktif untuk mengidentifikasi karyawan berisiko keluar.

---

## Cakupan Proyek

Proyek ini mencakup:

- Pembersihan dan eksplorasi data karyawan (EDA).
- Analisis faktor-faktor yang memengaruhi attrition (usia, lembur, status pernikahan, dll).
- Pemilihan fitur penting menggunakan korelasi dan feature selection (RFE).
- Pembangunan model prediktif menggunakan 5 algoritma: Logistic Regression, Random Forest, SVM, XGBoost, dan KNN.
- Evaluasi model menggunakan metrik akurasi, recall, dan F1-score.
- Pembuatan business dashboard interaktif di Metabase untuk memvisualisasikan hasil analisis dan insight model.

---

## Persiapan

### **Sumber Data**
Dataset yang digunakan dalam proyek ini berasal dari **[Jaya Jaya Maju Employee Dataset](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee)**. Dataset ini disediakan secara resmi oleh Dicoding sebagai bagian dari studi kasus proyek pertama.

---

### **Setup Lingkungan (Environment Setup)**

Agar seluruh proses analisis, prediksi, dan visualisasi berjalan dengan lancar, berikut adalah langkah-langkah setup yang direkomendasikan:

---

#### 1. **Menjalankan `notebook.ipynb`**
- Pastikan seluruh **library dan dependensi** yang diperlukan telah terinstal (cek file `requirements.txt`).
- Notebook ini dapat dibuka di Google Colab, JupyterLab, atau IDE lokal seperti VSCode.
- Jalankan sel secara berurutan untuk melakukan data exploration, preprocessing, feature selection, modeling, dan evaluasi.

---

#### 2. **Menjalankan `prediction.py`**
- Script ini berfungsi untuk melakukan prediksi pada dataset baru.
- Bisa dijalankan langsung dari terminal atau IDE, pastikan dependensi sudah sesuai dengan `requirements.txt`.
- Edit baris berikut untuk menyesuaikan input:
  ```python
  sample = pd.read_csv('dataset/sample_data.csv')  # Ganti path sesuai file yang ingin diprediksi


---

#### **3. Menjalankan Dashboard**
Untuk melihat **dashboard** secara langsung, Anda dapat menggunakan **Metabase** dengan bantuan **Docker**. Pastikan **Docker** telah terpasang di sistem Anda.

**Langkah-langkah untuk menjalankan Metabase menggunakan Docker**:
1. **Tarik (pull) image Metabase dari Docker Hub** dengan perintah:
   ```bash
   docker pull metabase/metabase:latest
   ```

2. **Jalankan container Metabase** dengan perintah:
   ```bash
   docker run -p 3000:3000 --name metabase metabase/metabase
   ```

3. **Login ke Metabase** menggunakan kredensial berikut:
   - **email**: `root@mail.com`
   - **Password**: `root123`
   - atau
   - **Username**: `muhammaddila.all@gmail.com`
   - **email**: `313200863MuhDila`

Dengan mengikuti langkah-langkah ini, Anda dapat memulai **analisis data** dan **dashboard**, serta melihat hasil visualisasi langsung di **Metabase**.

---

# Business Dashboard

Business dashboard ini dibuat menggunakan **Metabase** untuk memberikan visualisasi interaktif yang membantu departemen HR dalam memahami pola dan faktor yang mempengaruhi tingginya tingkat keluar karyawan (attrition) di perusahaan **Jaya Jaya Maju**.

## Tujuan Dashboard
Dashboard ini berfungsi untuk:
- Menampilkan komposisi karyawan yang keluar dan bertahan.
- Memvisualisasikan faktor-faktor utama penyebab attrition berdasarkan hasil model machine learning.
- Menyajikan distribusi attrition berdasarkan kategori penting seperti umur, gender, status pernikahan, job role, jarak rumah, gaji bulanan, dan overtime.

## Tampilan Dashboard

![HR Dashboard](muhdila-dashboard.png)

## Fitur-Fitur Dashboard:
- **Pie Chart Attrition**: Menunjukkan persentase karyawan keluar (16.9%) vs bertahan (83.1%).
- **Top Faktor Penyebab Keluar**: Seperti lembur (OverTime), total tahun pengalaman kerja, dan pendapatan bulanan.
- **Distribusi Attrition** berdasarkan:
  - Umur: Karyawan usia 25–35 tahun paling banyak keluar.
  - Gender: Laki-laki lebih dominan secara populasi dan attrition.
  - Status Pernikahan: Single memiliki tingkat attrition tertinggi.
  - Job Role: Sales Representative dan Lab Technician memiliki tingkat keluar paling tinggi.
  - Gaji: Income rendah berkorelasi dengan keluar.
  - Jarak: Karyawan dengan jarak rumah >10 km lebih berisiko keluar.
  - OverTime: Karyawan lembur jauh lebih rentan keluar.

## Akses Dashboard
Dashboard ini dapat diakses melalui Metabase secara lokal:

- **Email**: `muhammaddila.all@gmail.com`
- **Password**: `313200863MuhDila!`
- **URL lokal**: [http://localhost:3000](http://localhost:3000)

Dashboard ini juga telah diekspor dalam bentuk file database `.mv.db` dan disertakan dalam submission.

# Conclusion

Proyek ini berhasil menyelesaikan tantangan utama dalam manajemen sumber daya manusia, khususnya dalam memahami dan memprediksi **attrition** atau tingkat keluarnya karyawan dari perusahaan **Jaya Jaya Maju**.

Dari hasil analisis data dan modeling, ditemukan bahwa faktor-faktor seperti **OverTime**, **MonthlyIncome**, **TotalWorkingYears**, dan **JobLevel** memiliki pengaruh paling signifikan terhadap keputusan karyawan untuk keluar.

Model terbaik yang digunakan untuk memprediksi attrition adalah **XGBoost**, dengan performa sebagai berikut:
- **Akurasi**: 82.55%
- **Recall** (kelas attrition): 42%
- **F1-Score**: 0.45

Dashboard interaktif juga telah dibuat menggunakan **Metabase**, yang memberikan insight visual secara langsung dan mudah dipahami oleh tim HR, seperti distribusi berdasarkan umur, jabatan, jarak rumah, dan status pernikahan.

Dengan pemahaman berbasis data dan model prediktif ini, perusahaan kini memiliki alat bantu untuk:
- Mengawasi kondisi workforce secara real-time.
- Mengidentifikasi karyawan berisiko tinggi keluar.
- Menyusun strategi retensi yang lebih efektif.

---

# Rekomendasi Action Items

Berikut adalah beberapa tindakan strategis yang dapat dilakukan oleh perusahaan berdasarkan hasil proyek:

- **Kurangi Beban Lembur (OverTime):**  
  Karyawan yang sering lembur menunjukkan tingkat attrition yang jauh lebih tinggi. Perusahaan sebaiknya meninjau kembali kebijakan lembur dan mempertimbangkan fleksibilitas kerja.

- **Tinjau Struktur Kompensasi:**  
  Karyawan dengan penghasilan rendah lebih rentan untuk keluar. Perusahaan perlu menyesuaikan struktur gaji agar lebih kompetitif dan adil, khususnya untuk karyawan baru dan di level jabatan rendah.

- **Fokus pada Karyawan Muda dan Single:**  
  Karyawan berusia 25–35 tahun dan belum menikah memiliki risiko keluar lebih tinggi. Intervensi seperti coaching karier dan program pengembangan diri bisa membantu retensi.

- **Gunakan Model Prediktif Secara Aktif:**  
  Integrasikan model prediksi attrition ke sistem HRIS untuk mendeteksi karyawan berisiko secara berkala, dan lakukan pendekatan personal untuk mencegah resign.

- **Perbaiki Lingkungan Kerja dan Keterlibatan:**  
  Faktor seperti JobSatisfaction dan EnvironmentSatisfaction juga berpengaruh. Meningkatkan komunikasi internal, transparansi manajerial, dan kejelasan jenjang karier bisa berdampak positif.

---

Dengan penerapan rekomendasi ini, diharapkan perusahaan mampu menurunkan tingkat attrition secara signifikan dan mempertahankan talenta terbaik.

