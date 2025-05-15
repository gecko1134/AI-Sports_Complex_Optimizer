import streamlit as st
import pandas as pd
from datetime import date

def run():
    st.title("📑 Contract Usage Tracker")

    st.markdown("### Organizations With Usage Contracts")

    contracts = pd.DataFrame({
        "Organization": ["UMD Soccer", "North High School", "ACME Corp", "City Rec League"],
        "Type": ["University", "High School", "Corporate", "Recreation League"],
        "Hours Purchased": [120, 80, 150, 100],
        "Hours Used": [100, 64, 50, 92],
        "Contract Start": ["2024-01-01", "2023-09-01", "2024-02-01", "2024-03-15"],
        "Contract End": ["2025-01-01", "2024-06-01", "2025-02-01", "2024-09-15"],
        "Hourly Rate": [150, 100, 200, 75]
    })

    contracts["Hours Remaining"] = contracts["Hours Purchased"] - contracts["Hours Used"]
    contracts["ROI"] = (contracts["Hours Used"] * contracts["Hourly Rate"]) / (contracts["Hours Purchased"] * contracts["Hourly Rate"]) * 100
    contracts["ROI"] = contracts["ROI"].round(1).astype(str) + "%"

    st.dataframe(contracts)

    st.download_button("Download Contract Data", contracts.to_csv(index=False), "usage_contracts.csv")