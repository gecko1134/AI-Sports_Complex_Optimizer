
import streamlit as st
import pandas as pd

def run():
    st.title("🏅 Team Loyalty Credit System")
    df = pd.DataFrame({
        "Team": ["UMN", "Proctor"],
        "Points": [450, 275],
        "Tier": ["Gold", "Silver"]
    })
    st.dataframe(df)
