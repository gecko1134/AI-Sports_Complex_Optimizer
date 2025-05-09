
import streamlit as st
import pandas as pd

def run():
    st.title("🏛️ Board of Directors Dashboard")
    data = pd.DataFrame({
        "Name": ["Alex Johnson", "Jamie Lee"],
        "Role": ["Chair", "Secretary"],
        "Voting Rights": ["Yes", "Yes"]
    })
    st.dataframe(data)
