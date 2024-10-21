import streamlit as st

def home():
        print ("hello")

def document():
        print ("document")
        
pg = st.navigation([st.Page("home"), st.Page("document")])
pg.run()
