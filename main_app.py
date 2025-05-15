import streamlit as st

# Import all known working modules
import memberships_tool as memberships
import membership_credit_tracker as credit_tracker
import membership_insights_ai as member_ai
import facility_membership_monitor as member_benchmark

import dome_usage_tool as usage
import complex_usage_optimizer as optimizer
import visual_calendar_layout as layout
import revenue_heatmap as heatmap
import ai_scheduling_suggestions as schedule_ai
import dynamic_pricing_tool as pricing

import sponsor_dashboard as sponsors
import sponsorship_ai_calculator as sponsor_calc
import pandadoc_contract as pandadoc
import proposal_to_pdf as proposal
import sponsorship_roi_tracker as sponsor_roi

import contract_usage_tracker as contract_tracker
import contract_insights_ai as contract_ai
import facility_contract_monitor as contract_benchmark

import governance_tool as governance
import student_committee as student
import mentorship_center as mentorship
import scholarship_tracker as scholarships

import volunteer_hub as volunteer
import referee_manager as referee
import team_club_manager as teams
import league_coordinator as leagues

import nil_tracker as nil
import ai_matchmaker_tool as matchmaker
import ai_scheduler_tool as scheduler

import central_dashboard as dashboard

# Page settings
st.set_page_config(page_title="Venture North Admin", layout="wide")
st.sidebar.title("🏟️ Venture North Admin Tools")

# Dictionary of all tools flatly
tools = {
    "📊 Central Dashboard": dashboard,
    "👥 Memberships - Manager": memberships,
    "👥 Memberships - Credit Tracker": credit_tracker,
    "👥 Memberships - AI Insights": member_ai,
    "👥 Memberships - Benchmark Monitor": member_benchmark,

    "🏟️ Usage - Logger": usage,
    "🏟️ Usage - Optimizer": optimizer,
    "🏟️ Usage - Visual Layout": layout,
    "🏟️ Usage - Revenue Heatmap": heatmap,
    "🏟️ Usage - AI Scheduling": schedule_ai,
    "🏟️ Usage - Dynamic Pricing": pricing,

    "💼 Sponsors - Dashboard": sponsors,
    "💼 Sponsors - AI Calculator": sponsor_calc,
    "💼 Sponsors - Contract Generator": pandadoc,
    "💼 Sponsors - Proposal to PDF": proposal,
    "💼 Sponsors - ROI Tracker": sponsor_roi,

    "📑 Contracts - Tracker": contract_tracker,
    "📑 Contracts - AI Insights": contract_ai,
    "📑 Contracts - Benchmarking": contract_benchmark,

    "🏛️ Governance - Board": governance,
    "🏛️ Governance - Student Committee": student,
    "🏛️ Governance - Mentorship": mentorship,
    "🏛️ Governance - Scholarships": scholarships,

    "🤝 Personnel - Volunteers": volunteer,
    "🤝 Personnel - Referees": referee,
    "🤝 Personnel - Teams & Clubs": teams,
    "🤝 Personnel - League Coordinator": leagues,

    "📢 NIL - Tracker": nil,
    "📢 NIL - AI Matchmaker": matchmaker,
    "📢 NIL - AI Scheduler": scheduler,
}

# Sidebar selection
selected_tool = st.sidebar.selectbox("Choose a Tool to Load", list(tools.keys()))
tools[selected_tool].run()