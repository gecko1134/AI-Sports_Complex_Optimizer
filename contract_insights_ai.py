import streamlit as st

def run():
    st.title("🧠 Contract AI Insights & Marketing Suggestions")

    st.markdown("### AI Observations")
    st.info("🏫 North High School is at 80% usage. Auto-trigger renewal reminder.")
    st.success("💼 ACME Corp has only used 1/3 of purchased hours. Suggest adding lunchtime rentals or gift hours to stimulate usage.")
    st.warning("📢 City Rec League runs out in 30 days. Recommend re-sign with 5% early renewal bonus.")

    st.markdown("### AI Email Offer Suggestions")
    st.write("- Offer UMD Soccer 10 bonus hours if they renew 60 days early.")
    st.write("- Recommend High School Preseason Package (Aug–Oct) to 3 local teams.")
    st.write("- Build a ‘Club Partner Bundle’ (discount + signage) for heavy users.")