import streamlit as st
from login import login_page
from SistemDeteksiJantung import deteksi_page

# Menjalankan aplikasi
if "user" in st.session_state:
    deteksi_page(st.session_state["user"])
else:
    login_page()
