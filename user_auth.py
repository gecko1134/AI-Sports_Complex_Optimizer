
import streamlit as st

USER_CREDENTIALS = {
    "admin@venture.com": ("admin123", "Master Admin")
}

MODULE_ACCESS = {
    "Master Admin": ["all"]
}

def authenticate():
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False
        st.session_state["user_role"] = None
        st.session_state["user_email"] = None

    if not st.session_state["authenticated"]:
        st.sidebar.title("🔐 Login")
        email = st.sidebar.text_input("Email")
        password = st.sidebar.text_input("Password", type="password")
        if st.sidebar.button("Login"):
            if email in USER_CREDENTIALS and USER_CREDENTIALS[email][0] == password:
                st.session_state["authenticated"] = True
                st.session_state["user_email"] = email
                st.session_state["user_role"] = USER_CREDENTIALS[email][1]
            else:
                st.sidebar.error("Invalid login.")
        st.stop()

def get_accessible_tabs():
    role = st.session_state.get("user_role")
    if role == "Master Admin":
        return "all"
    return MODULE_ACCESS.get(role, [])
