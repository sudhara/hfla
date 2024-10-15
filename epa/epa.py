import requests
import json 
import pandas as pd
import streamlit as st 
import multiprocessing
import pydeck as pdk
import altair as alt
from streamlit_navigation_bar import st_navbar
import plotly.express as px

st.set_page_config(layout="wide",)

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

@st.cache_data
def load_epa():
    #response = requests.get("https://aqs.epa.gov/data/api/dailyData/byState?email=sudha.kirthi@gmail.com&key=cobaltcrane97&param=45201&bdate=20240101&edate=20240630&state=06")
    #response = requests.get("https://aqs.epa.gov/data/api/transactionsQaAnnualPerformanceEvaluations/byCounty?email=sudha.kirthi@gmail.com&key=cobaltcrane97&param=44201&bdate=20230101&edate=20231231&state=06&county=011")
    response = requests.get("https://aqs.epa.gov/data/api/dailyData/byCounty?email=sudha.kirthi@gmail.com&key=cobaltcrane97&param=88101&bdate=20240101&edate=20240630&state=06&county=037")
    result =  json.loads(response.text)
    data = json.dumps(result['Data'])
    df = pd.read_json(data)

    response = requests.get("https://aqs.epa.gov/data/api/dailyData/byCounty?email=sudha.kirthi@gmail.com&key=cobaltcrane97&param=88101&bdate=20230101&edate=20231231&state=06&county=037")
    result =  json.loads(response.text)
    data = json.dumps(result['Data'])
    df1 = pd.read_json(data)

    response = requests.get("https://aqs.epa.gov/data/api/dailyData/byCounty?email=sudha.kirthi@gmail.com&key=cobaltcrane97&param=88101&bdate=20220101&edate=20221231&state=06&county=037")
    result =  json.loads(response.text)
    data = json.dumps(result['Data'])
    df2 = pd.read_json(data)

    response = requests.get("https://aqs.epa.gov/data/api/dailyData/byCounty?email=sudha.kirthi@gmail.com&key=cobaltcrane97&param=88101&bdate=20210101&edate=20211231&state=06&county=037")
    result =  json.loads(response.text)
    data = json.dumps(result['Data'])
    df3 = pd.read_json(data)

    response = requests.get("https://aqs.epa.gov/data/api/dailyData/byCounty?email=sudha.kirthi@gmail.com&key=cobaltcrane97&param=88101&bdate=20200101&edate=20201231&state=06&county=037")
    result =  json.loads(response.text)
    data = json.dumps(result['Data'])
    df4 = pd.read_json(data)

    response = requests.get("https://aqs.epa.gov/data/api/annualData/byCounty?email=sudha.kirthi@gmail.com&key=cobaltcrane97&param=88101,88502&bdate=20240101&edate=20240930&state=06&county=037")
    result =  json.loads(response.text)
    data = json.dumps(result['Data'])
    df10 = pd.read_json(data)

    df = pd.concat([df,df1,df2,df3,df4])
    df['date_local_dt'] = (pd.to_datetime(df['date_local'])) 
    df['dt_local_year'] = df['date_local_dt'].dt.year
    df['dt_local_month'] = df['date_local_dt'].dt.month


    grp_df = df.groupby(['city'])['aqi'].mean()
    grp_df1 = df.groupby(['date_local_dt'])['aqi'].mean()
    grp_df2 = df.groupby(['dt_local_year','city'])['aqi'].mean().to_frame()
    return df, grp_df, grp_df1, grp_df2, df10
 

if __name__=='__main__':
    df, grp_df, grp_df1, grp_df2,df10 = load_epa()
#    with st.sidebar:
#    st.logo("hfla.png")

    page = st_navbar(["Exploratory Data Analysis", "Documentation", "ML Models"])
    st.write(page)

    #documentation
    if page == "Documentation":
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

    #machine learning models
    if page == "ML Models":
        st.balloons()
        st.write("Models Coming Soon")

    if page == "Exploratory Data Analysis":
        st.title("EPA Data - California:2020 - 2024")
        tabA, tabB, tabD, tabE, tabF = st.tabs(["Raw Data", "Summary","Grouped by Date", "BoxPlot","Summary Data"])
        #raw data
        with tabA:
            st.subheader("Raw Data from EPS site")
            st.write(df)

        #summary stats
        with tabB:
            st.subheader("Summary")
            st.dataframe(df.describe().T, use_container_width=True, height=700)

        # #grouped chart by city
        # with tabC:
        #     st.subheader("Bar chart - Mean by city")
        #     st.bar_chart(grp_df, x=None, y="aqi")

        #grouped chart by date
        with tabD:
            st.subheader("AQI chart by Date")
            st.line_chart(grp_df1)
        
        #box plot
        with tabE:
            fig = px.box(
                    df,
                    x="city",
                    y="aqi",
                    color = 'dt_local_year',
                    notched = True,
                    title = "Box Plot by City for 2020 - 2024"
                )
            st.plotly_chart(fig, theme="streamlit", use_container_width=True)

        #summary data
        with tabF:
            st.subheader("Summary Data")
            st.write(df10)
            df11 = df10.loc[df10.groupby(['metric_used','pollutant_standard'])['arithmetic_mean'].idxmax()][['metric_used','pollutant_standard','arithmetic_mean','observation_count','standard_deviation','units_of_measure','first_max_value','first_max_datetime']]
            st.subheader("Maximum arithmetic mean Observation Data for year 2024")
            st.write(df11)
