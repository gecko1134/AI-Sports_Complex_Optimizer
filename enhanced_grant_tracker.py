
import streamlit as st
import pandas as pd

def run():
    st.title("📑 Enhanced Grant Tracker")
    df = pd.DataFrame({
        "Grant": ["Youth Development", "Infrastructure"],
        "Status": ["Submitted", "Draft"],
        "Amount": [100000, 500000]
    })
    st.dataframe(df)
