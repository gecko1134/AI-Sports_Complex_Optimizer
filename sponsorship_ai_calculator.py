import streamlit as st
import pandas as pd

def run():
    st.title("🤖 Advanced Sponsorship AI Calculator")

    st.markdown("### Step 1: Select Sponsorship Assets")
    assets = {
        "Field Naming Rights": 10000,
        "Court Banner": 2500,
        "Digital Scoreboard Ad": 1500,
        "Website Logo": 1000,
        "Event Title Sponsorship": 7500,
        "Email Blast Inclusion": 1200,
        "Booth at Tournament": 2000
    }

    selected_assets = []
    total_base = 0

    for asset, value in assets.items():
        if st.checkbox(f"{asset} (${value})"):
            selected_assets.append(asset)
            total_base += value

    st.markdown("### Step 2: Customize Sponsorship Details")

    visibility = st.slider("Visibility Level (1 = low, 10 = national)", 1, 10, 6)
    exclusivity = st.slider("Exclusivity (1 = shared, 10 = exclusive)", 1, 10, 5)
    duration_months = st.slider("Contract Length (months)", 1, 36, 12)

    modifier = (visibility * 0.1 + exclusivity * 0.1 + duration_months / 12)
    estimated_value = total_base * modifier

    st.metric("📈 Estimated Deal Value", f"${estimated_value:,.2f}")

    st.markdown("### Auto-Recommendation")
    if estimated_value >= 50000:
        tier = "Platinum"
    elif estimated_value >= 25000:
        tier = "Gold"
    elif estimated_value >= 10000:
        tier = "Silver"
    else:
        tier = "Bronze"

    st.success(f"Suggested Tier: **{tier}**")

    st.markdown("### Perks Unlocked")
    if tier == "Platinum":
        st.markdown("- Naming rights")
        st.markdown("- Digital + physical signage")
        st.markdown("- Press release + media push")
        st.markdown("- VIP passes to events")
    elif tier == "Gold":
        st.markdown("- Scoreboard & court signage")
        st.markdown("- Tournament exposure")
    elif tier == "Silver":
        st.markdown("- Booth space")
        st.markdown("- Social media mentions")
    else:
        st.markdown("- Website logo + basic placement")

    st.markdown("### Industry Benchmark Insights")
    st.info("Other complexes offering:
- $100,000/yr stadium naming deals
- $5,000 court banners
- $10,000 for email/event bundles")

    if st.button("Generate Proposal Summary"):
        summary = f"""
Sponsor AI Proposal Summary
===========================
Assets Selected:
{', '.join(selected_assets)}

Visibility: {visibility}
Exclusivity: {exclusivity}
Duration: {duration_months} months

Estimated Value: ${estimated_value:,.2f}
Suggested Tier: {tier}
"""
        st.download_button("Download Proposal", summary.encode(), file_name="sponsorship_proposal.txt")