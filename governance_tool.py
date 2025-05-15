import streamlit as st
import pandas as pd

def run():
    st.title("🗳️ Governance Board")

    st.markdown("### Track Board Members & Meeting Votes")
    members = pd.DataFrame({
        "Name": ["Alice", "Bob", "Carmen"],
        "Role": ["Chair", "Treasurer", "Member"],
        "Status": ["Active", "Active", "Inactive"]
    })
    st.dataframe(members)

    vote_topic = st.text_input("Propose Vote Topic")
    if st.button("Submit Vote"):
        st.success(f"Vote '{vote_topic}' submitted for board review.")