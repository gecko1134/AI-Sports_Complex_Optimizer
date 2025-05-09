
import streamlit as st
import pandas as pd

def run():
    st.title("📊 Usage Tracker")
    df = pd.DataFrame({
        "Date": ["2024-06-01", "2024-06-02"],
        "Resource": ["Court A", "Dome"],
        "User": ["UMN", "Proctor"],
        "Hours": [2, 4]
    })
    st.dataframe(df)
