# heart_disease_visualization.py
HEART DISEASE PREDICTION
PROJECT TITLE: HEART DISEASE PREDICTION USING DATA VISUALIZATION 
SYNOPSIS
Heart disease prediction using data science involves analyzing medical data to identify patterns and risk factors that contribute to heart disease. Statistical methods and visualization methods used to develop predictive models. Here’s how the process works:
1.	DATA COLLECTION
●	Clinical data (age, gender, cholesterol level, blood pressure, etc.)
●	Lifestyle factors (smoking, exercise, diet)
●	Medical history (diabetes, previous heart conditions)
●	Electrocardiogram (ECG) and echocardiogram data
 
2.	DATA PREPROCESSING
●	Handling missing values
●	Data normalization and transformation
3.	EXPLORATORY DATA ANALYSIS (EDA)
●	Distribution analysis of attributes
●	Correlation heatmaps to identify relationships between factors
●	Box plots, histograms and scatter plots for data trends
4.	DATA VISUALIZATION TECHNIQUES
●	Pie charts for categorical distributions
●	Line and bar graphs for trend analysis
●	Pair plots for multivariate analysis
5.	TOOLS & TECHNOLOGIES
●	Programming language: Python
●	Libraries: Pandas, NumPy, Matplotlib
●	Frameworks: Jupyter notebook
6.	EXPECTED OUTCOME
●	Graphical representation of key risk factors for heart disease
●	Interactive dashboards for better understanding of heart disease patterns

CONCULSION
             This project demonstrateAs how data science and visualization helps to understand the risk factors of patients in health care domain. The insights for this model can help health care professionals to take proactive steps to analyze the patient’s outcomes for better understanding. It shows the proper layouts of the patients health status to improve the outcomes.



Project title:
          HEART DISEASE PREDICTION USING DATA VISUALIZATION    
STUDY OF DATASETS USING VISUALIZATION 
Data sourcing:
●	Get the datasets from the Kaggle website.
 IMPORTING LIBRARIES 
●	Importing libraries is the first step to start the programming.
●	In the project, I used libraries like pandas, numpy, SciPy, matplotlib and seaborn for advanced visualization.
●	I imported warnings for Suppress unnecessary alerts.
Read a CSV file using pandas:
                     df=pd. read_csv("C:/Users/Hp/Downloads/kirthi.txt/heart_disease.csv")
●	This is my command to read the csv file. I imported the file in df to use in the program.
●	df. Describe () is used in program. It provides summary statistics for the numerical columns in your dataset.
Summary statistics:
▪	Count → Number of non-missing values in each column
▪	Mean → Average value
▪	Std → Standard deviation (spread of data)
▪	Min → Minimum value
▪	25% → 1st quartile (Q1) - 25% of data is below this value
▪	50% → Median (Q2) - Middle value
▪	75% → 3rd quartile (Q3) - 75% of data is below this value
▪	Max → Maximum value
▪	df. Info () It provides a summary of the dataset, including:
▪	 Number of rows and columns
▪	 Column names and data types
▪	 Number of non-null (non-missing) values
Data preprocessing:
●	Handling missing values
●	Data normalization and transformation
       

Using fillna() to filling the missing values:
●	When missing values are few and replacing them with the mean won’t distort the data.
●	When the variable is normally distributed (not skewed).
            Df ['Blood Pressure'] = df ['Blood Pressure']. fillna (df ['Blood Pressure']. Mean ())
▪	I used this code to fill the missing values in blood pressure. This is the process to fill the no skewner or normal distribution with mean value.

●	df. isnull ().sum()
▪	It counts the number of missing (NaN) values in each column of your dataset.
visualizing the dataset for better understanding the risk factor of the patient
Source code:
               gender_counts = df['Gender'].value_counts ()
