
import streamlit as st

def run():
    st.title("🗓️ Staff Scheduler")

    name = st.text_input("Staff Name")
    shift = st.selectbox("Shift", ["Morning", "Afternoon", "Evening"])
    if st.button("Assign"):
        st.success(f"{name} assigned to {shift} shift.")

    st.markdown("This is a working demo of scheduling.")
