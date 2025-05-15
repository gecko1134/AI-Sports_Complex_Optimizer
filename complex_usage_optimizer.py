import streamlit as st
import pandas as pd
from datetime import datetime

def run():
    st.title("🏟️ Complex Usage Optimizer with AI")

    st.markdown("### Input a Usage Block")
    surface = st.selectbox("Surface", ["Turf A", "Turf B", "Court 1", "Court 2", "Court 3"])
    sport = st.selectbox("Sport", ["Soccer", "Basketball", "Volleyball", "Pickleball", "Cricket"])
    use_type = st.selectbox("Use Type", ["Practice", "Game", "Scrimmage", "Tournament"])
    user_type = st.selectbox("User Type", ["Recreation", "Adult", "Youth", "High School"])
    referees = st.number_input("Referees Needed", 0, 5, 0)
    equipment_needed = st.multiselect("Equipment Needed", ["Nets", "Balls", "Cones", "Cricket Gear"])
    coach_assigned = st.radio("Coach Assigned", ["Yes", "No"])
    hours = st.slider("Block Duration (Hours)", 0.5, 4.0, 1.0, 0.5)
    attendees = st.number_input("Expected Attendance", 1, 100, 10)
    add_btn = st.button("Add Usage Block")

    if "usage_log" not in st.session_state:
        st.session_state.usage_log = []

    if add_btn:
        st.session_state.usage_log.append({
            "Surface": surface,
            "Sport": sport,
            "Use Type": use_type,
            "User Type": user_type,
            "Referees": referees,
            "Equipment": ", ".join(equipment_needed),
            "Coach": coach_assigned,
            "Hours": hours,
            "Attendees": attendees,
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    st.markdown("### Current Usage Log")
    if st.session_state.usage_log:
        df = pd.DataFrame(st.session_state.usage_log)
        st.dataframe(df)

        # AI Optimization Suggestion Engine (simple example logic)
        st.markdown("### 🧠 AI Suggestions")
        underused = df[df["Hours"] <= 1]
        if not underused.empty:
            st.warning("Consider extending or combining underused time blocks.")
        empty_surfaces = {"Turf A", "Court 3"} - set(df["Surface"])
        if empty_surfaces:
            st.info(f"🕓 These surfaces are still open: {', '.join(empty_surfaces)}")

        if "Cricket" not in df["Sport"].values:
            st.info("📢 Consider marketing to cricket clubs to expand usage.")

        st.download_button("Download Usage Log", df.to_csv(index=False), "complex_usage_log.csv")