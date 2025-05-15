import streamlit as st
import pandas as pd

def run():
    st.title("🏟️ Dome Usage Tracker")

    usage = pd.DataFrame({
        "Date": ["2024-05-01", "2024-05-02"],
        "Type": ["Sports", "Non-Sport"],
        "Event": ["Youth Soccer", "Health Expo"],
        "Group": ["Proctor FC", "Wellness Coalition"],
        "Hours": [2, 5],
        "Area": ["Turf A", "Full Dome"]
    })

    st.dataframe(usage)
    st.download_button("Download Usage Log", usage.to_csv(index=False), "dome_usage.csv")