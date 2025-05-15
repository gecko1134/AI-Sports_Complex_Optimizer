import streamlit as st
import pandas as pd

def run():
    st.title("🏈 Teams & Clubs")

    rosters = pd.DataFrame({
        "Team": ["U14 Soccer", "Varsity Volleyball"],
        "Coach": ["Coach Kyle", "Coach Nina"],
        "Roster Size": [18, 12]
    })
    st.dataframe(rosters)