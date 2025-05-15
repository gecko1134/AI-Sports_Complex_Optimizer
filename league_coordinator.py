import streamlit as st
import pandas as pd

def run():
    st.title("📅 League Coordinator")

    st.markdown("### Manage Schedules and Field Credits")
    schedule = pd.DataFrame({
        "League": ["HS Soccer", "Youth BBall"],
        "Field": ["Dome A", "Court 2"],
        "Time": ["3pm", "6pm"]
    })
    st.dataframe(schedule)