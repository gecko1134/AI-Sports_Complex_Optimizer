import streamlit as st
import pandas as pd
from datetime import date

def run():
    st.title("🏟️ Dome Usage Tracker")

    st.markdown("### Log New Usage")
    usage_type = st.selectbox("Type", ["Sport", "Non-Sport"])
    event_name = st.text_input("Event Name")
    group = st.text_input("Group or Team")
    hours = st.number_input("Hours", step=0.5)
    area = st.text_input("Facility Area")
    log_btn = st.button("Log Usage")

    if "usage_log" not in st.session_state:
        st.session_state.usage_log = []

    if log_btn and event_name:
        st.session_state.usage_log.append({
            "Date": str(date.today()),
            "Type": usage_type,
            "Event": event_name,
            "Group": group,
            "Hours": hours,
            "Area": area
        })

    df = pd.DataFrame(st.session_state.usage_log)
    if not df.empty:
        st.dataframe(df)
        st.download_button("Download Usage Log", df.to_csv(index=False), "usage.csv")