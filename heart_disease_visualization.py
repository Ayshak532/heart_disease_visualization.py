# HEART DISEASE PREDICTION USING DATA VISUALIZATION
# --------------------------------------------------

# Importing Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Load Dataset
df = pd.read_csv("heart_disease.csv")   # Update path if needed
print(df.head())

# Basic Info
print(df.info())
print(df.describe())

# -------------------------
# Data Preprocessing
# -------------------------

# Fill missing values (Example: Blood Pressure)
df['Blood Pressure'] = df['Blood Pressure'].fillna(df['Blood Pressure'].mean())

# Check for missing values
print(df.isnull().sum())

# -------------------------
# Data Visualization
# -------------------------

# 1. Gender Distribution (Bar Plot)
gender_counts = df['Gender'].value_counts()
mylabels = gender_counts.index

plt.bar(mylabels, gender_counts, color=['lightblue', 'pink'])
plt.xlabel("Gender")
plt.ylabel("Count")
plt.title("Gender Distribution")
plt.show()

# 2. Exercise Habits & Smoking Distribution (Pie Charts)
exercise_habits_count = [3372, 3332, 3271]
smoking_count = [5123, 4852]
exercise_labels = ['High', 'Medium', 'Low']
smoking_labels = ['Yes', 'No']
exercise_colors = ['purple', 'hotpink', 'grey']
smoking_colors = ['red', 'blue']

plt.figure(figsize=(10, 5))

# Exercise Habits Pie Chart
plt.subplot(1, 2, 1)
plt.pie(exercise_habits_count, labels=exercise_labels, colors=exercise_colors,
        startangle=90, autopct='%1.1f%%')
plt.title("Exercise Habits Distribution")
plt.legend()

# Smoking Status Pie Chart
plt.subplot(1, 2, 2)
plt.pie(smoking_count, labels=smoking_labels, colors=smoking_colors,
        startangle=120, autopct='%1.1f%%')
plt.title("Smoking Distribution")
plt.legend()
plt.show()

# 3. KDE Plot (Age & BMI)
sns.kdeplot(df['Age'], color='blue', label='Age', fill=True)
sns.kdeplot(df['BMI'], color='green', label='BMI', fill=True)
plt.xlabel("Value")
plt.ylabel("Density")
plt.title("KDE Plot of Age & BMI")
plt.legend()
plt.show()

# 4. 2D KDE Plot (Blood Pressure vs Cholesterol)
sns.kdeplot(data=df, x='Blood Pressure', y='Cholesterol Level',
            cmap="coolwarm", fill=True)
plt.xlabel("Blood Pressure")
plt.ylabel("Cholesterol Level")
plt.title("Density Plot: Blood Pressure vs Cholesterol Level")
plt.show()

# 5. Boxplot (Triglyceride Level vs Fasting Blood Sugar)
sns.boxplot(data=df[['Triglyceride Level', 'Fasting Blood Sugar']])
plt.xlabel("Variables")
plt.ylabel("Value")
plt.title("Boxplot of Triglyceride & Fasting Blood Sugar")
plt.show()

# 6. Histogram of Sleep Hours
plt.hist(df['Sleep Hours'], bins=10, color='skyblue', edgecolor='hotpink')
plt.xlabel("Sleep Hours")
plt.ylabel("Frequency")
plt.title("Histogram of Sleep Hours")
plt.show()

# 7. KDE Plot of CRP Level & Homocysteine Level
sns.kdeplot(df['CRP Level'], color='blue', label='CRP Level', fill=True)
sns.kdeplot(df['Homocysteine Level'], color='green', label='Homocysteine Level', fill=True)
plt.xlabel("Value")
plt.ylabel("Density")
plt.title("KDE Plot of CRP Level & Homocysteine Level")
plt.legend()
plt.show()

# 8. Pie Chart: Heart Disease Status
heart_disease_count = df['Heart Disease Status'].value_counts()
labels = ["No Heart Disease", "Heart Disease"]
sizes = [heart_disease_count.get('No', 0), heart_disease_count.get('Yes', 0)]
colors = ["skyblue", "red"]

plt.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=90)
plt.title("Proportion of Heart Disease Cases")
plt.legend()
plt.show()

# -------------------------
# Final Observations
# -------------------------
print("Data visualization completed successfully.")
print("Insights can help identify major risk factors of heart disease.")
