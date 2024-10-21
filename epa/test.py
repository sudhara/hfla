import streamlit as st
from streamlit_navigation_bar import st_navbar

style = {
"appview-container" : {"padding-top": "100px",},
"main" : {"padding-top": "100px",},
"block-container" : {"padding-top": "100px",}
}

page = st_navbar(["Home", "Documentation", "Examples", "Community", "About"], styles=style)

if page == "Home":
        st.write("Home")
elif page == "Documentation":
        st.write("Documentation")
st.write(page)
