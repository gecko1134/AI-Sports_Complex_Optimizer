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
    tier_filter = st.selectbox("Filter by Tier", ["All"] + sorted(df["Tier"].unique().tolist()))
    if tier_filter != "All":
        df = df[df["Tier"] == tier_filter]

    st.dataframe(df)
    st.download_button("Download Members CSV", df.to_csv(index=False), "members.csv")