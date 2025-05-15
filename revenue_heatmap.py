import streamlit as st
import pandas as pd

def run():
    st.title("💵 Revenue Heatmap")
    df = pd.DataFrame({
        "Hour": ["8-9", "9-10", "10-11"],
        "Turf A": [200, 250, 180],
        "Court 1": [100, 75, 60]
    })
    st.dataframe(df)
    st.warning("⚠️ Suggest bundling Court 1 for rec groups 10–11 AM.")