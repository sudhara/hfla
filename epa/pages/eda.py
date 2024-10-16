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

def eda():
    df, grp_df, grp_df1, grp_df2,df10 = load_epa()
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
