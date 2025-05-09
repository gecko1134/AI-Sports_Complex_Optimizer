
import streamlit as st

def run():
    st.title("💸 AI Pricing Engine")
    asset = st.selectbox("Select Asset", ["Court", "Turf", "Event Sponsorship"])
    base = st.number_input("Base Rate", min_value=0)
    duration = st.slider("Months", 1, 12)
    price = base * duration * 1.2
    st.markdown(f"Suggested Price: ${price:,.2f}")
