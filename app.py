import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load model
model = joblib.load("obesity_model.pkl")

# Encoding kategori ke angka
gender_map = {"Male": 1, "Female": 0}
yes_no_map = {"yes": 1, "no": 0}
calc_map = {"no": 0, "Sometimes": 1, "Frequently": 2, "Always": 3}
caec_map = {"no": 0, "Sometimes": 1, "Frequently": 2, "Always": 3}
mtrans_map = {
    "Public_Transportation": 0,
    "Automobile": 1,
    "Walking": 2,
    "Motorbike": 3,
    "Bike": 4
}

# Judul aplikasi
st.title("Prediksi Tingkat Obesitas")

# Input dari pengguna
age = st.number_input("Umur", min_value=1, max_value=100)
gender = st.selectbox("Jenis Kelamin", list(gender_map.keys()))
height = st.number_input("Tinggi Badan (meter)", min_value=0.5, max_value=2.5, step=0.01)
weight = st.number_input("Berat Badan (kg)", min_value=10.0, max_value=300.0, step=0.1)
favc = st.selectbox("Sering makan makanan tinggi kalori (FAVC)?", list(yes_no_map.keys()))
fcvc = st.slider("Frekuensi konsumsi sayur per hari", 0.0, 3.0, step=0.1)
ncp = st.slider("Jumlah makanan utama per hari", 1.0, 4.0, step=0.1)
scc = st.selectbox("Periksa konsumsi kalori (SCC)?", list(yes_no_map.keys()))
smoke = st.selectbox("Merokok?", list(yes_no_map.keys()))
ch2o = st.slider("Jumlah air yang diminum per hari", 0.0, 3.0, step=0.1)
family_history = st.selectbox("Riwayat keluarga overweight?", list(yes_no_map.keys()))
faf = st.slider("Aktivitas fisik mingguan", 0.0, 3.0, step=0.1)
tue = st.slider("Waktu pakai perangkat elektronik per hari", 0.0, 2.0, step=0.1)
calc = st.selectbox("Konsumsi alkohol", list(calc_map.keys()))
caec = st.selectbox("Konsumsi makanan antara waktu makan", list(caec_map.keys()))
mtrans = st.selectbox("Transportasi utama", list(mtrans_map.keys()))

# Tombol prediksi
if st.button("Prediksi"):
    # Encode input
    encoded_input = [
        age,
        gender_map[gender],
        height,
        weight,
        calc_map[calc],
        yes_no_map[favc],
        fcvc,
        ncp,
        yes_no_map[scc],
        yes_no_map[smoke],
        ch2o,
        yes_no_map[family_history],
        faf,
        tue,
        caec_map[caec],
        mtrans_map[mtrans]
    ]

    # Konversi ke array dan prediksi
    input_array = np.array([encoded_input])
    prediction = model.predict(input_array)[0]

    st.success(f"Prediksi tingkat obesitas: **{prediction}**")
