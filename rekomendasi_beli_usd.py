import streamlit as st
import pickle
import numpy as np
import xgboost

xgb = pickle.load(open('Model_XGB_Rekomendasi_USD_13 nov 2025.pkl', 'rb'))
scaler = pickle.load(open('Scaler_Rekomendasi_USD_13 nov 2025.pkl', 'rb'))



container1 = st.container()

with container1:

    prediksi_harga_penawaran = ''

    st.title('Rekomendasi Pembelian USD')

    kurs = st.number_input("**Masukkan Kurs USD**")
    estimasi_closing = st.number_input("**Masukkan Estimasi Closing USD**")
    moving_average_30 = st.number_input("**Masukkan Rata-rata USD 30 Hari terakhir**")
    moving_average_14 = st.number_input("**Masukkan Rata-rata USD 14 Hari terakhir**")
    budget = st.number_input("**Masukkan Rata-rata harga Budget USD**")
    last_buy = st.number_input("**Masukkan Harga Beli USD Terakhir**")
    batas_atas = st.number_input("**Masukkan Batas Atas Forecast USD**")
    batas_bawah = st.number_input("**Masukkan Batas Bawah Forecast USD**")

    if st.button('**Rekomendasi Pembelian USD**'):
        kurs_vs_estimasi_closing = (kurs-estimasi_closing)/kurs
        kurs_vs_ma_14 = (kurs-moving_average_14)/moving_average_14
        kurs_vs_ma_30 = (kurs-moving_average_30)/moving_average_30
        kurs_vs_budget = (kurs-budget)/budget
        kurs_vs_last_buy = (kurs-last_buy)/last_buy
        kurs_batas_atas = (kurs-batas_atas)/batas_atas
        kurs_batas_bawah = (kurs-batas_bawah)/batas_bawah
            
        recommendation = xgb.predict(scaler.transform([[kurs_vs_estimasi_closing,kurs_vs_ma_14,kurs_vs_ma_30, kurs_vs_budget,kurs_vs_last_buy,kurs_batas_atas, kurs_batas_bawah]]))
        confidence_level = np.max(xgb.predict_proba(scaler.transform([[kurs_vs_estimasi_closing,kurs_vs_ma_14,kurs_vs_ma_30, kurs_vs_budget,kurs_vs_last_buy,kurs_batas_atas, kurs_batas_bawah]])))

        if recommendation[0] == 1:
            st.success(f"Rekomendasi: **BELI**")
        else:
            st.error(f"Rekomendasi: **HOLD (TIDAK BELI)**")
        st.success(f"Confidence level prediksi adalah: {confidence_level*100}%")