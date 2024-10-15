import numpy as np
import pandas as pd
import streamlit as st

@st.cache_data
def load_data(rows):
    chart_data = pd.DataFrame(
        np.random.randn(rows, 10),
        columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
    )
    # Contains a static element st.area_chart
    st.area_chart(chart_data) # This will be recorded and displayed even when the function is skipped
    return chart_data

df = load_data(20)
st.dataframe(df)