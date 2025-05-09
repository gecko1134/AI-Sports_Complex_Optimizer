
import streamlit as st
import pandas as pd

def run():
    st.title("🎁 Referee & Volunteer Credit System")

    log = pd.DataFrame({
        "Name": ["Jordan Smith", "Taylor Lee"],
        "Credits Earned": [50, 30]
    })

    st.dataframe(log)
    st.markdown("Volunteers and refs earn credits per event.")
