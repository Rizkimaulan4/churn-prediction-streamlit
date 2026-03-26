import streamlit as st
import pandas as pd
import numpy as np
import joblib
import warnings
warnings.filterwarnings("ignore")
st.set_page_config(
    page_title="Data Science Portfolio",
    page_icon="📊",
    layout="wide"
)

# LOAD MODEL
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
encoder = joblib.load("encoder.pkl")

# UI
st.title("👋 Selamat Datang di Portfolio Rizki Maulana")
st.write(""" 
Website ini menampilkan project Machine Learning yang telah saya buat.

🔹 Fokus: Prediksi Churn Customer  
🔹 Tools: Python, Scikit-Learn, Streamlit  
🔹 Tujuan: Mengubah model ML menjadi aplikasi web interaktif
""")

st.image("WhatsApp Image 2026-02-07 at 17.16.27.jpeg", use_container_width=True)

st.info("Gunakan menu di kiri untuk membuka halaman selanjutnya.")