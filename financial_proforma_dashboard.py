
import streamlit as st
import pandas as pd

def run():
    st.title("📊 Financial Pro Forma Dashboard")

    st.subheader("Enter Revenue")
    rentals = st.number_input("Rental Revenue", min_value=0)
    sponsors = st.number_input("Sponsorship Revenue", min_value=0)

    st.subheader("Enter Expenses")
    ops = st.number_input("Operational Costs", min_value=0)
    staff = st.number_input("Staff Costs", min_value=0)

    net = (rentals + sponsors) - (ops + staff)
    st.markdown(f"### Net Income: ${net:,.0f}")
