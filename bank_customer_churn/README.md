
# Bank Customer Churn

Predicting customer churn is a critical task for banks aiming to retain their valuable customers and maintain steady revenue streams. Customer churn refers to the rate at which customers stop doing business with an entity. In the banking domain, churned customers might close their accounts or stop using services. Identifying churn early enables banks to take corrective actions, such as offering personalized services or better rates, to retain customers.

In the banking sector, understanding and predicting churn is crucial for retaining valuable customers and reducing revenue losses.

This project analyzes historical customer data to uncover the key factors behind customer churn and develops predictive models that enable banks to take proactive measures to enhance customer retention.

## Tools and Technologies

To implement the Bank Churn Prediction project, the following tools and technologies were used:

- Python: The primary programming language used for data analysis, visualization, and machine learning.
- Jupyter Notebook: Used for interactive coding, data analysis, and visualization.
- Pandas: For data manipulation and analysis (handling the dataset).
- Matplotlib & Seaborn: For visualizations (exploratory data analysis).
- Scikit-learn: For implementing machine learning algorithms and model evaluation.
- Pickle: For saving and loading the trained models.
## Methods and Steps Followed
The following steps were followed to implement the project:

1. Data Collection and Preprocessing

- Imported the dataset and performed necessary data cleaning, including handling missing values, encoding categorical variables, and scaling numerical features.
2. Exploratory Data Analysis (EDA)

- Conducted thorough analysis to understand the data distribution, correlations, and visual patterns.
- Identified key trends, outliers, and insights from the data.
3. Feature Engineering

- Selected relevant features and transformed the data (e.g., encoding categorical variables like 'Geography' and 'Gender' and scaling continuous variables).
4. Model Building

- Split the data into training and test sets (80-20 split).
- Implemented machine learning models using Scikit-learn.
5. Model Evaluation

- Evaluated models using performance metrics such as accuracy, precision, recall, F1-score, and ROC-AUC.
- Compared the models to select the best performing one.
## Findings from Data Analysis

- Data Imbalance: Approximately 80% of customers stayed, while 20% churned. This imbalance was addressed using class weights.
- Correlation Insights: Features like CreditScore, Balance, and Age were highly correlated with customer churn. A higher credit score and balance appeared to decrease the likelihood of churn.
- Gender and Geography: The churn rate was slightly higher for male customers compared to females, and churn varied across different geographical locations.

![screenshot1](https://github.com/user-attachments/assets/c8d75e2b-5f72-40fd-a004-3b203a643b14)
![screenshot2](https://github.com/user-attachments/assets/59a1b5e4-81a4-4961-817c-0a84e7fb6eca)

## Model Performance

Based on the evaluation results, logistic regression with class weights was best performing model with 70% recall.
## Acknowledgements

 - Dataset: https://www.kaggle.com/datasets/radheshyamkollipara/bank-customer-churn
 
 - Libraries Used: Python libraries such as pandas, numpy, matplotlib, seaborn, and scikit-learn for efficient data analysis and modeling.

