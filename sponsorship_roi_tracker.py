import streamlit as st
import pandas as pd

def run():
    st.title("📊 Sponsorship ROI Tracker")
    df = pd.DataFrame({
        "Sponsor": ["Nike", "BankCo"],
        "Clicks": [5000, 1200],
        "Event Mentions": [12, 5],
        "Estimated ROI": ["320%", "140%"]
    })
    st.dataframe(df)