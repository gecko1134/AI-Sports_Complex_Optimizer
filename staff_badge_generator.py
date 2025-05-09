
import streamlit as st
from fpdf import FPDF
import uuid
from datetime import date

def run():
    st.title("🪪 Badge Generator")

    name = st.text_input("Name")
    role = st.selectbox("Role", ["Referee", "Volunteer", "Staff"])
    event = st.text_input("Event")
    badge_id = str(uuid.uuid4()).split("-")[0].upper()
    badge_date = date.today().isoformat()

    if st.button("Generate Badge"):
        pdf = FPDF(orientation='P', unit='mm', format=(90, 60))
        pdf.add_page()
        pdf.set_font("Arial", "", 12)
        pdf.cell(0, 10, f"{name} - {role}", ln=True)
        pdf.cell(0, 10, f"Event: {event}", ln=True)
        pdf.cell(0, 10, f"Date: {badge_date}", ln=True)
        pdf.cell(0, 10, f"ID: {badge_id}", ln=True)
        path = f"/mnt/data/{name.replace(' ', '_')}_badge.pdf"
        pdf.output(path)
        with open(path, "rb") as f:
            st.download_button("Download Badge", f.read(), file_name=path.split("/")[-1])
