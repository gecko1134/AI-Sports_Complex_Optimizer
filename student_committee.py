import streamlit as st
import pandas as pd

def run():
    st.title("🎓 Student Committee Dashboard")

    st.markdown("### Log Student Rep Contributions")
    tasks = pd.DataFrame({
        "Name": ["Ava", "Jayden"],
        "School": ["North High", "Central Tech"],
        "Contribution": ["Led community event", "Gave proposal to board"]
    })
    st.dataframe(tasks)