import streamlit as st

def run():
    st.title("🤝 Mentorship Program")

    st.markdown("### Match and Manage Mentors")
    mentor = st.text_input("Mentor Name")
    mentee = st.text_input("Mentee Name")
    goal = st.text_area("Mentorship Goal")

    if st.button("Log Match"):
        st.success(f"Mentor {mentor} matched with {mentee}. Goal logged.")