
import streamlit as st
import pandas as pd

def run():
    st.title("🏟️ Team & Tournament Tracker")

    data = pd.DataFrame({
        "Team": ["UMN", "Proctor Panthers"],
        "Event": ["Soccer", "Basketball"],
        "Hours Used": [12, 8]
    })

    st.dataframe(data)
