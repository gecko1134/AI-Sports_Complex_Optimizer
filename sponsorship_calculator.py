import streamlit as st

def run():
    st.title("💡 Sponsorship AI Calculator")

    st.markdown("### Enter Sponsorship Criteria")
    visibility = st.slider("Visibility (1 = low signage, 10 = nationally featured)", 1, 10, 5)
    exclusivity = st.slider("Exclusivity Level (1 = shared, 10 = category exclusive)", 1, 10, 5)
    duration = st.slider("Duration (in months)", 1, 60, 12)
    base_rate = 1000  # base multiplier

    estimated_value = base_rate * visibility * (1 + exclusivity / 10) * (duration / 12)

    st.metric("Estimated Annual Value", f"${estimated_value:,.2f}")
    st.markdown("Use this estimate to suggest tier and pricing to sponsors.")