
import streamlit as st
import pandas as pd

def run():
    st.title("🧾 Referee & Volunteer Tracker")

    st.subheader("Waiver + Credential Status")
    data = pd.DataFrame({
        "Name": ["Jordan Smith", "Taylor Lee"],
        "Role": ["Referee", "Volunteer"],
        "Waiver Signed": ["Yes", "No"],
        "Background Check": ["Approved", "Pending"]
    })
    st.dataframe(data)
