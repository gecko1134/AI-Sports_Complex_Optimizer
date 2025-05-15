import streamlit as st
import pandas as pd

def run():
    st.title("🧠 AI Scheduling Suggestions")

    st.markdown("### Usage Snapshot by Hour and Surface")
    data = pd.DataFrame({
        "Time Slot": ["8-9 AM", "9-10 AM", "10-11 AM", "11-12 PM", "12-1 PM"],
        "Turf A": [1, 1, 0, 1, 0],
        "Court 1": [1, 0, 0, 1, 1],
        "Court 2": [1, 1, 0, 0, 0]
    })

    st.dataframe(data.replace({1: "Booked", 0: "Open"}))

    st.markdown("### AI Suggestions")
    st.success("📢 Recommend promoting Court 2 for corporate team building from 10 AM–1 PM.")
    st.info("📅 Move youth training to Court 1 10 AM–11 AM to open Court 2 for a 3-hour tournament block.")
    st.warning("🕓 Turf A is only 60% booked during off-peak hours — offer rental discount bundle.")
    st.markdown("💡 Suggest launching a 'Friday Open Field' campaign to drive weekend usage.")