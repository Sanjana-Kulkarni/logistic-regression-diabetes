# Logistic Regression – Interview Answers

## 1. What is Logistic Regression?

Logistic Regression is a supervised machine learning algorithm mainly used for classification problems. It predicts the probability of an outcome and then classifies it into a category.

In this project, I used Logistic Regression to predict whether a person is likely to have diabetes or not.

---

## 2. Why did you use Logistic Regression for this project?

I used Logistic Regression because the target variable, `Outcome`, has two possible values: 0 and 1.

So, it is a binary classification problem, which makes Logistic Regression a suitable model for this dataset.

---

## 3. What is the difference between Linear Regression and Logistic Regression?

Linear Regression is mainly used to predict continuous numerical values, such as salary or house price.

Logistic Regression is used for classification. It gives a probability between 0 and 1 and uses that probability to classify the data into categories.

---

## 4. What is the sigmoid function?

The sigmoid function converts the model's output into a value between 0 and 1.

This value can be interpreted as the probability of the positive class.

For example, if the predicted probability is 0.80, it means the model estimates an 80% probability of the person belonging to class 1.

---

## 5. What dataset did you use?

I used the diabetes dataset for this project.

The target variable is `Outcome`, and the input features include Pregnancies, Glucose, Blood Pressure, Skin Thickness, Insulin, BMI, Diabetes Pedigree Function, and Age.

---

## 6. How did you handle missing values?

In the dataset, some medical features contain zero values that are not meaningful measurements.

I treated zero values as missing values for Glucose, Blood Pressure, Skin Thickness, Insulin, and BMI.

I then replaced those missing values using the median of the respective columns.

---

## 7. Why did you use median instead of mean?

I used the median because medical datasets can contain extreme values or outliers.

The median is less affected by extreme values, so it can provide a more reliable replacement for missing values in this case.

---

## 8. How did you split the data?

I divided the dataset into training and testing data using an 80:20 split.

The model was trained on the training data and then evaluated on the test data.

I also used `random_state=42` so that the split remains consistent whenever I run the code again.

---

## 9. What is the purpose of `max_iter=1000`?

`max_iter` specifies the maximum number of iterations the Logistic Regression algorithm can take while finding the best model parameters.

I used `max_iter=1000` to give the model enough iterations to converge properly.

---

## 10. How did you evaluate your model?

I evaluated the model using classification performance measures such as accuracy, precision, recall, F1-score, and the confusion matrix.

These metrics help understand how well the model is performing instead of depending only on accuracy.

---

## 11. What is a confusion matrix?

A confusion matrix shows the number of correct and incorrect predictions made by a classification model.

It contains four important values:

- True Positive
- True Negative
- False Positive
- False Negative

These values help us understand the types of mistakes made by the model.

---

## 12. What is precision?

Precision tells us, out of all the cases predicted as positive, how many were actually positive.

For this project, it helps us understand how reliable the model's positive diabetes predictions are.

---

## 13. What is recall?

Recall tells us, out of all the actual positive cases, how many were correctly identified by the model.

For a medical prediction problem like diabetes, recall can be particularly important because missing an actual positive case can be significant.

---

## 14. What is F1-score?

F1-score is the harmonic mean of precision and recall.

It is useful when we want a balance between precision and recall rather than focusing on only one metric.

---

## 15. How did you deploy the model?

After training the Logistic Regression model, I saved it as a pickle file named `logistic_regression_model.pkl`.

I then created an `app.py` file using Streamlit.

The application takes the patient's input details, loads the trained model, and displays the prediction along with the probability of diabetes.

---

## 16. Why did you use pickle?

I used pickle to save the trained machine learning model.

This allows me to load the already-trained model later without training it again every time the application runs.

---

## 17. What is Streamlit?

Streamlit is a Python framework that makes it easy to create simple interactive web applications for data science and machine learning projects.

I used it to create the user interface for my diabetes prediction model.

---

## 18. What happens when a user clicks the Predict button?

When the user enters the required patient details and clicks the Predict button, the application creates the input data in the required format.

The saved Logistic Regression model then makes the prediction and calculates the probability.

Finally, the application displays whether the patient is predicted to have diabetes or not.

---

## 19. What did you learn from this project?

Through this project, I learned how to take a classification problem from data preprocessing and exploratory analysis to model building and evaluation.

I also learned how to save a trained model using pickle and create a simple Streamlit application to deploy it.

---

## 20. If you had more time, what would you improve?

If I had more time, I would try different classification algorithms and compare their performance.

I would also focus more on feature scaling, hyperparameter tuning, cross-validation, and improving the deployment interface.
