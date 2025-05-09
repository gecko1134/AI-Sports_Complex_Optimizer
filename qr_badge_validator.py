
import streamlit as st

def run():
    st.title("🔍 QR Badge Code Validator")

    badge_code = st.text_input("Enter Badge Code")
    if badge_code == "ABC123":
        st.success("Valid Badge: Jordan Smith, Referee")
    elif badge_code:
        st.error("Invalid badge code.")
