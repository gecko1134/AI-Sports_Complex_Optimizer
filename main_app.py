import streamlit as st

import memberships_tool as memberships
import dome_usage_tool as dome_usage
import governance_tool as governance
import personnel_tool as personnel
import finance_tool as finance
import ai_engine_tool as ai_engine
import events_tool as events
import ai_matchmaker_tool as ai_match
import ai_scheduler_tool as ai_sched

st.set_page_config(page_title="Venture North Admin", layout="wide")
st.sidebar.title("🏟️ Venture North Admin")

tools = {
    "Memberships": memberships,
    "Dome Usage": dome_usage,
    "Governance": governance,
    "Personnel": personnel,
    "Finance": finance,
    "AI Engine": ai_engine,
    "Events": events,
    "AI Matchmaker": ai_match,
    "AI Scheduler": ai_sched
}

selection = st.sidebar.selectbox("Choose a Tool", list(tools.keys()))
tools[selection].run()