Heart Disease Prediction

This project utilizes machine learning techniques to predict the likelihood of heart disease based on various health metrics and patient data. By analyzing patterns in historical data, the model aims to assist in early diagnosis and aid healthcare professionals in decision-making.

Features

Exploratory Data Analysis (EDA):
Gain insights into the dataset, including the distribution of features and correlations.
Data Preprocessing:
Handle missing data, encode categorical features, and scale numerical variables.
Model Training and Evaluation:
Train multiple machine learning models and evaluate their performance using appropriate metrics.
Feature Importance Analysis:
Identify key health indicators contributing to heart disease risk.
Technologies Used

Programming Language: Python 3
Libraries and Frameworks:
Pandas, NumPy: Data analysis and preprocessing
Matplotlib, Seaborn: Data visualization
Scikit-learn: Machine learning model implementation and evaluation
Dataset

The dataset includes patient health records with the following attributes:

Age
Sex
Chest pain type
Resting blood pressure
Cholesterol level
Fasting blood sugar
Resting ECG results
Maximum heart rate achieved
Exercise-induced angina
Oldpeak (ST depression induced by exercise)
Slope of the peak exercise ST segment
Number of major vessels colored by fluoroscopy
Thalassemia (thal)
The target variable indicates the presence or absence of heart disease.

How to Use

Clone the Repository
git clone https://github.com/pranavprasad7/Heart-Disease-Prediction.git
cd Heart-Disease-Prediction
Install Dependencies
Ensure you have Python 3 installed, then install the required libraries:
pip install -r requirements.txt
Run the Project
Execute the main script to preprocess data, train models, and evaluate results:
python main.py
Analyze Outputs
Visualize model performance and feature importance using the provided graphs and metrics.

Project Structure

data/ - Contains the dataset(s) used for the project
notebooks/ - Jupyter notebooks for EDA and initial experimentation
src/ - Core Python scripts for preprocessing, modeling, and evaluation
requirements.txt - List of dependencies
README.md - Project overview and instructions

Models Implemented

Logistic Regression
Decision Trees
Random Forest
Support Vector Machines (SVM)
K-Nearest Neighbors (KNN)
