import streamlit as st
import pandas as pd

def run():
    st.title("🙋 Volunteer Hub")

    st.markdown("### Track Volunteer Shifts and Hours")
    hours = pd.DataFrame({
        "Name": ["Chris", "Dana"],
        "Event": ["Health Expo", "Youth Tournament"],
        "Hours": [5, 4]
    })
    st.dataframe(hours)