
import streamlit as st
import pandas as pd

def run():
    st.title("📣 Contract Conversion Alerts")

    data = pd.DataFrame({
        "Team": ["UMN Bulldogs", "Proctor Panthers"],
        "Hours Used": [95, 48],
        "Hourly Rate": [120, 100],
        "Package Offer": ["100 hrs for $9500", "50 hrs for $4500"],
        "Package Cost": [9500, 4500]
    })

    data["Hourly Cost"] = data["Hours Used"] * data["Hourly Rate"]
    data["Savings"] = data["Hourly Cost"] - data["Package Cost"]
    data["Switch Recommended"] = data["Savings"] > 0

    st.dataframe(data)
    for i, row in data.iterrows():
        if row["Switch Recommended"]:
            st.warning(f"{row['Team']} should switch to package: saves ${row['Savings']:,.0f}")
