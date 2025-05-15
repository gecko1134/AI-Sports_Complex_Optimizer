import streamlit as st

def run():
    st.title("📝 Membership Intake Form")

    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    tier = st.selectbox("Select Tier", ["Basic", "Team", "Elite", "Club"])
    notes = st.text_area("Additional Info")

    if st.button("Submit Application"):
        st.success(f"Membership submitted for {name} at {tier} level.")