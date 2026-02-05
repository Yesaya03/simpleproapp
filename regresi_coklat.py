import streamlit as st
import pickle

model_tepung_coklat = pickle.load(open('regresi_tepung_soft.sav', 'rb'))
# scaler = pickle.load(open('Scaler_Regresi_Minyak_10 nov 2025.pkl', 'rb'))

container1 = st.container()

with container1:

    prediksi_harga_penawaran = ''

    st.title('Prediksi harga penawaran Tepung Coklat')

    bursa = st.number_input("Masukkan harga bursa Cocoa")

    usd = st.number_input("Masukkan nilai USD")


    if st.button('Predict harga penawaran Tepung Coklat'):
        prediksi_harga_penawaran = model_tepung_coklat.predict(([[bursa, usd]]))                          
        
        # st.subheader(f"Prediksi harga penawaran dari bursa `{bursa}` adalah: ")
        prediksi_include = round(prediksi_harga_penawaran[0], 2)
        st.success(f"Prediksi harga penawaran dari bursa `{bursa}` adalah: Rp. {prediksi_include},-")
