import streamlit as st
import pandas as pd

def run():
    st.title("🌐 AI Competitor Facility Insights")

    st.markdown("### What Other Complexes Are Doing (AI Monitored Trends)")

    trends = pd.DataFrame({
        "Facility": ["MegaDome TX", "Elite Arena NY", "The Hub CA", "Midwest Sports Park"],
        "Trending Sport": ["Cricket", "Youth Volleyball", "Indoor Soccer", "Pickleball"],
        "New Configurations": ["2x turf split for futsal", "volley pods", "turf tiles for events", "4 pickleball overlay"],
        "Price Change ($/hr)": ["+10%", "-5%", "Stable", "+15%"],
        "Last Update": ["Today", "Yesterday", "2 days ago", "Today"]
    })

    st.dataframe(trends)

    st.markdown("### Suggestions for Venture North")
    st.success("- Consider offering Cricket drop-in blocks (2–4pm, Mon–Wed)")
    st.success("- Test 'pod-style' court layout for Volleyball League")
    st.info("- Raise weekday turf rental to $225/hr based on TX/CA comparisons")
    st.info("- Promote 3-court Pickleball tournaments on off-peak Saturdays")