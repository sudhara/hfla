import streamlit as st
from streamlit_navigation_bar import st_navbar

st.markdown("""
<style>
.appview-container .main .block-container{{
        padding-top: {padding_top}rem;    }}
</style>""", unsafe_allow_html=True)

page = st_navbar(["Home", "Documentation", "Examples", "Community", "About"])
st.write(page)
