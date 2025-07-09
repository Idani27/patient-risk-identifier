# main.py

import streamlit as st
import pickle  # or joblib, depending on your model

# Load your model (update this path if needed)
model = pickle.load(open('models/suicide_risk_model.pkl', 'rb'))

st.set_page_config(page_title="Suicide Risk Predictor")
st.title("🧠 Suicide Risk Predictor")
st.write("This tool uses mental health indicators to assess whether a student may be at risk and needs support.")

# Form
with st.form("risk_form"):
    depression = st.selectbox("Do you have Depression?", ["Yes", "No"])
    anxiety = st.selectbox("Do you have Anxiety?", ["Yes", "No"])
    panic = st.selectbox("Do you have Panic attacks?", ["Yes", "No"])
    treatment = st.selectbox("Have you sought treatment?", ["Yes", "No"])
    submitted = st.form_submit_button("🔎 Predict")

# Predict
import pandas as pd

input_df = pd.DataFrame([input_data], columns=['depression', 'anxiety', 'panic', 'treatment'])
prediction = model.predict(input_df)[0]

    # Make prediction
    prediction = model.predict([input_data])[0]  # Adjust if your model needs different input

    # Display result
    if prediction == 1:
        st.markdown("<p class='risk'>⚠️ At risk. Please consider seeking professional help.</p>", unsafe_allow_html=True)
    else:
        st.markdown("<p class='safe'>✅ Safe. Keep taking care of your mental well-being!</p>", unsafe_allow_html=True)

# Optional: Add custom styling
st.markdown("""
    <style>
    .risk {
        color: red;
        font-weight: bold;
        font-size: 18px;
    }
    .safe {
        color: green;
        font-weight: bold;
        font-size: 18px;
    }
    </style>
""", unsafe_allow_html=True)
