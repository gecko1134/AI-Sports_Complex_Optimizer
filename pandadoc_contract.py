import streamlit as st

def run():
    st.title("📄 PandaDoc Contract Generator")

    name = st.text_input("Sponsor Name")
    tier = st.selectbox("Tier", ["Silver", "Gold", "Platinum"])
    amount = st.number_input("Sponsorship Value ($)", step=500)
    duration = st.number_input("Duration (Months)", step=1)
    email = st.text_input("Contact Email")

    if st.button("Generate Contract"):
        st.success(f"Draft contract prepared for {name} at {tier} tier.")
        st.info("📝 This would be sent via PandaDoc API in production.")