import streamlit as st
import pandas as pd

def run():
    st.title("👥 Membership Dashboard")
    data = pd.DataFrame({
        "Name": ["Jordan", "Casey"],
        "Tier": ["Elite", "Standard"],
        "Credits Remaining": [12, 3],
        "Last Login": ["2024-05-01", "2024-04-28"]
    })
    st.dataframe(data)