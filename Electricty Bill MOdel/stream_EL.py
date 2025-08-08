#type:ignore
import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("Elect_Bill.pkl")  # Change to your actual file path

st.title("Wind Energy Prediction App")

st.write("Enter the following feature values:")

# Input fields for all features
DayOfWeek = st.number_input("DayOfWeek", min_value=1, max_value=7, value=2)
ForecastWindProduction = st.text_input("ForecastWindProduction", value=328.57)
SystemLoadEA = st.text_input("SystemLoadEA", value=3060.71)
SMPEA = st.text_input("SMPEA", value=49.10)
ORKTemperature = st.text_input("ORKTemperature", value=5.00)
CO2Intensity = st.text_input("CO2Intensity", value=589.97)
ActualWindProduction = st.text_input("ActualWindProduction", value=311.00)
SystemLoadEP2 = st.text_input("SystemLoadEP2", value=2834.00)


# Predict button
if st.button("Predict"):
    import pandas as pd

# Keep the same column order used in training
    col_names = ['DayOfWeek', 'ForecastWindProduction', 'SystemLoadEA', 'SMPEA',
             'ORKTemperature', 'CO2Intensity', 'ActualWindProduction', 'SystemLoadEP2']

    features = pd.DataFrame([[DayOfWeek, ForecastWindProduction, SystemLoadEA, SMPEA,
                          ORKTemperature, CO2Intensity, ActualWindProduction,
                          SystemLoadEP2]], columns=col_names)

    prediction = model.predict(features)
    st.success(f"Predicted Value: {prediction[0]:.2f}")
