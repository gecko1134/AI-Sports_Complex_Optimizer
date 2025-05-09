
import streamlit as st

def run():
    st.title("📈 AI Forecast & Revenue Suggestions")

    rentals = st.number_input("Weekly Rental Hours", value=30)
    tournaments = st.number_input("Tournaments per Month", value=2)
    memberships = st.number_input("Active Memberships", value=150)

    total_revenue = rentals * 125 * 52 + tournaments * 10000 * 12 + memberships * 500
    st.markdown(f"### Projected Revenue: ${total_revenue:,.0f}")

    if rentals > 40:
        st.info("Consider shifting some rentals to higher-value tournaments.")
    if memberships < 200:
        st.warning("Boost membership campaigns to hit revenue goals.")
