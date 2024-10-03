import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from data_handler import load_data, save_data
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

def admin_page():
    st.title("Admin Dashboard")  # Menampilkan judul di halaman dashboard

    # Tombol Logout
    if st.button("Logout"):  # Membuat tombol untuk logout
        if 'role' in st.session_state:  # Memeriksa apakah 'role' tersimpan di session_state
            del st.session_state['role']  # Menghapus 'role' dari session_state untuk mengakhiri sesi login
        st.session_state['logged_out'] = True  # Menandai bahwa pengguna telah logout

    # Opsi Sidebar
    option = st.sidebar.selectbox("Pilih Opsi", ["Lihat Data", "Perbarui Data", "Hapus Data", "Visualisasi", "Prediksi"])  
    # Menampilkan menu dropdown di sidebar untuk memilih opsi tindakan

    # Memuat dan menampilkan data
    df = load_data()  # Memuat data dari sumber eksternal menggunakan fungsi load_data
    if df.empty:
        st.warning("No data available to visualize")  # Memberikan peringatan jika data kosong
        return

    # Daftar range usia yang digunakan
    age_ranges = [
        'Range Usia 18-24', 
        'Range Usia 25-34', 
        'Range Usia 35-44', 
        'Range Usia 45-54', 
        'Range Usia 55-64', 
        'Range Usia 65+'
    ]

    # Opsi "Lihat Data"
    if option == "Lihat Data":
        st.subheader("Data Table")  # Menampilkan judul sub-bagian
        st.write(df)  # Menampilkan data dalam bentuk tabel

    # Opsi "Perbarui Data"
    elif option == "Perbarui Data":
        st.subheader("Perbarui Data")  # Menampilkan sub-bagian untuk memperbarui data

        # Memilih data untuk diperbarui
        update_index = st.selectbox("Pilih Indeks untuk Diperbarui", df.index)  # Menampilkan dropdown untuk memilih baris yang akan diperbarui

        # Menampilkan data yang dipilih
        selected_row = df.loc[update_index]  # Mengambil baris data berdasarkan indeks yang dipilih
        updated_data = {}  # Dictionary untuk menyimpan data yang diperbarui

        for col in df.columns:
            updated_data[col] = st.text_input(f"Perbarui {col}", value=str(selected_row[col]))  # Input baru untuk setiap kolom

        if st.button("Simpan Perubahan"):
            df.loc[update_index] = updated_data  # Memperbarui data di DataFrame
            df.to_csv('user_input_data.csv', index=False)  # Menyimpan perubahan ke file CSV
            st.success("Data berhasil diperbarui!")  # Menampilkan pesan sukses

    # Opsi "Hapus Data"
    elif option == "Hapus Data":
        st.subheader("Hapus Data")  # Menampilkan sub-bagian untuk menghapus data

        # Memilih data untuk dihapus
        delete_index = st.selectbox("Pilih Indeks untuk Dihapus", df.index)  # Menampilkan dropdown untuk memilih data yang akan dihapus

        if st.button("Hapus Data"):
            df = df.drop(delete_index)  # Menghapus baris yang dipilih
            df.to_csv('user_input_data.csv', index=False)  # Menyimpan perubahan ke file CSV
            st.success("Data berhasil dihapus!")  # Menampilkan pesan sukses

    # Opsi "Visualisasi"
    elif option == "Visualisasi":
        st.subheader("Data Visualization")  # Menampilkan sub-bagian untuk visualisasi data

        # 1. Reach Over Time (Visualisasi reach berdasarkan waktu)
        st.write("### Reach Over Time")
        df['Tanggal'] = pd.to_datetime(df['Tanggal'], errors='coerce')  # Mengonversi kolom Tanggal menjadi tipe datetime
        df = df.dropna(subset=['Tanggal'])  # Menghapus baris dengan Tanggal yang tidak valid
        reach_over_time = df.groupby('Tanggal')['Reach'].sum().reset_index()  # Mengelompokkan reach berdasarkan tanggal
        fig, ax = plt.subplots(figsize=(8, 5))  # Membuat figur untuk plot
        ax.plot(reach_over_time['Tanggal'], reach_over_time['Reach'], label='Actual Reach')  # Membuat plot garis
        ax.set_title("Reach Over Time")  # Menambahkan judul grafik
        ax.set_xlabel("Tanggal")  # Menambahkan label sumbu-x
        ax.set_ylabel("Reach")  # Menambahkan label sumbu-y
        plt.xticks(rotation=45)  # Memutar label sumbu-x untuk keterbacaan
        st.pyplot(fig)  # Menampilkan plot di Streamlit

        # 2. Reach by Gender (Visualisasi reach berdasarkan gender)
        st.write("### Reach by Gender")
        gender_data = df[['Gender (L)', 'Gender (P)']].sum()  # Menghitung total reach per gender
        fig, ax = plt.subplots(figsize=(8, 5))  # Membuat figur untuk pie chart
        ax.pie(gender_data, labels=['Male (L)', 'Female (P)'], autopct='%1.1f%%', startangle=90, colors=['darkblue', 'orange'])  # Membuat pie chart
        ax.axis('equal')  # Memastikan pie chart berbentuk bulat
        st.pyplot(fig)  # Menampilkan pie chart di Streamlit

        # 3. Reach by Age Range (Visualisasi reach berdasarkan range usia)
        st.write("### Reach by Age Range")
        if all(range_col in df.columns for range_col in age_ranges):  # Memastikan semua kolom rentang usia ada dalam data
            age_range_data = df[age_ranges].sum()  # Menghitung total reach per rentang usia
            fig, ax = plt.subplots(figsize=(8, 5))  # Membuat figur untuk bar chart
            age_range_data.plot(kind='bar', ax=ax, color='green')  # Membuat bar chart
            ax.set_title("Reach by Age Range")  # Menambahkan judul
            ax.set_xlabel("Age Range")  # Label sumbu-x
            ax.set_ylabel("Reach")  # Label sumbu-y
            ax.set_xticklabels(age_ranges, rotation=45, ha='right')  # Memutar label rentang usia
            st.pyplot(fig)  # Menampilkan bar chart di Streamlit
        else:
            st.warning("No age range data available.")  # Peringatan jika data rentang usia tidak tersedia

    # Opsi "Prediksi"
    elif option == "Prediksi":
        if st.button("Prediksi Reach"):  # Tombol untuk menjalankan prediksi
            # Asumsi bahwa 'Reach' adalah variabel target untuk prediksi
            if 'Reach' not in df.columns:
                st.warning("No 'Reach' column found for predictions.")  # Peringatan jika kolom 'Reach' tidak ditemukan
                return

            # Fitur dan target
            X = df.drop(columns=['Reach', 'Tanggal'])  # Menghapus kolom 'Reach' dan 'Tanggal' dari fitur
            y = df['Reach']  # Target adalah kolom 'Reach'

            # Standardisasi
            scaler = StandardScaler()  # Inisialisasi standard scaler
            X_scaled = scaler.fit_transform(X.select_dtypes(include=['float64', 'int64']))  # Menstandarkan fitur numerik

            # Melatih model Random Forest
            model = RandomForestRegressor(n_estimators=100, random_state=42)  # Inisialisasi model Random Forest
            model.fit(X_scaled, y)  # Melatih model menggunakan data yang sudah distandarisasi

            # Melakukan prediksi pada data yang sama
            predictions = model.predict(X_scaled)  # Prediksi reach

            # Menghitung metrik akurasi
            mse = mean_squared_error(y, predictions)  # Menghitung Mean Squared Error
            r2 = r2_score(y, predictions)  # Menghitung R^2 score

            # Menampilkan prediksi
            df['Predicted Reach'] = predictions  # Menambahkan kolom prediksi ke DataFrame
            st.subheader("Predictions")  # Sub-bagian untuk menampilkan prediksi
            st.dataframe(df[['Reach', 'Predicted Reach']])  # Menampilkan tabel dengan actual dan predicted reach

            # Visualisasi actual vs predicted reach over time
            st.write("### Actual vs Predicted Reach Over Time")
            actual_vs_predicted = df.groupby('Tanggal').agg({'Reach': 'sum', 'Predicted Reach': 'sum'}).reset_index()  # Mengelompokkan actual dan predicted reach berdasarkan tanggal
            fig, ax = plt.subplots(figsize=(8.5, 5))  # Membuat figur untuk visualisasi
            actual_vs_predicted.plot(x='Tanggal', y=['Reach', 'Predicted Reach'], ax=ax)  # Plot actual vs predicted
            ax.set_title("Actual vs Predicted Reach Over Time")  # Menambahkan judul
            ax.set_xlabel("Tanggal")  # Label sumbu-x
            ax.set_ylabel("Reach")  # Label sumbu-y
            ax.legend(['Actual Reach', 'Predicted Reach'])  # Menambahkan legenda
            st.pyplot(fig)  # Menampilkan plot di Streamlit

            # Visualisasi prediksi berdasarkan gender
            st.write("### Predicted Reach by Gender")
            predicted_gender_data = pd.Series({
                'Male (L)': df['Gender (L)'].sum() * df['Predicted Reach'].sum() / df['Reach'].sum(),
                'Female (P)': df['Gender (P)'].sum() * df['Predicted Reach'].sum() / df['Reach'].sum()
            })  # Menghitung prediksi reach berdasarkan gender

            fig, ax = plt.subplots(figsize=(4, 2))  # Membuat figur yang lebih kecil
            ax.pie(predicted_gender_data, labels=predicted_gender_data.index, autopct='%1.1f%%', startangle=90, colors=['darkblue', 'orange'], textprops={'fontsize': 6})  # Membuat pie chart
            ax.axis('equal')  # Memastikan pie chart berbentuk bulat
            ax.set_title("Predicted Reach by Gender", fontsize=8)  # Mengatur ukuran font judul
            st.pyplot(fig)  # Menampilkan pie chart

            # Visualisasi prediksi berdasarkan rentang usia
            st.write("### Predicted Reach by Age Range")
            predicted_age_range_data = {
                age_range: (df[age_range].sum() * df['Predicted Reach'].sum() / df['Reach'].sum()) for age_range in age_ranges
            }  # Menghitung prediksi reach berdasarkan rentang usia

            fig, ax = plt.subplots(figsize=(8.5, 5))  # Membuat figur untuk bar chart
            pd.Series(predicted_age_range_data).plot(kind='bar', ax=ax, color='green')  # Membuat bar chart
            ax.set_title("Predicted Reach by Age Range")  # Menambahkan judul
            ax.set_xlabel("Age Range")  # Label sumbu-x
            ax.set_ylabel("Predicted Reach")  # Label sumbu-y
            ax.set_xticklabels(age_ranges, rotation=45, ha='right')  # Memutar label rentang usia
            st.pyplot(fig)  # Menampilkan bar chart

            # Visualisasi prediksi reach over time
            st.write("### Predicted Reach Over Time")
            predicted_over_time = df.groupby('Tanggal')['Predicted Reach'].sum()  # Mengelompokkan prediksi reach berdasarkan waktu
            fig, ax = plt.subplots(figsize=(8.5, 5))  # Membuat figur untuk line chart
            predicted_over_time.plot(kind='line', ax=ax, color='orange')  # Membuat plot garis
            ax.set_title("Predicted Reach Over Time")  # Menambahkan judul
            ax.set_xlabel("Tanggal")  # Label sumbu-x
            ax.set_ylabel("Predicted Reach")  # Label sumbu-y
            st.pyplot(fig)  # Menampilkan plot

            # Menampilkan metrik akurasi model
            st.subheader("Model Accuracy")  # Sub-bagian untuk akurasi model
            st.write(f"Mean Squared Error: {mse:.2f}")  # Menampilkan nilai MSE
            st.write(f"R^2 Score: {r2:.2f}")  # Menampilkan nilai R^2

# Pastikan fungsi ini dipanggil di main app
if __name__ == "__main__":
    admin_page()  # Memanggil fungsi admin_page sebagai halaman utama
