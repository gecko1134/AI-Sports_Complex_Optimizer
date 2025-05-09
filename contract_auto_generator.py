
import streamlit as st

def run():
    st.title("📝 Contract Auto-Generator")
    sponsor = st.text_input("Sponsor Name")
    amount = st.number_input("Contract Value ($)", min_value=0)
    if st.button("Generate Contract"):
        st.success(f"Contract for {sponsor} valued at ${amount:,} generated.")
