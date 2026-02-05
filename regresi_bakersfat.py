import streamlit as st
import pickle

model_bakersfat = pickle.load(open('regresi_tepung_soft.sav', 'rb'))
# scaler = pickle.load(open('Scaler_Regresi_Minyak_10 nov 2025.pkl', 'rb'))

container1 = st.container()

intercept = -161397.505484519
x_variable = 103.987049819106

with container1:

    prediksi_harga_penawaran = ''

    st.title('Prediksi harga penawaran Bakersfat')

    bursa = st.number_input("Masukkan harga bursa Crude Palm Oil (CPO)")


    if st.button('Predict harga penawaran Bakersfat'):
        prediksi_harga_penawaran = (bursa*x_variable)+intercept                          
        
        # st.subheader(f"Prediksi harga penawaran dari bursa `{bursa}` adalah: ")
        prediksi_include = round(prediksi_harga_penawaran, 2)
        st.success(f"Prediksi harga penawaran dari bursa `{bursa}` adalah: Rp. {round(prediksi_include/1.11,2)},-")
