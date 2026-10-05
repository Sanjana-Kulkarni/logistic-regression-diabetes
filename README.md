# Diabetes Prediction using Logistic Regression

A machine learning classification project that uses **Logistic Regression** to predict whether a person is likely to have diabetes based on medical and demographic features.

The project covers data preprocessing, exploratory data analysis, model building, evaluation, model serialization using Pickle, and deployment using Streamlit.

---

## 📌 Project Overview

Diabetes is a common health condition that can be predicted using various medical indicators.

In this project, Logistic Regression is used to solve a **binary classification problem**, where:

- `0` → Person is unlikely to have diabetes
- `1` → Person is likely to have diabetes

The trained model is saved as a Pickle file and integrated into a Streamlit web application for interactive predictions.

---

## 🎯 Objectives

- Perform exploratory data analysis on the diabetes dataset
- Handle missing or invalid values
- Prepare the dataset for machine learning
- Build a Logistic Regression classification model
- Evaluate model performance
- Save the trained model using Pickle
- Create an interactive Streamlit application
- Generate diabetes predictions from user-provided inputs

---

## 📊 Dataset

The project uses a diabetes dataset containing the following features:

| Feature | Description |
|---|---|
| Pregnancies | Number of pregnancies |
| Glucose | Plasma glucose concentration |
| BloodPressure | Diastolic blood pressure |
| SkinThickness | Skin fold thickness |
| Insulin | Insulin level |
| BMI | Body Mass Index |
| DiabetesPedigreeFunction | Diabetes pedigree function |
| Age | Age of the person |
| Outcome | Target variable |

### Target Variable

`Outcome`

- `0` → No diabetes
- `1` → Diabetes

---

## 🧹 Data Preprocessing

Some values of `0` in the medical features do not represent meaningful measurements.

Therefore, zero values were treated as missing values for:

- Glucose
- BloodPressure
- SkinThickness
- Insulin
- BMI

The missing values were then replaced using the **median** of the respective feature.

---

## 🤖 Machine Learning Model

### Logistic Regression

Logistic Regression was selected because the target variable contains two possible outcomes.

The model was created using:

```python
LogisticRegression(max_iter=1000)
