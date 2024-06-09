import pandas as pd
from sklearn.linear_model import LogisticRegression
import streamlit as st
import joblib

def main():
    st.title("Heart Disease Prediction System")

    # Input fields for user information
    age = st.slider("Age", min_value=0, max_value=150, step=1, value=50)
    sex = st.selectbox("Sex", ["Male", "Female"])
    cp = st.selectbox("Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"])
    trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=0, max_value=300, step=1)
    chol = st.number_input("Serum Cholesterol (mg/dl)", min_value=0, max_value=600, step=1)
    fbs = st.selectbox("Fasting Blood Sugar (> 120 mg/dl)", ["False", "True"])
    restecg = st.selectbox("Resting Electrocardiographic Results", ["Normal", "ST-T wave abnormality", "Probable or definite left ventricular hypertrophy"])
    thalach = st.slider("Maximum Heart Rate Achieved", min_value=0, max_value=300, step=1, value=150)
    exang = st.selectbox("Exercise Induced Angina", ["No", "Yes"])
    oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.0, max_value=10.0, step=0.1)
    slope = st.selectbox("Slope of the Peak Exercise ST Segment", ["Upsloping", "Flat", "Downsloping"])
    ca = st.number_input("Number of Major Vessels Colored by Fluoroscopy", min_value=0, max_value=4, step=1)
    thal = st.selectbox("Thalassemia", ["Normal", "Fixed Defect", "Reversible Defect"])

    if st.button("Predict"):
        model = joblib.load('model_joblib_heart')
        sex = 1 if sex == "Male" else 0
        fbs = 1 if fbs == "True" else 0
        exang = 1 if exang == "Yes" else 0
        # Mapping categorical values to numeric for model prediction
        cp_mapping = {"Typical Angina": 0, "Atypical Angina": 1, "Non-Anginal Pain": 2, "Asymptomatic": 3}
        slope_mapping = {"Upsloping": 0, "Flat": 1, "Downsloping": 2}
        restecg_mapping = {"Normal": 0, "ST-T wave abnormality": 1, "Probable or definite left ventricular hypertrophy": 2}
        thal_mapping = {"Normal": 0, "Fixed Defect": 1, "Reversible Defect": 2}
        
        cp = cp_mapping[cp]
        slope = slope_mapping[slope]
        restecg = restecg_mapping[restecg]
        thal = thal_mapping[thal]
        
        # Predicting the result
        result = model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        if result == 0:
            st.write("No Heart Disease")
        else:
            st.write("Yes")

if __name__ == "__main__":
    main()