mylabels = gender_counts. index
plt. bar (mylabels, gender_counts, color = ['lightblue', 'pink'])
plt. xlabel ("Gender")
plt. ylabel ("Count")
plt. title ("Gender Distribution")
Bar plot for gender distribution:
●	The x-axis represents genders (Male, Female).
●	The y-axis represents counts (for Male, for Female).
●	This code counts gender occurrences and plots a bar chart.
●	Colors (light blue & pink) distinguish categories.
●	plt. bar () is used to visualize the gender distribution.
 PIE CHART
A pie chart is a circular statistical graphic that divides data into proportional slices to represent percentage distributions of different categories. Each slice's size corresponds to the proportion of that category in the dataset.
                  Create two pie charts side by side:
▪	Exercise Habits Distribution
▪	Smoking Distribution
Interpreting the Output
           First Pie Chart (Exercise Habits Distribution)
●	Shows the percentage of people in High, Medium, and Low exercise groups.
●	Purple, Hotpink and Grey distinguish different levels.
●	The slices are proportional to the count values.
Second Pie Chart (Smoking Distribution)
●	Displays the proportion of Smokers (Yes) and Non-Smokers (No).
●	Red (Yes) vs. Blue (No) highlights the division.
●	The percentage is displayed on each slice.
Source code:
Exercise_ habits_ count = [3372, 3332, 3271]
Smoking_ count = [5123,4852]
exercise_ labels = ['High', 'Medium', 'Low']
smoking_ labels = ['Yes', 'No']
exercise_ colors = ['purple', 'hotpink', 'grey']
smoking _ colors = ['red', 'blue']
# first plot to display the exercise habit distribution
plt. subplot (1,2,1)
plt. pie (Exercise_ habits_ count, labels=exercise_ labels, colors= exercise_ colors, startangle = 90, autopct='%1.1f%%')
plt. title ("Exercise Habits Distribution")
plt. legend ()
# second plot to display the smoking distribution
plt. subplot (1,2,2)
plt. pie (Smoking_ count, labels=smoking_ labels, colors=smoking_ colors, startangle=120, autopct='%1.1f%%')
plt. title ("Smoking Distribution")
plt. legend ()
plt. show ()
KDE (Kernel Density Estimate) plot  for plotting Age and BMI:
              A KDE (Kernel Density Estimate) plot is used to visualize the probability density function (PDF) of a continuous variable.
●	It smooths the distribution of data points to create a continuous curve.
●	Similar to a histogram, but without discrete bins instead, it uses a Gaussian kernel to estimate density.
●	The area under the curve represents the distribution of data points
    Source code:
                 sns. Kdeplot (df['Age'], color='blue', label='Age', fill=True)
                 sns. Kdeplot (df['BMI'], color='green', label='BMI', fill=True)
                 plt. xlabel ("Value")
                 plt. ylabel ("Density")
                 plt. title ("KDE Plot of Age & BMI")
                 plt. legend ()
                 plt. show ()
Explanation of KDE plot:
KDE Plot	Smooth curve estimating the density distribution of Age & BMI.

X-axis	Represents values of Age & BMI.

Y-axis	Represents density (relative frequency) of data.

Color Coding	Blue (Age), Green (BMI) for easy comparison.

Peaks in KDE	Indicate common values where data is concentrated.

Skewness	Determines symmetry of distribution.

Goal of This KDE Plot:
●	Compare the distributions of Age and BMI in the dataset.
●	Identify where data points are concentrated (high density) and sparse (low density).
●	Observe trends and patterns in these two health-related features.
KDE Plot Explanation for age and BMI data distribution:
●	The x-axis represents the numerical values of Age and BMI.
●	The y-axis represents the density, meaning how frequent (probabilistically) certain values are.
●	The blue curve represents the distribution of Age.
●	The green curve represents the distribution of BMI.
●	Higher peaks indicate that more values fall around that range.
●	The KDE plot smooths the histogram using a probability density function, making it useful for understanding the data distribution.
●	If the Age curve has a single peak, Age data is unimodal (single dominant age group).
●	If the BMI curve is spread out, BMI values have high variance.
●	Overlapping areas show that Age and BMI might share similar distributions.


