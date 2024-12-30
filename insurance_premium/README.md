
# Insurance Premium Prediction

The **Insurance Premium Prediction** project aims to develop a machine learning model that predicts insurance premiums (expenses) based on various factors, including demographics, health characteristics, and lifestyle choices of individuals. The goal of this predictive model is to help insurance companies accurately assess the premium for an individual, leading to better pricing strategies, improved customer experience, and more efficient risk management.

### Objective of the Project

The primary objective of this project is to build a robust predictive model capable of accurately estimating insurance premiums based on various individual factors through the use of machine learning techniques.



## Dataset Overview

The dataset used in this project is **insurance.csv** and contains the following columns:

- **age**: Age of the insured individual.
- **sex**: Gender of the insured (male/female).
- **bmi**: Body Mass Index of the insured.
- **children**: Number of children/dependents covered by the insurance.
- **smoker**: Whether the insured is a smoker (yes/no).
- **region**: The region where the insured lives.
- **expenses**: The insurance expenses (target variable) incurred by the insured.



## Project Workflow

## Data Preprocessing

### 1. **Data Cleaning**:
   - **Duplicate Removal**: Checked for duplicate entries and removed them.
   - **Missing Values**: Verified that no missing values were present in the dataset.

### 2. **Data Transformation**:
   - **Log Transformation**: Applied log transformation to the `expenses` column to reduce skewness and stabilize variance.
   - **Categorical Encoding**: Applied one-hot encoding to the categorical variables: `sex`, `smoker`, and `region`.


### 3. **Feature Engineering**:
   - **Feature Scaling**: Scaled numerical features like age, bmi, and children to ensure that all features have the same scale.

## Exploratory Data Analysis (EDA)

### 1. **Univariate Analysis**:
   - Box plots were used to examine the distribution of numerical variables like `age`, `bmi`, and `children`.
   - Count plots were used for categorical variables (`sex`, `smoker`, and `region`) to understand their distribution.

### 2. **Bivariate Analysis**:
   - Scatter plots were used to examine the relationship between the numerical features and the target variable `expenses`.
   - Box plots were used to visualize the distribution of the target variable (`expenses`) across categorical features.

## Modelling

The dataset was split into training and testing sets (80% training, 20% testing). The following models were trained:

- **Linear Regression**: 
  - RMSE: 0.3979
  - R²: 0.8295
- **Decision Tree Regressor**:
  - RMSE: 0.5137
  - R²: 0.7157
- **Random Forest Regressor**:
  - RMSE: 0.3759
  - R²: 0.8477
- **Gradient Boosting Regressor**:
  - RMSE: 0.3264
  - R²: 0.8852

### Best Performing Model:
The **Gradient Boosting Regressor** outperformed all other models with the lowest RMSE (0.3264) and highest R² (0.8852), indicating its performance in predicting insurance expenses.




## Analysis Insights

1. The average age of the individuals in the dataset is approximately 39.22 years, with a range spanning from 18 to 64 years. This indicates a fairly balanced age distribution, encompassing both younger and older adults.

2. The average Body Mass Index (BMI) is approximately 30.67, which falls into the overweight category according to standard BMI classifications. The dataset shows a maximum BMI of 53.1, indicating the presence of individuals with significantly higher BMI values.

3. The average number of children is about 1.1, with most individuals having between 0 to 2 children, and a maximum of 5 children.


4. The dataset has a nearly equal distribution of male (675) and female (662) individuals. T

5. The majority of individuals are non-smokers (1063), while 274 individuals are smokers. 

6. The median expense is around 10,000, indicating the central tendency of the expense values.There are numerous outliers beyond the upper whisker, starting from around 30,000 and extending up to approximately 60,000. These outliers suggest the presence of unusually high expense values in the dataset.
## Requirements

- **Python 3.x**
- **Pandas**
- **NumPy**
- **Matplotlib & Seaborn**
- **Scikit-learn**


## Acknowledgements

The dataset used in this project is available on Kaggle: https://www.kaggle.com/datasets/simranjain17/insurance