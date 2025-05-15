import streamlit as st
import pandas as pd

def run():
    st.title("🪪 Membership Manager")

    data = {
        "Name": ["Jordan Smith", "Casey Lee"],
        "Tier": ["Elite", "Team"],
        "Renewal": ["2024-12-01", "2024-08-15"],
        "Status": ["Active", "Pending"]
    }

    df = pd.DataFrame(data)
    st.dataframe(df)
    st.markdown("Filter, upgrade, or export members as needed.")
    st.download_button("Download Member List", df.to_csv(index=False), "members.csv")