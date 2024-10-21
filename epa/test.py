import streamlit as st
from streamlit_navigation_bar import st_navbar

styles = {
"appview-container" "main" "block-container" : {
        "padding-top": "100px"}
}

page = st_navbar(["Home", "Documentation", "Examples", "Community", "About"], styles=styles)

if page == "Home":
        st.write("Home")
elif page == "Documentation":
        st.write("Documentation")
st.write(page)
