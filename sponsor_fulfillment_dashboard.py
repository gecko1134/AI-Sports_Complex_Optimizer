
import streamlit as st
import pandas as pd

def run():
    st.title("✅ Sponsor Fulfillment Dashboard")
    data = pd.DataFrame({
        "Sponsor": ["GoldCo", "SportFuel"],
        "Asset": ["Court A Banner", "Entrance Sign"],
        "Status": ["Complete", "In Progress"]
    })
    st.dataframe(data)
