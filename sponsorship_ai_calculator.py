import streamlit as st

def run():
    st.title("💼 AI Sponsorship Calculator")
    amount = st.slider("Sponsorship Amount", 1000, 100000, 10000, step=500)
    tier = "Platinum" if amount > 50000 else "Gold" if amount > 25000 else "Silver"
    st.metric("Recommended Tier", tier)
    st.write("📈 Suggest targeting weekend events and field signage.")