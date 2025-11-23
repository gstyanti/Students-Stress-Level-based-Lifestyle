import streamlit as st
import joblib
import numpy as np
import sys

#Display environment info
st.sidebar.write("**Environtment Info:**")
st.sidebar.write(f"Python version: {sys.version.split()[0]}")
st.sidebar.write(f"Numpy: {np.__version__}")

try:
   model = joblib.load("students-rf-model.joblib")
   st.success("✅ Model loaded successfully!")

except FileNotFoundError:
   st.error("❌ Model file not found. Please ensure 'students-rf-model.joblib' is in the correct directory.")
   st.stop()

st.title('Student Stress Level Prediction')

# Input fields
study_hours = st.number_input("Enter Study Hours", min_value=0, max_value=24, value=0)
extracurricular = st.number_input("Enter Extracurricular Hours", min_value=0, max_value=24, value=0)
sleep_hours = st.number_input("Enter Sleep Hours", min_value=0, max_value=24, value=0)
social_hours = st.number_input("Enter Social Hours", min_value=0, max_value=24, value=0)
physical_activity = st.number_input("Enter Physical Activity", min_value=0, max_value=24, value=0)
gpa = st.number_input("Enter GPA", min_value=0.0, max_value=4.0, value=0.0)

if st.button("🎲 Predict Stress Level", type="primary"):
    try:
        # Create input array
        input_data = np.array([[
            study_hours,
            extracurricular, 
            sleep_hours,
            social_hours,
            physical_activity,
            gpa
        ]])
        
        # Prediction
        prediction = model.predict(input_data)
        
        # Stress labels dengan emoji
        stress_labels = {
            0: "😊 Low Stress - You're doing great!",
            1: "😐 Moderate Stress - Take some breaks!", 
            2: "😰 High Stress - Time to relax and seek help!"
        }
        
        result = stress_labels.get(prediction[0], "Unknown")
        
        # Display result dengan color coding
        if prediction[0] == 0:
            st.success(f"## {result}")
        elif prediction[0] == 1:
            st.warning(f"## {result}")
        else:
            st.error(f"## {result}")
            
        # Additional info
        with st.expander("📈 See input details"):
            st.write(f"Study Hours: {study_hours}")
            st.write(f"Extracurricular: {extracurricular}")
            st.write(f"Sleep Hours: {sleep_hours}") 
            st.write(f"Social Hours: {social_hours}")
            st.write(f"Physical Activity: {physical_activity}")
            st.write(f"GPA: {gpa}")
        
    except Exception as e:
        st.error(f"❌ Prediction error: {e}")