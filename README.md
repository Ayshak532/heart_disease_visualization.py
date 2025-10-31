# ❤️ Heart Disease Prediction Using Data Visualization

## 🧠 Project Overview
This project focuses on predicting and understanding heart disease risk factors using data visualization techniques.  
By analyzing clinical, lifestyle, and medical data, the project identifies patterns and correlations that contribute to heart disease.  
The goal is to provide clear visual insights that support early diagnosis and healthcare decision-making.

---

## 📊 Project Workflow

### **1. Data Collection**
- Clinical data: Age, Gender, Blood Pressure, Cholesterol Level  
- Lifestyle factors: Smoking habits, Exercise frequency, Diet  
- Medical history: Diabetes, Previous heart conditions  
- Diagnostic data: ECG and echocardiogram readings  

**Dataset Source:** [Kaggle Heart Disease Dataset](https://www.kaggle.com/)  

---

### **2. Data Preprocessing**
- Handled missing values using the `fillna()` method.  
- Normalized and transformed data for consistency.  
- Checked data summary using:
  ```python
  df.describe()
  df.info()
  df.isnull().sum()
