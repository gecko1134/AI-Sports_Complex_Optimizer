
import streamlit as st
import pandas as pd
from fpdf import FPDF
import uuid

def run():
    st.title("🪪 Batch Badge Generator")
    st.markdown("Upload a CSV with columns: Name, Role, Event")

    uploaded = st.file_uploader("Upload CSV", type="csv")
    if uploaded:
        df = pd.read_csv(uploaded)
        st.dataframe(df)
        st.success("Badges will be generated for each row.")
