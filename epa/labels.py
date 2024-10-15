import requests
import json 
import pandas as pd
import streamlit as st 
from streamlit_navigation_bar import st_navbar
import plotly.express as px

st.set_page_config(layout="wide",)


@st.cache_data
def load_gitissues():
    response = requests.get("https://api.github.com/repos/hackforla/ops/issues?state=open")
    result =  json.loads(response.text)
    data = pd.json_normalize(result)
    #df = pd.json_normalize(data['labels'])
    st.write(data)
    return df


if __name__ == "__main__":
    st.title("HackForLA - DevOps Issues")
    df = load_gitissues()
    #df = df[["number","title"]]
    #st.write(df)