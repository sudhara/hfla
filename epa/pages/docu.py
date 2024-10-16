import requests
import json 
import pandas as pd
import streamlit as st 
import multiprocessing
import pydeck as pdk
import altair as alt
from streamlit_navigation_bar import st_navbar
import plotly.express as px


def docu():
    d = {'Levels of Concern': ['Good','Moderate','Unhealthy for Sensitive Groups','Unhealthy','Very Unhealthy','Hazardous']
            , 'Values of Index': ['o to 50', '51 to 100', '101 to 150', '151 to 200','201 to 300','301 and higher']
            , 'Description': ['Air quality is satisfactory, and air pollution poses little or no risk.'
                            ,'Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution.'
                            ,'Members of sensitive groups may experience health effects. The general public is less likely to be affected.'
                            ,'Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects.'
                            ,'Health alert: The risk of health effects is increased for everyone.'
                            ,'Health warning of emergency conditions: everyone is more likely to be affected.']
            }
    aqi_df = pd.DataFrame(data=d)
    st.subheader("AQI Levels of Concern and Values of Index")
    multi1 = '''What is the U.S. Air Quality Index (AQI)?

                The U.S. AQI is EPA’s index for reporting air quality.'''
    multi2 = '''How does the AQI work?

                    Think of the AQI as a yardstick that runs from 0 to 500. The higher the AQI value, the greater the level of air pollution and the greater the health concern. 
    For example, an AQI value of 50 or below represents good air quality, while an AQI value over 300 represents hazardous air quality.
    For each pollutant an AQI value of 100 generally corresponds to an ambient air concentration that equals the level of the short-term national ambient air quality 
    standard for protection of public health. AQI values at or below 100 are generally thought of as satisfactory. 
    When AQI values are above 100, air quality is unhealthy: at first for certain sensitive groups of people, then for everyone as AQI values get higher.
    The AQI is divided into six categories. Each category corresponds to a different level of health concern. 
    Each category also has a specific color. 
    The color makes it easy for people to quickly determine whether air quality is reaching unhealthy levels in their communities.'''
    st.markdown(multi1)
    st.markdown(multi2)
    st.dataframe(aqi_df)