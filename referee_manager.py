import streamlit as st
import pandas as pd

def run():
    st.title("⚖️ Referee Manager")

    refs = pd.DataFrame({
        "Referee": ["Mike", "Sara"],
        "Certified": [True, True],
        "Games This Month": [3, 4]
    })
    st.dataframe(refs)

    assign = st.text_input("Assign Ref to Game")
    if st.button("Assign"):
        st.success(f"Assigned {assign} to next available game.")