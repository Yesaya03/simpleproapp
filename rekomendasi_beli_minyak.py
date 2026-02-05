import streamlit as st
import pickle
import numpy as np

# gradient_boost = pickle.load(open('rekomendasi_GB_minyak_200524.pkl', 'rb'))
log_reg = pickle.load(open('rekomendasi_LR_minyak_200524.pkl', 'rb'))
scaler = pickle.load(open('scaler_rekomendasi_minyak_minmax_200524.pkl', 'rb'))

container1 = st.container()

with container1:

    prediksi_harga_penawaran = ''

    st.title('Rekomendasi Pembelian Minyak')

    harga_minyak = st.number_input("**Masukkan Harga Beli Minyak**")
    budget = st.number_input("**Masukkan Budget Pembelian Minyak**")
    moving_average_30 = st.number_input("**Masukkan Rata-rata harga Minyak 30 Hari terakhir**")
    last_buy = st.number_input("**Masukkan Harga Beli Minyak Terakhir**")
    jumlah_sisa_po = st.number_input("**Masukkan Jumlah Sisa PO (dalam kg)**")
    prediksi_trend = st.selectbox(
        "**Masukkan Prediksi Trend Minyak**",
        ("NAIK","TURUN"),
    )
    confidence_level_prediksi = st.number_input("**Masukkan Probabilitas Prediksi Trend Minyak**")

    if st.button('**Rekomendasi Pembelian Minyak**'):
        budget_vs_est_deal = (harga_minyak-budget)/budget
        penawaran_vs_MA = (harga_minyak-moving_average_30)/moving_average_30
        last_buy_vs_est_deal = (harga_minyak-last_buy)/last_buy
        sisa_po = (jumlah_sisa_po-140000)/140000

        if prediksi_trend == "NAIK":
            prediksi_trend_minyak = 1
        else:
            prediksi_trend_minyak = 0
            
        recommendation = log_reg.predict(scaler.transform([[budget_vs_est_deal,prediksi_trend_minyak,confidence_level_prediksi, penawaran_vs_MA,last_buy_vs_est_deal,sisa_po]]))
        confidence_level = np.max(log_reg.predict_proba(scaler.transform([[budget_vs_est_deal,prediksi_trend_minyak,confidence_level_prediksi, penawaran_vs_MA,last_buy_vs_est_deal,sisa_po]])))

        if recommendation == 1:
            if jumlah_sisa_po > 400000:
                # print("Rekomendasi: Tidak Beli")
                st.error(f"Rekomendasi: **HOLD (TIDAK BELI)**")
            elif confidence_level > 0.8:
                st.success(f"Rekomendasi: BELI ")
                st.success(f"Rekomendasi Quantity: BELI QUANTITY BANYAK")
                # print("Rekomendasi: ", recommendation)
                # print("Rekomendasi Quantity: Beli Quantity Banyak")
            else:
                st.success(f"Rekomendasi: BELI")
                st.success(f"Rekomendasi Quantity: BELI QUANTITY SEDIKIT")
                # print("Rekomendasi: ", recommendation)
                # print("Rekomendasi Quantity: Beli Quantity Secukupnya")
        else:
            if jumlah_sisa_po < 70000:
                st.success(f"BELI QUANTITY SEDIKIT")
                # print("Beli Quantity Sedikit")
            else:
                st.error(f"Rekomendasi: **HOLD (TIDAK BELI)**")
        st.success(f"Confidence level prediksi adalah: {confidence_level*100}%")
                # print("Rekomendasi: ", recommendation)
                # print("Confidence level prediksi adalah: ",confidence_level)