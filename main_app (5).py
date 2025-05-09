
import streamlit as st
from pathlib import Path
import importlib.util

import user_auth
user_auth.authenticate()

st.set_page_config(page_title="Venture North Admin", layout="wide")
st.sidebar.title("🏟️ Venture North Admin")

modules = [
    "financial_proforma_dashboard", "team_tournament_tracker", "staff_scheduler",
    "ref_volunteer_tracker", "ref_volunteer_credit_system", "staff_checkin_portal",
    "event_checkin_shift_report", "staff_badge_generator", "qr_badge_validator",
    "ai_forecast_suggestion", "ai_roi_estimator", "contract_conversion_alerts",
    "sponsor_fulfillment_dashboard", "contract_auto_generator", "sponsor_portal_login",
    "ai_bundle_builder", "ai_pricing_engine", "grant_tracker", "sponsor_fulfillment_pdf_generator",
    "voucher_email_sender", "redemption_tracker", "redemption_reporting",
    "team_loyalty_credit_system", "calendar_booking_credit_check",
    "google_sheets_sync", "ai_sponsor_match_score", "ai_scheduling_optimizer",
    "enhanced_grant_tracker", "usage_tracker", "credit_usage_tracker",
    "batch_badge_generator", "board_of_directors_dashboard"
]

tab = st.sidebar.selectbox("Choose Module", ["Welcome"] + [x.replace('_', ' ').title() for x in modules])

if tab == "Welcome":
    st.title("🎯 Venture North Admin Dashboard")
    st.success(f"Logged in as {st.session_state.get('user_role', 'Unknown')}")
    st.markdown("Use the sidebar to access any module.")
else:
    mod_name = tab.replace(" ", "_").lower()
    path = Path(__file__).parent / f"{mod_name}.py"
    spec = importlib.util.spec_from_file_location(mod_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.run()
