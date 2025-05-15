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
import nil_tracker as nil
import scholarship_tracker as scholarships
import mentorship_center as mentorship
import student_committee as student
import volunteer_hub as volunteers
import referee_manager as refs
import team_club_manager as teams
import league_coordinator as leagues
import tournament_manager as tournaments
import sponsor_dashboard as sponsors
import pandadoc_contract as contracts

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
    "AI Scheduler": ai_sched,
    "NIL Tracker": nil,
    "Scholarships": scholarships,
    "Mentorships": mentorship,
    "Student Committee": student,
    "Volunteers": volunteers,
    "Referees": refs,
    "Teams & Clubs": teams,
    "Leagues": leagues,
    "Tournaments": tournaments,
    "Sponsors": sponsors,
    "Contracts (PandaDoc)": contracts
}

selection = st.sidebar.selectbox("Choose a Tool", list(tools.keys()))
tools[selection].run()