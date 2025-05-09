
import streamlit as st

def run():
    st.title("🎯 AI Sponsor Match Score")
    goals = st.multiselect("Select Goals", ["Brand Awareness", "Youth Impact", "Digital Reach"])
    budget = st.number_input("Sponsor Budget ($)", min_value=0)
    if st.button("Calculate Match"):
        score = 70 + len(goals) * 10
        st.success(f"Match Score: {min(score, 100)}")
