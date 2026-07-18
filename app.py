import streamlit as st
from xgboost import XGBClassifier
model_1 = XGBClassifier()
model_1.load_model("Heart_Disease_model.json")
st.set_page_config(page_title="Heart Disease Prediction")

st.title("❤️ Heart Disease Prediction")
st.write("Enter the patient's information below:")
age = st.number_input("Age", min_value=1, max_value=120, value=45)

sex = st.selectbox("Sex",["Male", "Female"])
sex_value = 1 if sex == "Male" else 0
cp = st.selectbox("Chest Pain Type",[0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure",min_value=80,max_value=250,value=120)
chol = st.number_input("Cholesterol (chol)",min_value=100,max_value=600,value=200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (fbs)",options=[0, 1])
restecg = st.selectbox("Resting ECG (restecg)",options=[0, 1, 2])
thalach = st.number_input("Maximum Heart Rate (thalach)",min_value=60,max_value=250,value=150)
exang = st.selectbox("Exercise Induced Angina (exang)",options=[0, 1])
oldpeak = st.number_input("Oldpeak",min_value=0.0,max_value=10.0,value=1.0,step=0.1)
slope = st.selectbox("Slope",options=[0, 1, 2])
ca = st.selectbox("Number of Major Vessels (ca)",options=[0, 1, 2, 3, 4])
thal = st.selectbox("Thal",options=[0, 1, 2, 3])
import numpy as np
if st.button("Predict"):
    sex_value = 1 if sex == "Male" else 0
    input_data = np.array([[age,sex_value , cp, trestbps, chol,fbs, restecg, thalach,exang, oldpeak, slope,ca,thal]],dtype=float)
    prediction = model_1.predict(input_data)
    if prediction[0] == 1:
        st.error("❤️ Heart Disease Detected")
    else:
        st.success("💚 No Heart Disease Detected")
