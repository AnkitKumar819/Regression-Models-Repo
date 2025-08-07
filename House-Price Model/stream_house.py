
# type: ignore

import streamlit as st
import pandas as pd
import joblib

# Load trained pipeline
model = joblib.load("Insurance_pipeline.pkl")  # Make sure this path is correct

# App UI
st.title("🧮 Insurance Price Forecast App")

# Input Fields
age = st.number_input("Enter Age", min_value=0, max_value=100, step=1)
sex = st.selectbox("Select Gender", ['male', 'female'])
bmi = st.number_input("Enter BMI", min_value=0.0, max_value=60.0)
children = st.number_input("Number of Children", min_value=0, max_value=10, step=1)
smoker = st.selectbox("Do you Smoke?", ['yes', 'no'])
region = st.selectbox("Select Region", ['northeast', 'northwest', 'southeast', 'southwest'])

# Prediction Button
if st.button("Predict Insurance Charges"):
    # Create DataFrame from inputs
    input_data = pd.DataFrame({
        'age': [age],
        'sex': [sex],
        'bmi': [bmi],
        'children': [children],
        'smoker': [smoker],
        'region': [region]
    })

    # Predict
    prediction = model.predict(input_data)[0]

    st.success(f"💰 Estimated Insurance Charges: ${prediction:,.2f}")
