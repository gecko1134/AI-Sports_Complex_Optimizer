import streamlit as st
import pandas as pd

def run():
    st.title("🏛️ Governance Board")
    members = pd.DataFrame({
        "Name": ["Alice", "Bob"],
        "Role": ["Chair", "Treasurer"]
    })
    st.dataframe(members)