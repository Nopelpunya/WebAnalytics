import streamlit as st

def login():
    # Menampilkan judul "Login" dengan format HTML
    # 'unsafe_allow_html=True' digunakan agar Streamlit mengizinkan rendering HTML secara langsung
    st.markdown("<h5 style='margin:0;'>Login</h5>", unsafe_allow_html=True)
    
    # Membuat dropdown atau selectbox untuk memilih peran (role) yang diinginkan oleh pengguna
    # Pilihan yang tersedia adalah 'User' dan 'Admin'
    role = st.selectbox("Select your role", ['User', 'Admin'])
    
    # Membuat tombol 'Login'. Saat tombol ditekan, logika login akan dijalankan
    if st.button('Login'):
        # Menyimpan role yang dipilih pengguna ke dalam session state
        # 'st.session_state' digunakan untuk menyimpan data antar interaksi (stateful)
        st.session_state['role'] = role
    
    # Mengecek apakah role sudah tersimpan di session state
    # Jika ya, menampilkan pesan bahwa pengguna telah login sebagai role yang dipilih
    # Jika tidak, meminta pengguna untuk memilih peran dan login
    if st.session_state.get('role'):
        st.write(f"You are logged in as {st.session_state['role']}")
    else:
        st.write("Please select your role and log in.")
