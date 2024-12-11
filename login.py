import streamlit as st

def login_page():
    st.markdown("""
    <style>
        .main-header {
            background-color: #ff6347; /* Warna latar belakang header */
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            color: white;
        }
        .login-description {
            margin-top: 20px;
            font-size: 1.2rem;
            color: #ffffff;
        }
    </style>
    <div class="main-header">
        <h1>🩺 Sistem Pakar Deteksi Penyakit Jantung</h1>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    
    st.markdown("""
    <div class='login-description'>
        Selamat datang! Silakan masukkan informasi Anda untuk login.
    </div>
    """, unsafe_allow_html=True)
    
    nama = st.text_input("Nama", key="nama")
    umur = st.text_input("Umur", key="umur")
    asal = st.text_input("Asal", key="asal")
    
    if st.button("Login"):
        if nama and umur and asal:
            st.session_state["user"] = {"nama": nama, "umur": umur, "asal": asal}
            st.session_state["page"] = "deteksi"  # Set flag for redirection
            st.success(f"Selamat datang, {nama}! Anda berhasil login, klik login lagi yaa untuk lanjut di halaman deteksi ")
        else:
            st.error("Harap isi semua kolom untuk melanjutkan.")
