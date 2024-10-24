import streamlit as st
import pandas as pd
st.title('😫Machine Learning APP')
st.info('this app buids a machine learning model')
with st.expander('Data'):
  st.write('**Raw data**')
  df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/penguins.csv')
  df
