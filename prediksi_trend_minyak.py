import streamlit as st
import pickle
import numpy as np

trend_prediction_model = pickle.load(open('Random_Forest_CPO_Trend_Prediction.sav', 'rb'))

container1 = st.container()

with container1:

    prediksi_harga_penawaran = ''

    st.title('Prediksi Trend Minyak berdasarkan Sentiment')

    china_demand = st.selectbox(
        "**China Demand**",
        (0,-1,1),
    )
    exports = st.selectbox(
        "**Export CPO**",
        (0,-1,1),
    )
    geopolitics = st.selectbox(
        "**Geopolitics**",
        (0,-1,1),
    )
    indian_demand = st.selectbox(
        "**Indian Demand**",
        (0,-1,1),
    )
    inventory = st.selectbox(
        "**Supply/Inventory**",
        (0,-1,1),
    )
    production = st.selectbox(
        "**Production**",
        (0,-1,1),
    )
    weather = st.selectbox(
        "**Weather**",
        (0,-1,1),
    )

    if st.button('Predict Trend Harga Minyak/CPO'):
        prediksi_trend = trend_prediction_model.predict([[china_demand, exports, geopolitics, indian_demand, inventory, production, weather]])                          
        proba = np.max(trend_prediction_model.predict_proba([[china_demand, exports, geopolitics, indian_demand, inventory, production, weather]]))

        if prediksi_trend[0] == 1:
            st.error(f"Prediksi trend harga minyak berdasarkan kondisi diatas adalah **NAIK**, dengan Probabilitas sebesar {proba*100}%")
        else:
            st.success(f"Prediksi trend harga minyak berdasarkan kondisi diatas adalah **TURUN**, dengan Probabilitas sebesar {proba*100}%")