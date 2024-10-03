import streamlit as st  # Mengimpor Streamlit untuk membangun antarmuka web
from data_handler import save_data  # Mengimpor fungsi save_data dari file data_handler.py untuk menyimpan data pengguna

# Fungsi untuk menampilkan halaman pengguna
def user_page():
    st.title("Halaman Pengguna")  # Menampilkan judul halaman pengguna
    st.write("Selamat datang di halaman pengguna!")  # Menampilkan teks sambutan di halaman pengguna

    # Tombol Logout
    if st.button("Logout"):  # Membuat tombol Logout
        if 'role' in st.session_state:  # Mengecek apakah ada 'role' di session_state
            del st.session_state['role']  # Menghapus 'role' dari session_state ketika logout
        st.session_state['logged_out'] = True  # Mengatur flag bahwa pengguna sudah logout
    
    # Membuat form untuk input data dari pengguna
    with st.form("data_input_form"):  # Membuat form bernama "data_input_form"
        
        # Input tanggal
        date = st.date_input("Enter the date")  # Input tanggal menggunakan widget date_input dari Streamlit
        
        # Input Reach
        reach = st.number_input("Enter reach", min_value=0)  # Input angka untuk Reach, dengan batas minimal 0
        
        # Input Gender L (Male)
        gender_l = st.number_input("Gender L (Male)", min_value=0)  # Input angka untuk gender laki-laki (L), minimal 0
        
        # Input Gender P (Female)
        gender_p = st.number_input("Gender P (Female)", min_value=0)  # Input angka untuk gender perempuan (P), minimal 0
        
        # Input untuk rentang usia
        st.write("Enter reach for each age range")  # Teks untuk mengarahkan pengguna mengisi rentang usia
        
        # Input reach untuk rentang usia 18-24
        age_18_24 = st.number_input("18-24", min_value=0)  # Input angka untuk reach rentang usia 18-24, minimal 0
        
        # Input reach untuk rentang usia 25-34
        age_25_34 = st.number_input("25-34", min_value=0)  # Input angka untuk reach rentang usia 25-34, minimal 0
        
        # Input reach untuk rentang usia 35-44
        age_35_44 = st.number_input("35-44", min_value=0)  # Input angka untuk reach rentang usia 35-44, minimal 0
        
        # Input reach untuk rentang usia 45-54
        age_45_54 = st.number_input("45-54", min_value=0)  # Input angka untuk reach rentang usia 45-54, minimal 0
        
        # Input reach untuk rentang usia 55-64
        age_55_64 = st.number_input("55-64", min_value=0)  # Input angka untuk reach rentang usia 55-64, minimal 0
        
        # Input reach untuk rentang usia 65+
        age_65_plus = st.number_input("65+", min_value=0)  # Input angka untuk reach rentang usia 65 tahun ke atas, minimal 0

        # Tombol submit untuk mengirimkan form
        submitted = st.form_submit_button("Submit")  # Tombol submit untuk mengirimkan data form

        if submitted:  # Mengecek apakah tombol submit ditekan
            # Menyiapkan data yang akan disimpan dalam bentuk dictionary
            data = {
                'Tanggal': date,  # Menyimpan data tanggal dari input
                'Reach': reach,  # Menyimpan data reach dari input
                'Gender (L)': gender_l,  # Menyimpan data gender laki-laki dari input
                'Gender (P)': gender_p,  # Menyimpan data gender perempuan dari input
                'Range Usia 18-24': age_18_24,  # Menyimpan data reach rentang usia 18-24
                'Range Usia 25-34': age_25_34,  # Menyimpan data reach rentang usia 25-34
                'Range Usia 35-44': age_35_44,  # Menyimpan data reach rentang usia 35-44
                'Range Usia 45-54': age_45_54,  # Menyimpan data reach rentang usia 45-54
                'Range Usia 55-64': age_55_64,  # Menyimpan data reach rentang usia 55-64
                'Range Usia 65+': age_65_plus  # Menyimpan data reach rentang usia 65 tahun ke atas
            }

            # Memanggil fungsi save_data untuk menyimpan data ke file atau database
            save_data(data)
            
            # Menampilkan pesan sukses setelah data berhasil disimpan
            st.success("Data saved successfully!")  # Menampilkan pesan bahwa data berhasil disimpan
