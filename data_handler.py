import pandas as pd  # Mengimpor pandas untuk manipulasi data
import streamlit as st  # Mengimpor Streamlit untuk membangun antarmuka web

# Fungsi untuk memuat data yang sudah disimpan dari file CSV
def load_data():
    try:
        # Membaca data dari file 'user_input_data.csv' menggunakan pandas
        df = pd.read_csv('user_input_data.csv')
        if df.empty:  # Mengecek apakah DataFrame kosong
            # Mengembalikan DataFrame kosong dengan kolom yang diinginkan jika CSV kosong
            return pd.DataFrame(columns=['Tanggal', 'Reach', 'Gender (L)', 'Gender (P)', 'Range Usia 18-24', 'Range Usia 25-34', 'Range Usia 35-44', 'Range Usia 45-54', 'Range Usia 55-64', 'Range Usia 65+'])
        return df  # Mengembalikan DataFrame yang sudah dibaca jika tidak kosong
    except FileNotFoundError:
        # Jika file CSV tidak ditemukan, mengembalikan DataFrame kosong dengan kolom yang diinginkan
        return pd.DataFrame(columns=['Tanggal', 'Reach', 'Gender (L)', 'Gender (P)', 'Range Usia 18-24', 'Range Usia 25-34', 'Range Usia 35-44', 'Range Usia 45-54', 'Range Usia 55-64', 'Range Usia 65+'])

# Fungsi untuk menyimpan data input baru ke file CSV
def save_data(data):
    # Memvalidasi apakah semua kolom yang diperlukan ada di dalam data yang diberikan
    required_columns = ['Tanggal', 'Reach', 'Gender (L)', 'Gender (P)', 'Range Usia 18-24', 'Range Usia 25-34', 'Range Usia 35-44', 'Range Usia 45-54', 'Range Usia 55-64', 'Range Usia 65+']
    
    for col in required_columns:
        if col not in data:  # Jika ada kolom yang hilang, mengeluarkan error
            raise ValueError(f"Missing required data: {col}")

    # Memuat data yang sudah ada dari CSV
    df = load_data()
    
    # Membuat DataFrame baru dengan data input yang baru
    new_data = pd.DataFrame([data])

    # Menggabungkan data lama dengan data baru, lalu menyimpan ke CSV
    try:
        df = pd.concat([df, new_data], ignore_index=True)  # Menggabungkan data lama dan baru
        df.to_csv('user_input_data.csv', index=False)  # Menyimpan data yang telah digabung ke file CSV
    except Exception as e:
        # Menampilkan pesan error jika terjadi masalah saat menyimpan
        print(f"Error saving data: {e}")
