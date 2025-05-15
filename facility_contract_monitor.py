import streamlit as st
import pandas as pd

def run():
    st.title("🌐 Facility Contract Benchmarking (AI Monitored)")

    benchmarks = pd.DataFrame({
        "Facility": ["PowerDome", "NextGen Sports", "AllAccess Fieldhouse"],
        "Avg Price/Hour": [175, 200, 150],
        "Term Length": ["1 year", "2 years", "Seasonal"],
        "User Type": ["College", "Corporate", "Rec League"],
        "Free Hours Included": ["5", "0", "2"],
        "Renewal Discount": ["10%", "None", "5%"]
    })

    st.dataframe(benchmarks)

    st.markdown("### Suggestions for Venture North:")
    st.success("🟢 Consider adding 5 free off-peak hours for Rec Leagues on renewals.")
    st.warning("🔁 ACME Corp contract may be overpriced compared to peer average.")
    st.info("🏷️ Youth Clubs often offer ‘seasonal credits’ as incentives.")