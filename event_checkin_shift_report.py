
import streamlit as st
import pandas as pd

def run():
    st.title("📋 Event Shift Logs")

    st.markdown("This is a simulated report.")
    log = pd.DataFrame({
        "Name": ["Jordan Smith", "Taylor Lee"],
        "Event": ["Soccer Tourney", "Family Day"],
        "Time": ["8am", "12pm"]
    })
    st.dataframe(log)
