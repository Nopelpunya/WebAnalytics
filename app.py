import streamlit as st  # Mengimpor modul Streamlit untuk membangun antarmuka web
from login import login  # Mengimpor fungsi login dari file login.py untuk menangani proses login
from user import user_page  # Mengimpor fungsi user_page dari file user.py untuk halaman pengguna (User)
from admin import admin_page  # Mengimpor fungsi admin_page dari file admin.py untuk halaman admin (Admin)

# Fungsi utama
def main():
    # Membuat dua kolom pada halaman, col1 lebih kecil (1) dan col2 lebih besar (3) untuk tata letak
    col1, col2 = st.columns([1, 3]) 

    # Bagian kolom 1 akan menampilkan gambar logo
    with col1:
        image_path = "perindo-removebg-preview.png"  # Lokasi gambar yang akan ditampilkan
        st.image(image_path, width=210)  # Menampilkan gambar dengan lebar 210 piksel

    # Bagian kolom 2 akan menampilkan judul halaman
    with col2:
        # Menampilkan teks sebagai judul halaman menggunakan HTML dan Streamlit's markdown
        st.markdown("<h3 style='margin:0;'>Selamat Datang di Halaman Analisis Reach berdasarkan Gender dan Usia</h3>", unsafe_allow_html=True)

    # Mengecek apakah variabel 'role' ada di session_state dan sudah terisi
    if 'role' not in st.session_state or st.session_state['role'] is None:
        login()  # Jika belum login (tidak ada role), arahkan pengguna ke halaman login
    else:
        # Jika pengguna sudah login, periksa peran mereka
        if st.session_state['role'] == 'User':
            user_page()  # Jika role adalah 'User', tampilkan halaman untuk pengguna
        elif st.session_state['role'] == 'Admin':
            admin_page()  # Jika role adalah 'Admin', tampilkan halaman untuk admin

# Memanggil fungsi main() ketika aplikasi dijalankan
if __name__ == '__main__':
    main()  # Fungsi utama dipanggil saat aplikasi Streamlit dieksekusi
