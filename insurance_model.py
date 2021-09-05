# Import modules
import streamlit as st
import numpy as np
import pandas as pd
from xgboost import XGBRFRegressor
from sklearn.linear_model import LinearRegression
import xgboost

@st.cache
def load_data():
    # Load the dataset
    df = pd.read_csv("insurance_medical.csv")

    # Change values to numerical
    df.replace(to_replace={"male":0, "female":1, "no":0, "yes":1, "northwest": 0, "northeast":1, "southeast":2, "southwest":3}, inplace=True)

    # Split data into feature and target
    X = df.drop(['charges'], axis=1)
    y = df['charges']

    # Return values
    return X,y

@st.cache
def model():
    # Load features and target
    X, y = load_data()

    # Create model and get accuracy.
    model = LinearRegression()
    model.fit(X, y)
    acc = model.score(X, y)

    # return accuracy
    return model, acc