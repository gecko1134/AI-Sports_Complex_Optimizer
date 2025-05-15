import streamlit as st
import pandas as pd

def run():
    st.title("📊 Sponsor Dashboard")
    df = pd.DataFrame({
        "Sponsor": ["Nike", "BankCo", "Health Group"],
        "Tier": ["Platinum", "Gold", "Silver"],
        "Value": [50000, 20000, 10000]
    })
    st.dataframe(df)