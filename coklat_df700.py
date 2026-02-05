import streamlit as st
import pickle

model_df700 = pickle.load(open('Regresi_DF 700_21 Jan 2026.sav', 'rb'))
# scaler = pickle.load(open('Scaler_Regresi_Minyak_10 nov 2025.pkl', 'rb'))

container1 = st.container()

with container1:

    prediksi_harga_penawaran = ''

    st.title('Prediksi harga penawaran Tepung Coklat DF-700')

    bursa = st.number_input("Masukkan harga bursa Cocoa")


    if st.button('Predict harga penawaran Tepung Coklat DF-700'):
        prediksi_harga_penawaran = model_df700.predict(([[bursa]]))                          
        
        # st.subheader(f"Prediksi harga penawaran dari bursa `{bursa}` adalah: ")
        prediksi_include = round(prediksi_harga_penawaran[0], 2)
        st.success(f"Prediksi harga penawaran dari bursa `{bursa}` adalah: Rp. {prediksi_include},-")