Understanding KDE (Kernel Density Estimate) for 2D Data
A KDE (Kernel Density Estimate) plot is used to visualize the distribution of two continuous variables in a dataset. Unlike 1D KDE plots that show one variable's density, this 2D KDE plot helps us analyse how Blood Pressure (x-axis) and Cholesterol Level (y-axis) are distributed together.
TO UNDERSTANDS THE KDE PLOT 2D USING THIS KEYPOINTS:
      THE KDE PLOT 2D using this key points will helps you to understands the distribution,
●	Darker blue areas → Very few data points in that region.
●	Lighter blue areas → Slightly more data points.
●	Orange-red areas → Moderate density.
●	Bright red areas → Most data points are clustered here (highest density).
Source code:
             sns. Kdeplot (data=df, x='Blood Pressure', y='Cholesterol Level', cmap = "coolwarm", fill=True)
             #blue for low density, red for high density
             plt. xlabel ("Blood Pressure")
             plt. ylabel ("Cholesterol Level")
             plt. title ("Density Plot: Blood Pressure vs. Cholesterol Level")
             plt. show ()

Key Observations from the KDE Plot
1️⃣ High-Density Cluster (Red/Orange Areas)
●	These regions indicate the most common Blood Pressure and Cholesterol Level values in the dataset.
●	If the high-density area is centered, it means most people have a Blood Pressure of ~120 and Cholesterol Level of ~200.
2️⃣ Low-Density Areas (Blue Regions)
●	Represent uncommon Blood Pressure & Cholesterol values.
●	If an area is deep blue, very few individuals fall within that range.
3️⃣ Shape of the Distribution
●	If the plot is narrow and tall, it means most people have similar Blood Pressure values but vary in Cholesterol Levels.
●	If the plot is wide, it means Blood Pressure values are spread out over a wider range.
●	If it is diagonal, it suggests a correlation between the two variables (higher BP → higher Cholesterol).

Final Explanation of the Output
●	The KDE plot will show a contour-like heatmap of the density of data points.
●	Red areas indicate regions where Blood Pressure and Cholesterol Levels have a high concentration of data points.
●	Blue areas indicate regions with low density of data points.
●	This helps visualize the relationship between Blood Pressure and Cholesterol Levels.
Boxplot visualization:
          A boxplot (also called a box-and-whisker plot) is a standardized way of visualizing the distribution of a dataset based on five key statistical values:
●	Minimum (Lower Whisker) → The smallest value, excluding outliers.
●	First Quartile (Q1 - 25th percentile) → The median of the lower half of the data.
●	Median (Q2 - 50th percentile) → The middle value of the dataset.
●	Third Quartile (Q3 - 75th percentile) → The median of the upper half of the data.
●	Maximum (Upper Whisker) → The largest value, excluding outliers.
Source code:
                             sns. Boxplot (data=df [['Triglyceride Level', 'Fasting Blood Sugar']])
                              plt. xlabel ("Variables")
                              plt. ylabel ("Value")
                              plt. title ("Boxplot of Triglyceride & Fasting Blood Sugar ")
                              plt. show ()
 Interpreting the Distribution
1️ the Box is Wide
●	The variable has high variability (data is spread out).
●	Large variation in Triglyceride Levels or Fasting Blood Sugar.

2️ the Box is Narrow
●	The data is closely packed, indicating low variability.
●	Most values are similar
.
3️  the Median Line is Centered
●	 the median is not closer to Q1 → The data is zero-skewed (similar values more common).
●	If the median is not closer to Q3 → The data is zero-skewed (similar values more common).

4️⃣ If There Are Many Outliers
●	Several dots outside the whiskers → Suggests that some individuals have very high or low values of Triglyceride or Fasting Blood Sugar.

________________________________________

 Triglyceride Skewness (0.0057)

