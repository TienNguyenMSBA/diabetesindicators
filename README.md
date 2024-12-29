**Machine Learning for Diabetes Risk Prediction and Insights**

This project leverages the CDC Diabetes Health Indicators dataset to develop machine learning models for predicting diabetes risk and gaining insights into key health factors. The project involves:

- Predictive Modeling: Building a classification model to predict the likelihood of diabetes based on health indicators, with a focus on optimizing performance using algorithms like logistic regression, decision tree, random forest, and XGBoost.
- Feature Importance Analysis: Identifying the most influential health indicators contributing to diabetes risk using feature selection techniques.
- Anomaly Detection: Detecting unusual health profiles that may signal potential outliers or unique cases using Isolation Forest.
- Risk Score Development: Designing a scoring system to classify individuals into low, medium, and high-risk categories, enabling actionable insights for public health strategies.

- The project emphasizes a data-driven approach to understanding and addressing diabetes prevalence through machine learning.

Before running the code, please ensure you have the necessary libraries installed by running the following command:

```bash 
pip install pandas certifi
pip install ucimlrep
``` 

The main code file is `diabetes_risk_prediction.ipynb`, which contains the implementation of the machine learning models and analysis. The dataset used in this project is publicly available from the UCI Machine Learning Repository. This dataset is skewed with more observations in the non-diabetic than diabetic, so I have under-sampled the majority class to balance the dataset for training the models. The dataset has not null values, so no imputation is required. However, there are some features that needed to be converted to dummy variables (eg, GenHealth, Age, Education, Income) because the orginal dataset has categorical variables. 

I have written an article on this project, which you can find on my Medium
