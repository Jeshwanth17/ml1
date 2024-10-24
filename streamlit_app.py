import streamlit as st
import pandas as pd
st.title('😫Machine Learning APP')
st.info('this app buids a machine learning model')
with st.expander('Data'):
  st.write('**Raw data**')
  df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/penguins.csv')
  df
  st.write('**X**')
  X = df.drop('species',axis =1)
  X
  st.write('**y**')
  y = df.species
  y
with st.expander('Data Visulization'):
  #species,island,bill_length_mm,bill_depth_mm,flipper_length_mm,body_mass_g,sex
  st.scater_chart(data=df,x=',bill_depth_mm',y='body_mass',color='species')
  
