from pandas.core.api import DataFrame
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
import seaborn as sns


# Load some data
url='https://drive.google.com/file/d/1aWkNwXLI8jmu-cj0OTHM23M19XGKt0e0/view'
url='https://drive.google.com/uc?id=' + url.split('/')[-2]
df = pd.read_csv(url) 

# Add title and header
st.title("Internet Access Around the Globe")
st.header("Internet usage data")




# Widgets: checkbox (you can replace st.xx with st.sidebar.xx)
if st.checkbox("Show Dataframe"):
    st.header("This is my dataset:")
    st.dataframe(data=df)
    # st.table(data=iris)
    # st.write(data=iris)

# Setting up columns
left_column, middle_column, right_column = st.columns([2, 2, 1])

# Widgets: selectbox
country = ["All"]+sorted(pd.unique(df['Entity']))
country = left_column.selectbox("Choose a country", country)

# Widgets: radio buttons
show_means = middle_column.radio(
    label='Show Class Means', options=['Yes', 'No'])

st.write(country)
st.write(show_means)
