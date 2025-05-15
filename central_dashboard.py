import streamlit as st
import pandas as pd

def run():
    st.title("📊 Central Dashboard")
    st.metric("Total Revenue This Month", "$18,750")
    st.metric("Active Members", 187)
    st.metric("Contracts Nearing Renewal", 3)