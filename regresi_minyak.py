import streamlit as st
import pickle
import pandas as pd

# Load model pipeline
model = pickle.load(open("model_regresi_minyak.pkl", "rb"))

st.title("Prediksi harga penawaran minyak")

bursa = st.number_input("Masukkan harga bursa minyak")
ringgit = st.number_input("Masukkan nilai ringgit")

if st.button("Predict harga penawaran minyak"):
    
    input_df = pd.DataFrame([{
        'HARGA CPO': bursa,
        'RINGGIT': ringgit
    }])

    prediksi = model.predict(input_df)[0]

    harga_pred = round(prediksi, 0)
    max_nego = harga_pred - 98

    st.success(f"Prediksi harga penawaran: Rp {harga_pred:,}")
    st.success(f"Perkiraan maksimal negosiasi: Rp {max_nego:,}")
