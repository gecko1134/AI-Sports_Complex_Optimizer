import streamlit as st
import pandas as pd

def run():
    st.title("📅 Visual Calendar Layout")

    st.markdown("### Daily Surface Usage Overview")

    schedule = pd.DataFrame({
        "Time Slot": ["8-9 AM", "9-10 AM", "10-11 AM", "11-12 PM", "12-1 PM", "1-2 PM"],
        "Turf A": ["Soccer", "Soccer", "Open", "Lacrosse", "Open", "Youth Training"],
        "Court 1": ["Basketball", "Open", "Basketball", "Open", "Volleyball", "Volleyball"],
        "Court 2": ["Pickleball", "Pickleball", "Open", "Open", "Pickleball", "Open"]
    })

    st.dataframe(schedule)

    st.markdown("🧠 **AI Insight:** Court 2 has 50% idle hours — suggest running 2-for-1 court rentals from 10 AM – 1 PM.")