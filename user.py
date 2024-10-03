import streamlit as st
from data_handler import save_data

def user_page():
    st.title("Halaman Pengguna")
    st.write("Selamat datang di halaman pengguna!")

    # Tombol Logout
    if st.button("Logout"):
        if 'role' in st.session_state:
            del st.session_state['role']  # Hapus role dari session_state
        st.session_state['logged_out'] = True
    
    # Input form for user data
    with st.form("data_input_form"):
        # Date input
        date = st.date_input("Enter the date")
        
        # Reach input
        reach = st.number_input("Enter reach", min_value=0)
        
        # Gender L (Male) input
        gender_l = st.number_input("Gender L (Male)", min_value=0)
        
        # Gender P (Female) input
        gender_p = st.number_input("Gender P (Female)", min_value=0)
        
        # Age range inputs
        st.write("Enter reach for each age range")
        age_18_24 = st.number_input("18-24", min_value=0)
        age_25_34 = st.number_input("25-34", min_value=0)
        age_35_44 = st.number_input("35-44", min_value=0)
        age_45_54 = st.number_input("45-54", min_value=0)
        age_55_64 = st.number_input("55-64", min_value=0)
        age_65_plus = st.number_input("65+", min_value=0)

        # Submit button
        submitted = st.form_submit_button("Submit")

        if submitted:
            # Prepare data dictionary
            data = {
                'Tanggal': date,
                'Reach': reach,
                'Gender (L)': gender_l,
                'Gender (P)': gender_p,
                'Range Usia 18-24': age_18_24,
                'Range Usia 25-34': age_25_34,
                'Range Usia 35-44': age_35_44,
                'Range Usia 45-54': age_45_54,
                'Range Usia 55-64': age_55_64,
                'Range Usia 65+': age_65_plus
            }
            # Save the data
            save_data(data)
            st.success("Data saved successfully!")
