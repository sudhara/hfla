import streamlit as st
from streamlit_navigation_bar import st_navbar

<style>
.appview-container .main .block-container{{
        padding-top: {padding_top}rem;    }}
</style>

page = st_navbar(["Home", "Documentation", "Examples", "Community", "About"])
st.write(page)
