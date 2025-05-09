
import streamlit as st
import pandas as pd

def run():
    st.title("📑 Grant Tracker")
    df = pd.DataFrame({
        "Grant": ["Youth Access", "Infrastructure Boost"],
        "Status": ["Submitted", "Draft"],
        "Deadline": ["2024-09-15", "2024-12-01"]
    })
    st.dataframe(df)
