import streamlit as st
import numpy as np

st.title("📥 Input Data Prediksi")

# Ambil input dari user
sepal_length = st.slider('Sepal Length', 4.0, 8.0, 5.0)
sepal_width = st.slider('Sepal Width', 2.0, 4.5, 3.0)
petal_length = st.slider('Petal Length', 1.0, 7.0, 4.0)
petal_width = st.slider('Petal Width', 0.1, 2.5, 1.0)

# Simpan data ke session_state agar bisa dipakai di halaman lain
st.session_state['input_data'] = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

st.info("Data siap. Silakan buka halaman 'Hasil Prediksi' di menu.")
