import streamlit as st
import pandas as pd

def run():
    st.title("🌐 Facility Membership Benchmarking")

    facilities = pd.DataFrame({
        "Facility": ["The Hub", "DomeX", "AllSport Complex"],
        "Base Plan ($/mo)": [30, 45, 40],
        "Credits Included": [10, 20, 15],
        "Family Plan Available": ["Yes", "Yes", "No"],
        "Peak Access": ["Limited", "Full", "Partial"]
    })

    st.dataframe(facilities)

    st.markdown("### Suggestions:")
    st.success("🧠 Add weekend peak access to Premium plan to compete with DomeX.")
    st.warning("💡 Consider bundling 3-month rental + membership for adult leagues.")