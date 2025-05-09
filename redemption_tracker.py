
import streamlit as st
import pandas as pd

def run():
    st.title("🎟️ Redemption Tracker")
    df = pd.DataFrame({
        "Team": ["UMN", "Panthers"],
        "Reward": ["Court Hour", "Concession Credit"],
        "Points Used": [100, 75]
    })
    st.dataframe(df)
