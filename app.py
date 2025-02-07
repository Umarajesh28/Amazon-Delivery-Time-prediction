import streamlit as st 
import numpy as np
import pandas as pd
import pickle

# Load the saved model from the .pkl file
with open("best_xgboost_tuned.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Title of the app
st.title("Amazon Delivery Time Prediction")

# Input fields for user data based on the available features
st.header("Input Order Details")

agent_age = st.number_input("Agent Age", min_value=18, max_value=100, value=30, step=1)
agent_rating = st.number_input("Agent Rating", min_value=0.0, max_value=5.0, value=4.0, step=0.1)
weather = st.selectbox("Weather (0=Clear, 1=Rainy, 2=Foggy)", options=[0, 1, 2])
vehicle = st.selectbox("Vehicle Type (0=Bike, 1=Car, 2=Truck)", options=[0, 1, 2])
area = st.selectbox("Area Type (0=Urban, 1=Suburban, 2=Rural)", options=[0, 1, 2])
distance_km = st.number_input("Distance (km)", min_value=1.0, max_value=500.0, value=10.0, step=0.1)
traffic_encoded = st.selectbox("Traffic Level (0=Low, 1=Medium, 2=High)", options=[0, 1, 2])
category_encoded = st.selectbox("Category Encoded (0=Standard, 1=Express)", options=[0, 1])
pickup_time = st.number_input("Pickup Time (minutes)", min_value=0, max_value=1440, value=30, step=1)

# ✅ Manually define the correct feature order (matching training data)
feature_order = [
    'Agent_Age', 'Agent_Rating', 'Weather', 'Vehicle', 'Area', 
    'Distance_km', 'Traffic_encoded', 'Category Encoded', 'pickup_time(min)'
]

# Prepare the input data as a DataFrame
input_data = pd.DataFrame([[agent_age, agent_rating, weather, vehicle, area, 
                            distance_km, traffic_encoded, category_encoded, pickup_time]], 
                          columns=feature_order)

# ✅ Convert data types to match training data
input_data = input_data.astype(float)  

#📊 Show order summary
st.subheader("🔎 Order Summary")
st.write(input_data)

# 🚀 Make Prediction
if st.button("🚀 Predict Delivery Time"):
    try:
        prediction = model.predict(input_data)
        st.success(f"🕒 Estimated Delivery Time: {prediction[0]:.2f} minutes")
    except Exception as e:
        st.error(f"⚠️ An error occurred during prediction: {e}")
