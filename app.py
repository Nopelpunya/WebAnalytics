import streamlit as st
from login import login
from user import user_page
from admin import admin_page

# Fungsi utama
def main():
     # Membuat kolom untuk gambar dan judul
    col1, col2 = st.columns([1, 3]) 

    with col1:
        image_path = "perindo-removebg-preview.png"  
        st.image(image_path, width=210) 

    with col2:
        # Menambahkan judul halaman
        st.markdown("<h3 style='margin:0;'>Selamat Datang di Halaman Analisis Reach berdasarkan Gender dan Usia</h3>", unsafe_allow_html=True)

    if 'role' not in st.session_state or st.session_state['role'] is None:
        login()  
    else:
        if st.session_state['role'] == 'User':
            user_page()  
        elif st.session_state['role'] == 'Admin':
            admin_page()  

if __name__ == '__main__':
    main()
