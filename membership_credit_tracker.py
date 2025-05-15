import streamlit as st
import pandas as pd

def run():
    st.title("💳 Credit Tracker")
    df = pd.DataFrame({
        "Member": ["Jordan", "Casey"],
        "Credits Bought": [30, 10],
        "Used": [18, 7]
    })
    df["Remaining"] = df["Credits Bought"] - df["Used"]
    st.dataframe(df)