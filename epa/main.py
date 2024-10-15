import requests
from flask import Flask, jsonify, request
import json 
import pandas as pd
import streamlit as st 
import multiprocessing

must_reload_page = False
def start_flask():
    if not hasattr(st, 'already_started_server'):
        # Hack the fact that Python modules (like st) only load once to
        # keep track of whether this file already ran.
        st.already_started_server = True
        must_reload_page = True
        app = Flask(__name__)
        app.run(port=5001)

        hello = [ {'message': 'Hello World'}]
        @app.route("/")
        def hello_world():
            return jsonify(hello)

def reload_page():
    if must_reload_page:
        must_reload_page = False
        st.experimental_rerun()

if __name__=='__main__':
    flask_process = multiprocessing.Process(target=start_flask)
    reload_process = multiprocessing.Process(target=reload_page)
    flask_process.start()
    reload_process.start()

response = requests.get("https://aqs.epa.gov/data/api/transactionsQaAnnualPerformanceEvaluations/byCounty?email=sudha.kirthi@gmail.com&key=cobaltcrane97&param=44201&bdate=20170101&edate=20171231&state=06&county=011")
result =  json.loads(response.text)
data = json.dumps(result['Data'])
df = pd.read_json(data)
st.write(df.describe())