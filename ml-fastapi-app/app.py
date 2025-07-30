import streamlit as st
import numpy as np
import joblib

# Load your model
model = joblib.load("model.pkl")

# Streamlit Page Config
st.set_page_config(page_title="Electricity Cost Predictor")
st.title("⚡ Electricity Cost Prediction App")

st.write("Fill in the building/environment details below to predict electricity cost:")

# Input fields
site_area = st.number_input("Site Area (sq ft)", min_value=0)
water_consumption = st.number_input("Water Consumption", min_value=0.0)
recycling_rate = st.slider("Recycling Rate (%)", min_value=0, max_value=100)
utilisation_rate = st.slider("Utilisation Rate (%)", min_value=0, max_value=100)
air_quality_index = st.number_input("Air Quality Index", min_value=0)
issue_resolution_time = st.number_input("Issue Resolution Time (in days)", min_value=0)

# Structure Type Encoding
structure_mapping = {
    'Mixed-use': 0,
    'Commercial': 1,
    'Residential': 2,
    'Industrial': 3
}
structure_type_str = st.selectbox("Structure Type", options=list(structure_mapping.keys()))
structure_type_encoded = structure_mapping[structure_type_str]

resident_count = st.number_input("Resident Count ", format="%.6f")

# Predict Button
if st.button("Predict Electricity Cost"):
    features = np.array([[
        site_area,
        water_consumption,
        recycling_rate,
        utilisation_rate,
        air_quality_index,
        issue_resolution_time,
        structure_type_encoded,
        resident_count
    ]])

    prediction = model.predict(features)
    st.success(f"Predicted Electricity Cost: ₹{prediction[0]:,.2f}")
