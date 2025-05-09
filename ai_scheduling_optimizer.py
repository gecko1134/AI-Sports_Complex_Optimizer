
import streamlit as st

def run():
    st.title("📅 AI Scheduling Optimizer")
    team_type = st.selectbox("Requestor", ["Rec", "College", "Pro"])
    preferred_time = st.selectbox("Time Block", ["Morning", "Afternoon", "Evening"])
    if st.button("Suggest Slot"):
        st.success(f"Suggested: {preferred_time} slot for {team_type} team.")
