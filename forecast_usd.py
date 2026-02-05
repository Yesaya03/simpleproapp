import streamlit as st
import pickle
import numpy as np

model_usd = pickle.load(open('Model_Kurs_Linear_Regression_29_jan_2026_var.pkl', 'rb'))
scaler = pickle.load(open('scaler_kurs_USD_Linear_Regression_29_jan_2026.pkl', 'rb'))

container1 = st.container()

with container1:

    prediksi_harga_penawaran = ''

    st.title('Rekomendasi Pembelian USD')

    kurs = st.number_input("**Masukkan Kurs USD**")
    cpi = st.number_input("**Masukkan Inflasi CPI (US)**")
    pce = st.number_input("**Masukkan Inflasi PCE (US)**")
    inflasi_indo = st.number_input("**Masukkan Inflasi Indonesia**")
    nfp = st.number_input("**Masukkan Non Farm Payroll (US)**")
    unemployment_rate = st.number_input("**Masukkan Unemployment Rate (US)**")
    initial_jobless = st.number_input("**Masukkan Initial Jobless Claims (US)**")
    interest_rates = st.number_input("**Masukkan Interest Rates**")
    china_inflation = st.number_input("**Masukkan Inflasi China**")
    us_retail_data = st.number_input("**Masukkan US Retail Data**")
    gdp = st.number_input("**Masukkan GDP US**")

    if st.button('**Rekomendasi Pembelian USD**'):
            
        forecast = model_usd.predict(scaler.transform([[kurs,cpi,pce, inflasi_indo,nfp,unemployment_rate, initial_jobless,interest_rates,china_inflation,us_retail_data,gdp]]))
        error = 80

        batas_atas = forecast + error
        batas_bawah = forecast - error

        st.success(f"**Batas atas Forecast adalah: {batas_atas[0]}**")

        st.success(f"**Batas bawah Forecast adalah: {batas_bawah[0]}**")