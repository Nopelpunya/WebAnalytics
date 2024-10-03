import pandas as pd
import streamlit as st

# Load the saved data from CSV
def load_data():
    try:
        df = pd.read_csv('user_input_data.csv')
        if df.empty:  # Check if the DataFrame is empty
            return pd.DataFrame(columns=['Tanggal', 'Reach', 'Gender (L)', 'Gender (P)', 'Range Usia 18-24', 'Range Usia 25-34', 'Range Usia 35-44', 'Range Usia 45-54', 'Range Usia 55-64', 'Range Usia 65+'])
        return df
    except FileNotFoundError:
        return pd.DataFrame(columns=['Tanggal', 'Reach', 'Gender (L)', 'Gender (P)', 'Range Usia 18-24', 'Range Usia 25-34', 'Range Usia 35-44', 'Range Usia 45-54', 'Range Usia 55-64', 'Range Usia 65+'])

# Save new input data to CSV
def save_data(data):
    # Validate input data
    required_columns = ['Tanggal', 'Reach', 'Gender (L)', 'Gender (P)', 'Range Usia 18-24', 'Range Usia 25-34', 'Range Usia 35-44', 'Range Usia 45-54', 'Range Usia 55-64', 'Range Usia 65+']
    
    for col in required_columns:
        if col not in data:
            raise ValueError(f"Missing required data: {col}")

    df = load_data()
    
    new_data = pd.DataFrame([data])

    # Concatenate and save to CSV
    try:
        df = pd.concat([df, new_data], ignore_index=True)
        df.to_csv('user_input_data.csv', index=False)
    except Exception as e:
        print(f"Error saving data: {e}")