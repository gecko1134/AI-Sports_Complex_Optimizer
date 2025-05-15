import streamlit as st
import pandas as pd

def run():
    st.title("💸 Dynamic Pricing Tool")

    st.markdown("### Current Pricing Matrix")
    pricing = pd.DataFrame({
        "Surface": ["Turf A", "Turf B", "Court 1", "Court 2"],
        "Prime Time Rate ($/hr)": [225, 200, 75, 75],
        "Non-Prime Rate ($/hr)": [150, 125, 50, 50],
        "Avg Usage (hrs/wk)": [42, 38, 30, 28]
    })

    st.dataframe(pricing)

    st.markdown("### AI Pricing Suggestions")
    st.success("Turf A has consistent 90%+ usage. Raise prime time rate to $250/hr.")
    st.warning("Court 2 under 70% usage. Recommend 20% discount for weekday slots.")
    st.info("Bundle Court 1 + Court 2 for corporate rentals on Fridays.")

    st.markdown("💬 'Offer 25% off Tuesday Turf Rentals from 2–4 PM' is performing well at peer facilities.")