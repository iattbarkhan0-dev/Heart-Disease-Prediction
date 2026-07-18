# ❤️ Heart Disease Prediction using XGBoost

## 📌 Project Overview

This project is a **Machine Learning-based Heart Disease Prediction System** developed using the **XGBoost Classifier** algorithm. The application predicts whether a patient is likely to have heart disease based on several medical attributes.

The model is deployed using **Streamlit**, providing a simple and interactive web interface where users can enter patient information and receive an instant prediction.
LINK OF HEART DISEASE APP.
https://heart-disease-predictiongit-jsrvfkayey5c5kjdmtxr59.streamlit.app/
---

## 🚀 Features

* Predicts the presence of heart disease.
* User-friendly Streamlit web application.
* Built using the powerful XGBoost Classifier.
* Fast and accurate predictions.
* Easy to deploy on Streamlit Community Cloud.

---

## 🛠️ Technologies Used

* Python
* Streamlit
* NumPy
* Pandas
* Scikit-learn
* XGBoost

---

## 📂 Project Structure

```
Heart_Disease_Prediction/
│── app.py
│── Heart_Disease_model.json
│── requirements.txt
│── README.md
```

---

## 📊 Dataset Features

The model uses the following input features:

* Age
* Sex
* Chest Pain Type (cp)
* Resting Blood Pressure (trestbps)
* Cholesterol (chol)
* Fasting Blood Sugar (fbs)
* Resting ECG (restecg)
* Maximum Heart Rate (thalach)
* Exercise Induced Angina (exang)
* Oldpeak
* Slope
* Number of Major Vessels (ca)
* Thal

---

## 🤖 Machine Learning Model

* Algorithm: **XGBoost Classifier**
* Problem Type: Binary Classification
* Target Variable:

  * 0 → No Heart Disease
  * 1 → Heart Disease

---

## 📈 Model Evaluation

The model was evaluated using the following performance metrics:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix
* Classification Report

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Heart_Disease_Prediction.git
```

Move into the project directory:

```bash
cd Heart_Disease_Prediction
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## 💻 How to Use

1. Open the Streamlit application.
2. Enter the patient's medical information.
3. Click the **Predict** button.
4. View the prediction result instantly.

---

## 📌 Future Improvements

* Hyperparameter tuning for improved performance.
* Model comparison with Random Forest, LightGBM, and CatBoost.
* Probability score for predictions.
* Data visualization dashboard.
* Docker deployment.
* Cloud deployment on AWS, Azure, or Google Cloud.

---

## 👨‍💻 Author

**Iattbar Khan**

Machine Learning Enthusiast | Python Developer | Streamlit Developer

---

## ⭐ Support

If you found this project helpful, please consider giving the repository a **Star ⭐** on GitHub.
