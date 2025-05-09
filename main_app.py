
import streamlit as st
from pathlib import Path
import importlib.util

USER_CREDENTIALS = {
    "admin@venture.com": ("admin123", "Master Admin")
}

def authenticate():
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False
        st.session_state["user_role"] = None
    if not st.session_state["authenticated"]:
        st.sidebar.title("🔐 Login")
        email = st.sidebar.text_input("Email")
        password = st.sidebar.text_input("Password", type="password")
        if st.sidebar.button("Login"):
            if email in USER_CREDENTIALS and USER_CREDENTIALS[email][0] == password:
                st.session_state["authenticated"] = True
                st.session_state["user_role"] = USER_CREDENTIALS[email][1]
            else:
                st.sidebar.error("Invalid login.")
        st.stop()

authenticate()
st.set_page_config(page_title="Venture North Admin", layout="wide")
st.sidebar.title("🏟️ Venture North Admin")

modules = ["financial_proforma_dashboard", "team_tournament_tracker", "staff_scheduler"]
tab = st.sidebar.selectbox("Choose Module", ["Welcome"] + [x.replace('_', ' ').title() for x in modules])

if tab == "Welcome":
    st.title("🎯 Venture North Admin Dashboard")
    st.success(f"Logged in as {st.session_state['user_role']}")
    st.markdown("Use the sidebar to test working modules.")
else:
    mod_name = tab.replace(" ", "_").lower()
    spec = importlib.util.spec_from_file_location(mod_name, Path(__file__).parent / f"{mod_name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.run()
