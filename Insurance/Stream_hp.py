#type:ignore

import streamlit as st
import joblib
import numpy as np
import pandas as pd

# ------------------------
# Load the trained model
# ------------------------
with open("HousePrice.pkl", "rb") as f:
    model = joblib.load(f)

st.title("🏠 House Price Prediction App")
st.write("Enter the details below to predict the house price.")

# ------------------------
# User inputs
# ------------------------
bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10, value=3, step=1)
house_size = st.number_input("House Size (sq ft)", min_value=200, max_value=10000, value=1500, step=50)
floor = st.number_input("Floor Number", min_value=1, max_value=50, value=1, step=1)
city = st.selectbox("City", ["Bengaluru", "Gurugram", "Noida"])

# ------------------------
# Prediction
# ------------------------
if st.button("Predict Price"):
    # Create DataFrame for model
    input_data = pd.DataFrame({
        "bedrooms": [bedrooms],
        "house_size": [house_size],
        "floor": [floor],
        "city": [city]
    })

    prediction = model.predict(input_data)
    st.success(f"Predicted Price: ₹{prediction[0]:,.0f}")
