import streamlit as st
import pandas as pd

def run():
    st.title("🎟️ Membership Credit Tracker")

    credits = pd.DataFrame({
        "Member": ["Jordan Smith", "Casey Lee", "Dana Kim"],
        "Tier": ["Elite", "Family", "Basic"],
        "Credits Bought": [50, 30, 10],
        "Credits Used": [35, 20, 4],
        "Credits Remaining": [15, 10, 6]
    })

    st.dataframe(credits)
    st.download_button("Download Credit Report", credits.to_csv(index=False), "member_credits.csv")