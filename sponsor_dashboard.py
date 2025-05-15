import streamlit as st
import pandas as pd

def run():
    st.title("📊 Sponsor Dashboard")

    sponsors = pd.DataFrame({
        "Name": ["Nike", "Health Co.", "Local Bank"],
        "Tier": ["Platinum", "Gold", "Silver"],
        "Value ($)": [50000, 30000, 10000],
        "Contract End": ["2024-12-31", "2024-08-01", "2025-02-15"]
    })

    st.dataframe(sponsors)
    st.download_button("Download Sponsor List", sponsors.to_csv(index=False), "sponsors.csv")