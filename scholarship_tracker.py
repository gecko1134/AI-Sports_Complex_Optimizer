import streamlit as st
import pandas as pd

def run():
    st.title("🎓 Scholarship Tracker")

    candidates = pd.DataFrame({
        "Name": ["Talia", "Ethan"],
        "GPA": [3.8, 3.4],
        "Sport": ["Track", "Baseball"],
        "Eligible": [True, False]
    })
    st.dataframe(candidates)