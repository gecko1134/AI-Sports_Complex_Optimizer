
import streamlit as st

def run():
    st.title("📖 Investor Pitch Deck (Flipbook Viewer)")

    st.markdown(
        '''
        <iframe src="https://online.flippingbook.com/view/893923349/"
                width="100%" height="600" style="border:none;" allowfullscreen="true">
        </iframe>
        ''',
        unsafe_allow_html=True
    )

    st.info("Use the toolbar to zoom, go fullscreen, or share the flipbook.")
