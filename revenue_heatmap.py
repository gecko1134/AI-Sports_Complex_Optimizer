import streamlit as st
import pandas as pd

def run():
    st.title("💵 Revenue Heatmap")

    st.markdown("### Weekly Revenue by Surface & Hour")

    data = {
        "Hour": ["8-9 AM", "9-10 AM", "10-11 AM", "11-12 PM", "12-1 PM", "1-2 PM"],
        "Turf A ($)": [400, 450, 200, 300, 250, 150],
        "Court 1 ($)": [100, 120, 80, 50, 90, 70],
        "Court 2 ($)": [60, 75, 30, 20, 25, 40]
    }

    df = pd.DataFrame(data)
    st.dataframe(df)

    st.markdown("### AI Observations")

    st.warning("Court 2 has low revenue from 10 AM – 1 PM. Consider promotions.")
    st.success("Turf A peak value is 9–10 AM. Lock that for premium bookings.")
    st.info("Court 1 has stable mid-morning revenue. Consider leagues 9–11 AM.")