●	Very slightly positive (right-skewed), but almost negligible.
●	The upper and lower whiskers in the boxplot should be nearly the same length.
Fasting Blood Sugar Skewness (-0.0089)
●	Very slightly negative (left-skewed), but also negligible.
●	Again, the boxplot should show almost equal whiskers.
Expected Boxplot Characteristics
●	Balanced whiskers (upper and lower whiskers are similar in length).
●	The median is likely near the center of the box.
●	No extreme outliers that would cause heavy skewing.
HISTOGRAM WITH KDE       
         Source code:
                  plt. hist (df ['Sleep Hours'], bins=10, color='skyblue', edgecolor='hotpink')
                  plt. xlabel ("Sleep Hours")
                  plt. ylabel ("Frequency")
                  plt. title ("Histogram of Sleep Hours")
                  plt. show ()
         X-Axis (Sleep Hours)
o	The X-axis represents different ranges (bins) of Sleep Hours.
o	If bins=10, it divides Sleep Hours into 10 equal intervals.
●	Example:
o	If Sleep Hours range from 4 to 10 hours, bins could be:
▪	4-4.6 hours, 4.6-5.2 hours, ..., 9.4-10 hours.
________________________________________
 Y-Axis (Frequency)
●	The Y-axis represents how many people fall within each Sleep Hour range.
●	Taller bars = more people sleeping that many hours.
●	Shorter bars = fewer people in that sleep range.
Interpretation of Skewness = 0.00017
●	Since 0.00017 ≈ 0, the distribution is nearly symmetric.
●	There is no significant skew to the right or left.
●	The histogram should look bell-shaped, similar to a normal distribution.
●	The boxplot whiskers will likely be balanced (equal upper and lower whiskers).
Histogram with KDE Curve
●	The histogram should have a peak around the mean sleep hours.
●	There won’t be a long tail on either side.
●	The KDE curve should look symmetrical.
Kernel Density Estimation (KDE) Plot Explanation
●	A KDE plot is a smooth estimate of a variable's probability density function (PDF). It helps visualize the shape and distribution of continuous data.
Source code:
           sns. Kdeplot (df ['CRP Level'], color='blue', label='CRP Level', fill=True)
                 sns. Kdeplot (df ['Homocysteine Level'], color='green', label='Homocysteine Level', fill=True)
                 plt. xlabel ("Value")
                 plt. ylabel ("Density")
                 plt. title ("KDE Plot of CRP Level & Homocysteine Level")
                 plt. legend ()
                 plt. show ()
Output:
●	A KDE plot with two curves:
o	Blue curve: Represents the distribution of CRP Level.
o	Green curve: Represents the distribution of Homocysteine Level.
●	The x-axis represents the values of both variables.
●	The y-axis represents the estimated density.
●	The legend differentiates the two distributions.

This KDE plot is useful when:
●	Comparing the distribution of two numerical variables.
●	Identifying overlapping regions and differences between the two distributions.
●	Understanding the spread and peaks in the data.

Using the pie chart to visualizing the status of heart disease: 
               This pie chart visualizes the proportion of people with and without heart disease in your dataset.
          We have the count value, using this code:
                 heart_ disease_ count=df['Heart Disease Status'].value_counts()
output:
                Heart Disease Status
                              No     8000
                              Yes    2000
                               Name: count, dtype: int64
         After, we code the program to analyse the heart disease rate:
        Source code:  
                  labels = ["No Heart Disease", "Heart Disease"]
                  sizes = [8000, 2000]  
                  colors = ["skyblue", "red"]
                  plt. pie (sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=90)
                  plt. title ("Proportion of Heart Disease Cases")
                  plt. legend ()
                  plt. show ()
●	80.0% (No Heart Disease) – Blue
●	 20.0% (Heart Disease) – Red
●	 The chart will clearly show that most people do not have heart disease but 20% do.

RESULTS & CONCLUSION
The final model helps in predicting heart disease based on key factors. Insights derived from data visualization assist healthcare professionals in understanding risk patterns and making informed decisions for early diagnosis and prevention.
This project demonstrates that data visualization is a powerful tool for understanding heart disease risk factors. By analysing trends in medical and lifestyle data, we can highlight key indicators that contribute to heart disease. These insights can assist doctors and researchers in early detection and prevention strategies.
 Future Work: Implement machine learning models to predict heart disease risk with higher accuracy.


