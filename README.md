# Phishing-Website-Detection-System
PROJECT OVERVIEW
this project aims to detect phishing websites using machine learning techniques by analyzing URL-based features.  The system classifies whether a website is phishing or legitimate based on multiple security indicators.

OBJECTIVE
To build an automated phishing detectionsystem that can help reduce cyber fraud risks by identifying suspicous website URLs.

DATASET
Phishing Website Dataset collected from kaggle.
Total Samples:11055
30 URL Based-Features
Target Label: Phishing(-1)/Legitimate(1)

METHODOLOGY
1. Data Loading
2. Exploratory Data Analysis(EDA)
3. Data Cleaning(trimming column names and removing unnecessary index column)
4. Feature and Label Separation
5. Train-Test Split(80% Training,20% Testing)
6. Model training and Evaluation

MODELS USED
1. Decision Tree Classifier(Baseline Model)
2. Random Forest Classifier(Improved Ensemble Model)

RESULTS
Decision Tree Accuracy : 95.8%
Random Forest Accuracy : 96.7%
Random Forest showed slightly better performance and improved robustness compared to the Decision Tree baseline .

FUTURE SCOPE
Implementing GUI.
real-time URL phishing detection.
Feature importance visualization.
Model deployment as web applicaton.

TECHNOLOGIES USED
Python
Pandas
Scikit-learn
Git and GitHub

PROJECT STATUS
Model Training Completed
Model Comparison Completed
Further Improvements Planned