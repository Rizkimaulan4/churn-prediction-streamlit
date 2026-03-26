# 📊 Customer Churn Prediction App

Aplikasi berbasis Machine Learning untuk memprediksi apakah seorang customer akan churn (berhenti berlangganan) atau tidak.

Project ini mengubah model Machine Learning menjadi aplikasi web interaktif menggunakan Streamlit.

---

## 🌐 Live Demo
Coba langsung tanpa install:

👉 https://churn-prediction-modell.streamlit.app/

---

## 📌 Overview
Project ini bertujuan untuk:
- Mengolah data customer
- Membangun model prediksi churn
- Mengimplementasikan model ke dalam aplikasi web interaktif

Aplikasi ini dirancang agar user non-teknis dapat langsung menggunakan model tanpa perlu coding.

---

## 🚀 Features
- Input data customer secara manual
- Prediksi churn secara real-time
- Visualisasi hasil (tabel & grafik)
- Multi-page app:
  - Overview
  - Prediction
  - Analysis

---

## 🛠 Tech Stack
- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Joblib

---

## 🧑‍💻 Cara Menggunakan (User / Pengunjung)

### 🔹 Versi Online (Paling Mudah)
1. Klik link berikut:
   👉 https://churn-prediction-modell.streamlit.app/
2. Masuk ke halaman **Prediction**
3. Isi data customer
4. Klik tombol **Predict**
5. Lihat hasil prediksi churn

---
## 🧑‍💻 Cara Menjalankan Project Secara Lokal (Full Setup)

Ikuti langkah berikut untuk menjalankan aplikasi di komputer lokal:

# ================================
# 🚀 STEP 1 — CLONE REPOSITORY
# ================================
git clone https://github.com/Rizkimaulan4/churn-prediction-streamlit.git

# ================================
# 📂 STEP 2 — MASUK KE PROJECT
# ================================
cd churn-prediction-streamlit

# ================================
# 🧪 STEP 3 — BUAT VIRTUAL ENV
# ================================
python -m venv venv

# ================================
# ⚡ STEP 4 — AKTIFKAN ENV
# ================================

# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate

# ================================
# 📦 STEP 5 — INSTALL DEPENDENCIES
# ================================
pip install -r requirements.txt

# ================================
# ▶️ STEP 6 — JALANKAN APP
# ================================
streamlit run HOME.py

# ================================
# 🌐 STEP 7 — AKSES DI BROWSER
# ================================
# http://localhost:8501