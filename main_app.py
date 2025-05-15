import streamlit as st

import sponsorship_ai_calculator as sponsor_calc
import sponsor_dashboard as sponsor_dash
import pandadoc_contract as sponsor_contract
import proposal_to_pdf as sponsor_pdf
import sponsorship_roi_tracker as sponsor_roi

st.set_page_config(page_title="Venture North Admin", layout="wide")
st.sidebar.title("🏟️ Venture North Admin")

sections = {
    "Sponsorship": {
        "AI Sponsorship Calculator": sponsor_calc,
        "Sponsor Dashboard": sponsor_dash,
        "Contract Generator (PandaDoc)": sponsor_contract,
        "Proposal to PDF Generator": sponsor_pdf,
        "Sponsorship ROI Tracker": sponsor_roi
    }
}

selected_section = st.sidebar.selectbox("Select Section", list(sections.keys()))
selected_tool = st.sidebar.selectbox("Select Tool", list(sections[selected_section].keys()))

sections[selected_section][selected_tool].run()