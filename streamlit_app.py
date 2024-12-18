import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import numpy as np

st.title('🎈 Jumar Buladaco Project')

st.info('A machine learning app that categorizes penguins')

with st.expander('Data'):
  st.write('*Raw Data')
  df = pd.read_csv('https://raw.githubusercontent.com/akosijumaw/data/refs/heads/main/penguins_cleaned.csv')
  df

  st.write('*X*')
  x_raw = df.drop('species', axis=1)
  x_raw

  st.write('*Y*')
  y_raw = df.species
  y_raw

with st.expander('Visualization'):
 st.scatter_chart(data=df,x='culmen_length_mm', y='body_mass_g', color='species')

 with st.sidebar:
    st.header('Input Feature')
    island = st.selectbox('Island',('Biscoe','Dream','Torgersen'))
    gender = st.selectbox('Gender',('MALE','FEMALE'))
    culmen_length_mm = st.slider('Culmen length (mm)', 32.1, 59.6, 45.1)
    culmen_depth_mm = st.slider('Culmen depth (mm)', 13.1, 21.5, 18.5)
    flipper_length_mm = st.slider('Flipper length (mm)', 172.0, 231.0, 210.5)
    body_mass_g = st.slider('Body mass (g)',2700.0, 6300.0, 4500.1)

data = {'island':island,
        'culmen_length_mm': culmen_length_mm,
        'culmen_depth_mm': culmen_depth_mm,
        'flipper_length_mm': flipper_length_mm,
        'body_mass_g': body_mass_g,
        'sex': gender}
input_df = pd.DataFrame(data, index=[0])
input_penguins = pd.concat([input_df, x_raw], axis=0)

with st.expander('Input Features'):
  st.write('*Input Penguin Data')
  input_df
  st.write('*Combined Penguin Data')
  input_penguins

#encode x
encode = ['island', 'sex']
df_penguins = pd.get_dummies(input_penguins, prefix=encode)
x = df_penguins[1:]
input_row = df_penguins[:1]

#tencode y
target_mapper = {'Adelie': 0,
                  'Chinstrap': 1,
                  'Gentoo' : 2}
def target_encode(val):
  return target_mapper[val]
  
y = y_raw.apply(target_encode)

with st.expander('Data Preparation'):
  st.write('*Encoded X (Input penguin)')
  input_row
  st.write('*Encoded Y')
  y

#train model
clf = RandomForestClassifier()
clf.fit(x, y)

#predict
prediction = clf.predict(input_row)
prediction_proba = clf.predict_proba(input_row)

df_prediction_proba = pd.DataFrame(prediction_proba)
df_prediction_proba.columns = ['Adelie', 'Chinstrap', 'Gento']
df_prediction_proba.rename(columns={0:'Adelie',1:'Chinstrap',2:'Gento'})


#display predicted specie
st.subheader('Prediced Species')


df_prediction_proba




st.dataframe(df_prediction_proba,
        column_config={
          'Adelie' : st.column_config.ProgressColumn(
            'Adelie',
            format='%f',
            width='medium',
            min_value=0,
            max_value=1
          ),
            'Chinstrap' : st.column_config.ProgressColumn(
            'Chinstrap',
            format='%f',
            width='medium',
            min_value=0,
            max_value=1
          ),
            'Gento' : st.column_config.ProgressColumn(
            'Gento',
            format='%f',
            width='medium',
            min_value=0,
            max_value=1
          ),
        }, hide_index=True
)

penguin_species = np.array(['Adelie', 'Chinstrap','Gentoo'])
st.success(str(penguin_species[prediction[0]]))