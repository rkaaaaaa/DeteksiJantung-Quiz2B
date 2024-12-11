import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import os

# Gejala-Gejala dan penyakit berdasarkan Data dari QUIZ 2B
gejala = [
    "Nyeri dada", "Bahu kiri terasa tidak enak", "Keringat dingin", "Sesak nafas",
    "Gangguan pencernaan", "Mual", "Detak jantung tidak teratur", "Pusing",
    "Kaki bengkak", "Jantung berdebar-debar", "Mudah lelah", "Nyeri di daerah dada tengah",
    "Mudah berkeringat", "Dada mengencang", "Pembengkakan pada jantung", "Kelainan fungsi hati",
    "Pendarahan dari hidung", "Wajah kemerahan", "Batuk", "Sakit perut",
    "Detak jantung cepat", "Nyeri di daerah lengan kiri", "Punggung terasa tidak enak", "Sakit kepala"
]

penyakit = {
    "Penyakit Jantung Koroner": ["Nyeri dada", "Bahu kiri terasa tidak enak", "Keringat dingin", "Sesak nafas", 
    "Gangguan pencernaan", "Mual", "Detak jantung tidak teratur", "Nyeri di daerah lengan kiri", "Punggung terasa tidak enak"],
    "Penyakit Otot Jantung (Kardiomiopati)": ["Sesak nafas", "Pusing", "Kaki bengkak", "Jantung berdebar-debar", "Mudah lelah", "Detak jantung tidak teratur"],
    "Penyakit Jantung Iskemik": ["Nyeri di daerah dada tengah", "Mudah berkeringat", "Dada mengencang", "Nyeri di daerah lengan kiri", "Penebalan tendon achiles"],
    "Gagal Jantung": ["Sesak nafas", "Pembengkakan pada jantung", "Kelainan fungsi hati"],
    "Penyakit Jantung Hipertensi": ["Sakit kepala", "Pendarahan dari hidung", "Pusing", "Wajah kemerahan", "Mudah lelah"],
    "Penyakit Katup Jantung": ["Mudah lelah", "Jantung berdebar-debar", "Nyeri dada", "Sesak nafas", "Batuk", "Kaki bengkak"],
    "Penyakit Jantung Hipertrofik (Kardiomegali)": ["Sakit perut", "Detak jantung tidak teratur", "Detak jantung cepat", "Nyeri dada"]
}

def deteksi_page(user):
    st.set_page_config(page_title="Deteksi Awal Penyakit Jantung", page_icon="❤️")

    # Header aplikasi
    st.markdown("""
    <style>
        .main-header {
            background-color: #ff6347; /* Warna latar belakang header */
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            color: white;
        }
        .main-description {
            margin-top: 20px;
            font-size: 1.2rem;
            color: #ffffff;
        }
    </style>
    <div class="main-header">
        <h1>🩺 Deteksi Awal Penyakit Jantung</h1>
    </div>
    """, unsafe_allow_html=True)

    # Sambutan untuk pengguna
    st.write(f"Selamat datang, {user['nama']}! Semoga Anda sehat selalu.")

    # Deskripsi aplikasi
    st.markdown("""
    <div class='main-description'>
        Aplikasi ini menggunakan gejala-gejala yang Anda alami untuk mendeteksi kemungkinan penyakit jantung yang Anda alami. Silakan pilih gejala-gejala yang Anda rasakan.
    </div>
    """, unsafe_allow_html=True)

    # Menambahkan gambar dari folder yang sama
    if os.path.exists("rs.jpg"):
        st.image("rs.jpg", use_container_width=True)
    else:
        st.write("Gambar tidak ditemukan. Pastikan file 'rs.jpg' ada di folder yang sama dengan file ini.")

    st.write("---")

    # Input user
    gejala_terpilih = st.multiselect("Pilih gejala yang Anda rasakan:", gejala)

    if gejala_terpilih:
        # Proses deteksi penyakit dengan persentase kecocokan tertinggi
        hasil = {}
        for penyakit_name, gejala_penyakit in penyakit.items():
            jumlah_gejala = len(gejala_penyakit)
            cocok = sum(1 for gejala in gejala_penyakit if gejala in gejala_terpilih)
            persentase_cocok = (cocok / jumlah_gejala)
            hasil[penyakit_name] = persentase_cocok

        # Tentukan penyakit dengan persentase kecocokan tertinggi
        penyakit_tertinggi = max(hasil, key=hasil.get) if hasil else None

        st.write("---")

        # Tampilkan hasil
        if st.button("Deteksi Penyakit"):
            if penyakit_tertinggi:
                gejala_input = ", ".join(gejala_terpilih)
                st.write(f"Dari data yang Anda inputkan ({gejala_input}), Anda mungkin mengalami: {penyakit_tertinggi}")
            else:
                st.write("Gejala yang Anda alami tidak sesuai dengan penyakit jantung yang terdaftar.")
    else:
        st.write("Silakan pilih gejala yang anda rasakan dengan jujur untuk melanjutkan deteksi awal penyakit jantung.")

    st.write("---")