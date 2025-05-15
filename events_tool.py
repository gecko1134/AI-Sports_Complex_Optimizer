import streamlit as st
import pandas as pd
from datetime import date

def run():
    st.title("📅 Event Manager")

    st.markdown("### Add New Event")
    event_type = st.selectbox("Event Type", ["Tournament", "Expo", "Community"])
    name = st.text_input("Event Name")
    date_selected = st.date_input("Event Date", value=date.today())
    host = st.text_input("Host Group")
    add = st.button("Add Event")

    if "event_log" not in st.session_state:
        st.session_state.event_log = []

    if add and name:
        st.session_state.event_log.append({
            "Type": event_type,
            "Name": name,
            "Date": str(date_selected),
            "Host": host
        })

    df = pd.DataFrame(st.session_state.event_log)
    if not df.empty:
        st.dataframe(df)
        st.download_button("Download Event List", df.to_csv(index=False), "events.csv")