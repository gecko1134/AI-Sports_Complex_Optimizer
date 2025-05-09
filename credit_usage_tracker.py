
import streamlit as st
import pandas as pd

def run():
    st.title("💳 Credit Usage Tracker")
    df = pd.DataFrame({
        "User": ["UMN", "Sponsor X"],
        "Credits Assigned": [100, 200],
        "Used": [40, 150],
        "Remaining": [60, 50]
    })
    st.dataframe(df)
