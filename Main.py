import streamlit as st
import prediction

st.title("My Insurance Prediction Website")
st.markdown("### The ML model uses Linear Refression Algo to make predictions")

st.title('Welcome')
st.markdown('In this app We will predict your Insurance Charges by  takig some Inputs')
st.markdown('Go to next Prediction Page to do the Prediction')

st.sidebar.title("Navigation")
page = st.sidebar.radio("Pages", ["Home", "Prediction"])

if (page == "Prediction"):
    prediction.app()