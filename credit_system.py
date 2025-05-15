import streamlit as st
import pandas as pd

def run():
    st.title("🎟️ Membership Credit System")

    credits = pd.DataFrame({
        "Member": ["Jordan Smith", "Casey Lee"],
        "Tier": ["Elite", "Team"],
        "Credits Remaining": [12, 4],
        "Used This Month": [3, 6]
    })

    st.dataframe(credits)
    st.download_button("Download Credit Report", credits.to_csv(index=False), "credit_report.csv")