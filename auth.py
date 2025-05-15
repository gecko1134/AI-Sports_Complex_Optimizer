import streamlit as st
import json
from pathlib import Path

def login():
    users_file = Path(__file__).parent / "users.json"
    with open(users_file) as f:
        users = json.load(f)

    st.subheader("🔐 Login Required")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = users.get(email)
        if user and user["password"] == password:
            st.session_state["user"] = email
            st.session_state["role"] = user["role"]
            st.success(f"Welcome, {email}!")
            st.experimental_rerun()
        else:
            st.error("Invalid credentials.")

def require_login():
    if "user" not in st.session_state:
        login()
        st.stop()