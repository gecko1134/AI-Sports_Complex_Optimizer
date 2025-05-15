import streamlit as st

def run():
    st.title("🧠 AI Sponsor Matchmaker")

    st.markdown("Select your sponsorship goal:")
    goal = st.radio("Goal", ["Max Revenue", "Max Exposure", "Youth Development", "Balanced"])

    if goal:
        st.success(f"🧠 AI recommends:")
        if goal == "Max Revenue":
            st.write("- Assign Nike to Dome Banner")
            st.write("- Offer Platinum tier to National Bank")
        elif goal == "Max Exposure":
            st.write("- Feature Health Co. in Wellness Events")
        elif goal == "Youth Development":
            st.write("- Match Local Credit Union with U12 League")
        elif goal == "Balanced":
            st.write("- Distribute sponsorship across 3 programs")