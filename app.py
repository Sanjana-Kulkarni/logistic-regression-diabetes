import streamlit as st
import pandas as pd
import numpy as np
import pickle

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Diabetes Prediction",
    page_icon="🩺",
    layout="centered"
)

st.title("🩺 Diabetes Prediction using Logistic Regression")
st.write(
    "Enter the patient's details below to predict whether "
    "the patient is likely to have diabetes."
)

# --------------------------------------------------
# Load Trained Model
# --------------------------------------------------

with open("logistic_regression_model.pkl", "rb") as file:
    model = pickle.load(file)

# --------------------------------------------------
# User Input
# --------------------------------------------------

Pregnancies = st.number_input(
    "Pregnancies",
    min_value=0,
    max_value=20,
    value=1
)

Glucose = st.number_input(
    "Glucose",
    min_value=0.0,
    max_value=300.0,
    value=120.0
)

BloodPressure = st.number_input(
    "Blood Pressure",
    min_value=0.0,
    max_value=200.0,
    value=70.0
)

SkinThickness = st.number_input(
    "Skin Thickness",
    min_value=0.0,
    max_value=100.0,
    value=20.0
)

Insulin = st.number_input(
    "Insulin",
    min_value=0.0,
    max_value=900.0,
    value=80.0
)

BMI = st.number_input(
    "BMI",
    min_value=0.0,
    max_value=70.0,
    value=30.0
)

DiabetesPedigreeFunction = st.number_input(
    "Diabetes Pedigree Function",
    min_value=0.0,
    max_value=3.0,
    value=0.5
)

Age = st.number_input(
    "Age",
    min_value=1,
    max_value=120,
    value=30
)

# --------------------------------------------------
# Preprocessing
# Same preprocessing used in the notebook
# --------------------------------------------------

if st.button("Predict Diabetes"):

    # Create input dataframe
    input_data = pd.DataFrame({
        "Pregnancies": [Pregnancies],
        "Glucose": [Glucose],
        "BloodPressure": [BloodPressure],
        "SkinThickness": [SkinThickness],
        "Insulin": [Insulin],
        "BMI": [BMI],
        "DiabetesPedigreeFunction": [DiabetesPedigreeFunction],
        "Age": [Age]
    })

    # Columns where 0 was treated as missing
    columns = [
        "Glucose",
        "BloodPressure",
        "SkinThickness",
        "Insulin",
        "BMI"
    ]

    # Load dataset to calculate the same median values
    df = pd.read_csv("diabetes.csv")

    # Replace 0 with NaN
    df[columns] = df[columns].replace(0, np.nan)

    # Fill missing values with median
    for column in columns:
        median_value = df[column].median()

        if input_data[column].iloc[0] == 0:
            input_data[column] = median_value

    # --------------------------------------------------
    # Prediction
    # --------------------------------------------------

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1]

    # --------------------------------------------------
    # Display Result
    # --------------------------------------------------

    if prediction == 1:
        st.error("⚠️ Prediction: The patient is likely to have diabetes.")
    else:
        st.success("✅ Prediction: The patient is unlikely to have diabetes.")

    st.write(
        f"**Probability of diabetes:** {probability * 100:.2f}%"
    )