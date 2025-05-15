import streamlit as st

def run():
    st.title("🤖 Sponsorship AI Calculator")

    st.markdown("### Step 1: Select Assets to Include in Package")
    assets = {
        "Field Naming Rights": 10000,
        "Court Banner": 2500,
        "Digital Scoreboard Ad": 1500,
        "Website Logo Placement": 1000,
        "Event Title Sponsor": 7500,
        "Email Blast Inclusion": 1200,
        "Booth Space at Tournament": 2000
    }

    selected_assets = []
    total_value = 0

    for name, value in assets.items():
        if st.checkbox(f"{name} (${value:,})"):
            selected_assets.append(name)
            total_value += value

    st.markdown("### Step 2: Adjust Sponsorship Factors")
    visibility = st.slider("Visibility (1 = low, 10 = national)", 1, 10, 6)
    exclusivity = st.slider("Exclusivity (1 = shared, 10 = exclusive)", 1, 10, 5)
    duration = st.slider("Duration in Months", 1, 36, 12)

    multiplier = 1 + (visibility + exclusivity) / 20
    adjusted_total = total_value * multiplier * (duration / 12)

    st.metric("💵 Estimated Sponsorship Value", f"${adjusted_total:,.2f}")

    st.markdown("### Auto-Tier Recommendation")
    if adjusted_total >= 50000:
        tier = "Platinum"
    elif adjusted_total >= 25000:
        tier = "Gold"
    elif adjusted_total >= 10000:
        tier = "Silver"
    else:
        tier = "Bronze"

    st.success(f"Recommended Tier: {tier}")

    st.markdown("### Perks Unlocked")
    if tier == "Platinum":
        st.write("- Naming rights")
        st.write("- Press release & media exposure")
        st.write("- All lower tier perks")
    elif tier == "Gold":
        st.write("- Event signage + digital reach")
        st.write("- Scoreboard ads")
    elif tier == "Silver":
        st.write("- Booth space")
        st.write("- Website logo")
    else:
        st.write("- Recognition + basic digital presence")

    st.markdown("### Download Summary")
    if st.button("Generate Proposal Summary"):
        summary = f"""Sponsor Proposal Summary
========================

Selected Assets:
{chr(10).join("- " + asset for asset in selected_assets)}

Visibility: {visibility}/10
Exclusivity: {exclusivity}/10
Duration: {duration} months

Estimated Value: ${adjusted_total:,.2f}
Recommended Tier: {tier}
"""
        st.download_button("Download Proposal", summary.encode(), file_name="sponsor_proposal.txt")