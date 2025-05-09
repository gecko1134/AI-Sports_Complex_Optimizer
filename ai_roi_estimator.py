
import streamlit as st

def run():
    st.title("📊 Sponsor ROI Estimator")

    impressions = st.number_input("Estimated Impressions", value=50000)
    spend = st.number_input("Sponsorship Spend ($)", value=5000)
    engagement = st.slider("Engagement Rate (%)", 0.0, 10.0, 3.5)

    estimated_value = (impressions / 1000) * 15 + (engagement / 100 * impressions * 2.5)
    roi = estimated_value / spend if spend > 0 else 0

    st.markdown(f"Estimated Value: ${estimated_value:,.2f}")
    st.markdown(f"ROI Ratio: {roi:.2f}x")
