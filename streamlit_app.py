import streamlit as st
import pandas as pd

st.title('🎈 Jumar Buladaco Project')

st.info('A machine learning app that categorizes penguins')

with st.expander('Data'):
  st.write('**Raw Data')
  df = pd.read_csv('https://raw.githubusercontent.com/akosijumaw/data/refs/heads/main/penguins_cleaned.csv')
  df
