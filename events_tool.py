import streamlit as st
import pandas as pd
from datetime import date

def run():
    st.title("📆 Event Scheduler")

    st.markdown("### Add Event to Calendar")
    name = st.text_input("Event Name")
    date_selected = st.date_input("Date", date.today())
    host = st.text_input("Host Group")

    if "events" not in st.session_state:
        st.session_state.events = []

    if st.button("Add Event") and name:
        st.session_state.events.append({"Name": name, "Date": str(date_selected), "Host": host})

    df = pd.DataFrame(st.session_state.events)
    if not df.empty:
        st.dataframe(df)
        st.download_button("Download Events", df.to_csv(index=False), "events.csv")