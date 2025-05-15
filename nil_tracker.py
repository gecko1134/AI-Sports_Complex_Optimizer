import streamlit as st
import pandas as pd

def run():
    st.title("📢 NIL Tracker")

    players = pd.DataFrame({
        "Athlete": ["Emma R.", "Lucas T."],
        "Sport": ["Softball", "Football"],
        "Followers": [4500, 7200],
        "NIL Ready": [True, True]
    })
    st.dataframe(players)