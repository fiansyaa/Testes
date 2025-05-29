import streamlit as st
from knn_model import train_model

st.title("📊 Hasil Prediksi")

if 'input_data' in st.session_state:
    model, iris = train_model()
    data = st.session_state['input_data']
    prediction = model.predict(data)
    st.success(f"Hasil prediksi: **{iris.target_names[prediction[0]]}**")
    st.write("Detail input:")
    st.write(data)
else:
    st.warning("Belum ada data input. Silakan isi dulu di halaman 'Input Data Prediksi'.")
