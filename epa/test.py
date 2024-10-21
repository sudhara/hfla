import streamlit as st
from streamlit_navigation_bar import st_navbar

st.markdown("""
<style>
.appview-container .main .block-container{{
        padding-top: 100rem;    }}
</style>""", unsafe_allow_html=True)

page = st_navbar(["Home", "Documentation", "Examples", "Community", "About"])

if page == "Home":
        st.write("Home")
elif page == "Documentation":
        st.write("Documentation")
st.write(page)
