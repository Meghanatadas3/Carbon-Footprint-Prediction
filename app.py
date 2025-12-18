import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title='Carbon Footprint Predictor', page_icon='🌿')

st.title('AI for Sustainability — Carbon Footprint Prediction')
st.write('Enter lifestyle and activity details to predict your estimated Carbon Emission.')

# Load trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# User Inputs (linear flow — no functions or conditionals)
monthly_grocery_bill = st.number_input('Monthly Grocery Bill (₹)', min_value=0, max_value=100000, value=2000)
vehicle_distance = st.number_input('Vehicle Monthly Distance (Km)', min_value=0, max_value=20000, value=500)
tv_hours = st.number_input('How Long TV/PC Daily (hours)', min_value=0, max_value=24, value=5)
clothes = st.number_input('How Many New Clothes Monthly', min_value=0, max_value=50, value=5)
internet_hours = st.number_input('How Long Internet Daily (hours)', min_value=0, max_value=24, value=4)

# DataFrame for prediction
input_data = pd.DataFrame({
    'Monthly Grocery Bill': [monthly_grocery_bill],
    'Vehicle Monthly Distance Km': [vehicle_distance],
    'How Long TV PC Daily Hour': [tv_hours],
    'How Many New Clothes Monthly': [clothes],
    'How Long Internet Daily Hour': [internet_hours]
})

# Prediction
prediction = model.predict(input_data)

st.subheader('Predicted Carbon Emission')
st.metric(label='Estimated CO₂ Emission', value=str(round(float(prediction[0]), 2)) + ' units')

st.markdown('---')
st.write('Model performance details:')
with open('model_info.txt', 'r') as f:
    info = f.read()
st.code(info)
