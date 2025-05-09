
import streamlit as st
from datetime import datetime

def run():
    st.title("📲 Staff & Volunteer Check-In")

    name = st.text_input("Full Name")
    role = st.radio("Role", ["Referee", "Volunteer"])
    event = st.selectbox("Event", ["Soccer Tourney", "Family Day"])
    if st.button("Check In"):
        checkin_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        st.success(f"{name} checked in as {role} for {event} at {checkin_time}")
