
import streamlit as st

def run():
    st.title("🎯 AI Bundle Builder")
    goals = st.multiselect("Sponsorship Goals", ["Branding", "Youth Impact", "Digital Reach"])
    if st.button("Generate Bundle"):
        st.info("AI recommends: Banner + Livestream Package")
