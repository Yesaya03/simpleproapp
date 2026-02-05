import streamlit as st
import pickle


model_tepung = pickle.load(open('regresi_tepung_soft.sav', 'rb'))
# scaler = pickle.load(open('Scaler_Regresi_Minyak_10 nov 2025.pkl', 'rb'))

container1 = st.container()

with container1:

    prediksi_harga_penawaran = ''

    st.title('Prediksi harga penawaran Tepung Terigu Soft')

    bursa = st.number_input("Masukkan harga bursa Wheat")

    usd = st.number_input("Masukkan nilai USD")


    if st.button('Predict harga penawaran Tepung Terigu Soft'):
        prediksi_harga_penawaran = model_tepung.predict(([[bursa, usd]]))
        error_model = 3996                     
        
        # st.subheader(f"Prediksi harga penawaran dari bursa `{bursa}` adalah: ")
        prediksi_include = round(prediksi_harga_penawaran[0], 2)
        st.success(f"Prediksi Harga Penawaran dari bursa `{bursa}` adalah: Rp. {prediksi_include},-")
        st.success(f"Prediksi Harga Negosiasi dari bursa `{bursa}` adalah: Rp. {prediksi_include - error_model},-")
