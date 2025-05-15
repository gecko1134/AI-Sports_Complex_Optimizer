import streamlit as st
import pandas as pd

def run():
    st.title("📊 Venture North Central Dashboard")

    st.markdown("### 🔗 Contract Summary")
    contracts = pd.DataFrame({
        "Organization": ["UMD Soccer", "ACME Corp", "City League"],
        "Type": ["University", "Corporate", "Recreation"],
        "Hours Purchased": [120, 150, 100],
        "Hours Used": [100, 50, 92],
        "Remaining": [20, 100, 8],
        "Contract End": ["2025-01-01", "2025-02-01", "2024-09-15"]
    })
    st.dataframe(contracts)

    st.markdown("### 💰 Revenue Snapshot")
    revenue = pd.DataFrame({
        "Surface": ["Turf A", "Court 1", "Court 2"],
        "Hours Booked": [48, 40, 36],
        "Rate ($/hr)": [200, 50, 50],
        "Revenue": [9600, 2000, 1800]
    })
    st.dataframe(revenue)

    st.markdown("### 🕓 Usage by Surface")
    usage = pd.DataFrame({
        "Surface": ["Turf A", "Court 1", "Court 2"],
        "Prime Time Hours": [30, 24, 20],
        "Non-Prime Hours": [18, 16, 16],
        "Utilization %": [95, 85, 78]
    })
    st.dataframe(usage)

    st.markdown("### 📌 AI Suggestions")
    st.info("📢 Court 2 underutilized — consider 2-for-1 afternoon promos.")
    st.success("🎯 Turf A bookings exceeding 90% — suggest premium tier offer.")
    st.warning("🔔 City League contract ends soon — offer renewal bundle with bonus hours.")