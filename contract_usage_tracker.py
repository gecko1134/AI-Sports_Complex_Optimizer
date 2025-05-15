import streamlit as st
import pandas as pd

def run():
    st.title("📑 Contract Usage Tracker")
    contracts = pd.DataFrame({
        "Org": ["UMD Soccer", "City League"],
        "Hours Purchased": [100, 50],
        "Used": [82, 38]
    })
    contracts["Remaining"] = contracts["Hours Purchased"] - contracts["Used"]
    st.dataframe(contracts)