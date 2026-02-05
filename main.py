import pickle
import streamlit as st
import pandas as pd
import sklearn
import xgboost

# regresi_tepung_page = st.Page("regresi_tepung.py", title="Regresi Tepung", icon=":material/add_circle:")
# regresi_coklat_page = st.Page("regresi_coklat.py", title="Regresi Coklat", icon=":material/add_circle:")
# regresi_bakersfat_page = st.Page("regresi_bakersfat.py", title="Regresi Bakersfat", icon=":material/add_circle:")


pages = {
    "Minyak" : [
        st.Page("regresi_minyak.py", title="Regresi Minyak", icon=":material/add_circle:"),
        st.Page("prediksi_trend_minyak.py", title="Prediksi Trend Minyak", icon=":material/add_circle:"),
        st.Page("rekomendasi_beli_minyak.py", title="Rekomendasi Beli Minyak", icon=":material/add_circle:")
    ],
    "Tepung Terigu" : [
        st.Page("regresi_tepung_soft.py", title="Regresi Tepung Soft", icon=":material/add_circle:"),
        st.Page("regresi_tepung_medium.py", title="Regresi Tepung Medium", icon=":material/add_circle:")
    ],
    "Bakersfat" : [
        st.Page("regresi_bakersfat.py", title="Regresi Bakersfat", icon=":material/add_circle:"),
    ],
    "Tepung Coklat" : [
        st.Page("coklat_df700.py", title="Tepung Coklat DF-700", icon=":material/add_circle:"),
        st.Page("coklat_g960.py", title="Tepung Coklat G-960", icon=":material/add_circle:"),
        st.Page("coklat_ak230.py", title="Tepung Coklat AK-230", icon=":material/add_circle:")
    ],
    "USD" : [
        st.Page("rekomendasi_beli_usd.py", title="Rekomendasi USD", icon=":material/add_circle:"),
        st.Page("forecast_usd.py", title="Forecast USD (Range)", icon=":material/add_circle:")
    ]
}

pg = st.navigation(pages)
pg.run()