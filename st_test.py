import streamlit as st
import pickle

with open("data.pkl", "rb") as f:
    model = pickle.load(f)


data = st.slider('Enter a value',min_value=1.0, max_value=150.0, step=0.2, key='data_slider')
df=[data]
if st.button('Submit'):
    prediction=model.predict([[data]])
    st.write(f'The predicted value is: {prediction[0]}')

