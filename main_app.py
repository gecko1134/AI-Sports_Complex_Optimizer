import streamlit as st
import importlib

import memberships_tool as memberships
import dome_usage_tool as dome_usage
import governance_tool as governance
import personnel_tool as personnel
import finance_tool as finance
import ai_engine_tool as ai_engine
import events_tool as events

st.set_page_config(page_title="Venture North Admin", layout="wide")
st.sidebar.title("🏟️ Venture North Admin")

modules = {
    "Memberships": memberships,
    "Dome Usage": dome_usage,
    "Governance": governance,
    "Personnel": personnel,
    "Finance": finance,
    "AI Engine": ai_engine,
    "Events": events
}

selection = st.sidebar.selectbox("Choose a Tool", list(modules.keys()))
modules[selection].run()