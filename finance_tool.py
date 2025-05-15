import streamlit as st
import pandas as pd

def run():
    st.title("💰 Finance Dashboard")

    st.markdown("### Input Revenue and Expenses")
    revenue = st.number_input("Monthly Revenue ($)", 0)
    expenses = st.number_input("Monthly Expenses ($)", 0)

    net = revenue - expenses
    st.metric("Net Income", f"${net:,.2f}", delta=None)

    st.markdown("#### Sponsor Overview")
    sponsors = pd.DataFrame({
        "Name": ["Nike", "Local Bank", "Community Health"],
        "Tier": ["Platinum", "Gold", "Silver"],
        "Annual Value": [50000, 20000, 10000]
    })
    st.dataframe(sponsors)