import streamlit as st
import pickle


smart_model = pickle.load(open('Linear_Regression_Minyak_10 nov 2025.pkl', 'rb'))
scaler = pickle.load(open('Scaler_Regresi_Minyak_10 nov 2025.pkl', 'rb'))

container1 = st.container()

with container1:

    prediksi_harga_penawaran = ''

    st.title('Prediksi harga penawaran minyak')

    bursa = st.number_input("Masukkan harga bursa minyak")

    ringgit = st.number_input("Masukkan nilai ringgit")


    if st.button('Predict harga penawaran minyak'):
        prediksi_harga_penawaran = smart_model.predict(scaler.transform([[bursa, ringgit]]))                          
        
        # st.subheader(f"Prediksi harga penawaran dari bursa `{bursa}` adalah: ")
        prediksi_include = round(prediksi_harga_penawaran[0], 2)
        max_nego = prediksi_include-98
        st.success(f"Prediksi harga penawaran dari bursa `{bursa}` adalah: Rp. {prediksi_include},-")
        st.success(f"Perkiraan Maksimal negosiasi yang dapat dilakukan adalah: Rp. {max_nego},-")