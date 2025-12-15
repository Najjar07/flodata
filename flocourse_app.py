import pandas as pd
import joblib
import streamlit as st


model_path = r"C:\Users\LENOVO\Desktop\sk\course_mode.pkl"
encoder_path = r"c:\Users\LENOVO\Desktop\sk\course_encode.pkl"
model = joblib.load(model_path)
encoder = joblib.load(encoder_path)

st.title("Course Recommendation App")
hobby =st.text_input("write your hobby here: ")
passion =st.text_input("write your passion here: ")
technical_requirements =st.text_input("what materials do you have: ")

if st.button("recommended course"):
    sample_data = pd.DataFrame({
    "hobby": [hobby],
    "passion": [passion],
    "technical_requirements": [technical_requirements],
     })


    sample_data['hobby'] = sample_data['hobby'].str.lower()
    sample_data['passion'] = sample_data['passion'].str.lower()
    sample_data['technical_requirements'] = sample_data['technical_requirements'].str.lower()
                                                                        

    converted_sample_data = encoder.transform(sample_data)

    make_recommendation = model.predict(converted_sample_data)

    st.success(f"course: {make_recommendation[0]}")