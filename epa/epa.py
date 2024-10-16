import requests
import json 
import pandas as pd
import streamlit as st 
import multiprocessing
import pydeck as pdk
import altair as alt
from streamlit_navigation_bar import st_navbar
import plotly.express as px
import pages as pg
st.set_page_config(layout="wide",initial_sidebar_state="collapsed")

st.markdown("""
<style>

	.stTabs [data-baseweb="tab-list"] {
		gap: 20px;
        background-color: lightblue;
    }

	.stTabs [data-baseweb="tab"] {
        border: none;
        border-bottom: 2px solid #4f4f4f;
        border-radius: 4px 4px 0px 0px;
        padding-top: 5px;
        padding-bottom: 5px;
        color: #4f4f4f;
     }
            
    .stTabs [data-baseweb="tab-list"] p {
        font-size:1.2rem;  font-color:black
    }
    
    div[data-testid="stSidebarHeader"] > img, div[data-testid="collapsedControl"] > img {
      height: 5rem;
      width: auto;
  }
  
  div[data-testid="stSidebarHeader"], div[data-testid="stSidebarHeader"] > *,
  div[data-testid="collapsedControl"], div[data-testid="collapsedControl"] > * {
      display: flex;
      align-items: center;
  }

 </style>""", unsafe_allow_html=True)


pages = ["Home","Exploratory Data Analysis", "Documentation", "ML Models"]

styles = {
    "nav": {
        "background-color": "#7BD192",
    },
    "div": {
        "max-width": "32rem",
        "margin": "175px 50px 75px 100px"
    },
    "span": {
        "border-radius": "0.5rem",
        "padding": "0.4375rem 0.625rem",
        "margin": "0 0.125rem",
    },
    "active": {
        "background-color": "rgba(255, 255, 255, 0.25)",
    },
    "hover": {
        "background-color": "rgba(255, 255, 255, 0.35)",
    },
}

options = {
    "show_menu": True,
    "show_sidebar": True,
    "use_padding" : False
}

page = st_navbar(
    pages,
    options=options,
    styles=styles
)

st.header(page)

if page == "Home":
    st.write ("Welcome to the world of EPA")
    st.image("https://www.epa.gov/sites/epa.gov/files/styles/epa_main_theme_image_large/public/2021-05/California-Map.jpg?itok=pO0p3W8Y", width=700)

#documentation
if page == "Documentation":
    pg.docu()

#machine learning models
if page == "ML Models":
    pg.models()

if page == "Exploratory Data Analysis":
    pg.eda()