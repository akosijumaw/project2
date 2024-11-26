import streamlit as st
import pandas as pd

st.title('🎈 Jumar Buladaco Project')

st.info('A machine learning app that categorizes penguins')

with st.expander('Data'):
  st.write('*Raw Data')
  df = pd.read_csv('https://raw.githubusercontent.com/akosijumaw/data/refs/heads/main/penguins_cleaned.csv')
  df

  st.write('*X*')
  x = df.drop('species', axis=1)
  x

  st.write('*Y*')
  y = df.species
  y

with st.expander('Visualization'):
 st.scatter_chart(data=df,x='culmen_length_mm', y='body_mass_g', color='species')

 with st.sidebar:
    st.header('Input Feature')
    island = st.selectbox('Island',('Biscoe','Dream','Torgersen'))
    gender = st.selectbox('Gender',('MALE','FEMALE'))
    culmen_length_mm = st.slider('Culmen length (mm)', 32.1, 59.6, 45.1)
    culmen_depth_mm = st.slider('Culmen depth (mm)', 13.1, 21.5, 18.5)
    flipper_length_mm = st.slider('Flipper length (mm)', 172.0, 231.0, 210.5)