import streamlit as st
import pandas as pd

def run():
    st.title("📆 Visual Layout")
    schedule = pd.DataFrame({
        "Time": ["8-9", "9-10", "10-11"],
        "Turf A": ["Soccer", "Open", "Cricket"],
        "Court 1": ["Basketball", "Open", "Pickleball"]
    })
    st.dataframe(schedule)