
# Employee Retention Prediction

Employee retention is a critical factor for organizations, as high turnover can result in increased recruitment costs and loss of talent. By predicting employee attrition, companies can take proactive steps to address the underlying causes of turnover, improve employee satisfaction, and reduce operational disruptions. 

The Employee Retention Prediction project is focused on predicting whether an employee will leave or stay at an organization based on various demographic, professional, and socio-economic features.The primary objective of this project is to build a predictive model that can accurately forecast whether an employee will leave the organization (attrition) or stay. This model will help HR and management teams to:

- Identify at-risk employees who might leave soon.
- Take proactive measures to increase employee satisfaction and retention.
- Optimize recruitment strategies by focusing on retention rather than constantly hiring new employees.


## Data Description

1. **Education** : Represents the highest level of education attained by the employee.

2. **JoiningYear** : The year in which the employee joined the company.
 

3. **City** : The city where the employee is located or works.
   

4. **PaymentTier** : Represents the payment or salary tier assigned to the employee.
 

5. **Age** : The age of the employee.

6. **Gender** : The gender of the employee.

7. **EverBenched** : Indicates whether the employee has ever been on a "bench," meaning a period of time when they were not actively assigned to a project or task.

8. **ExperienceInCurrentDomain** : The number of years the employee has worked in their current professional domain.

9. **LeaveOrNot** : Target variable representing whether the employee has left the company or not.


## Project Workflow

### 1. Data Loading and Exploration
- **Loading Data**: The data is loaded from a CSV file named `Employee.csv`.
- **Initial Exploration**: Basic data inspection is performed using `head()`, `shape()`, and `info()` functions to understand the structure of the dataset.
- **Handling Missing Values**: No missing values are found in the dataset after cleaning.
- **Removing Duplicates**: Duplicate entries are dropped, ensuring the data used for modeling is unique.

### 2. Data Preprocessing
- **Numerical vs. Categorical Data**: The dataset is split into numerical and categorical columns.
- **Visualization**: Boxplots are used to visualize the distribution of numerical variables, and countplots for categorical data to examine the frequency of each category.
- **Feature Engineering**: Categorical features are one-hot encoded to convert them into binary dummy variables.
- **Scaling**: Numerical features are standardized using `StandardScaler` to ensure that the features are on the same scale.

### 3. Train-Test Split
- **Splitting Data**: The dataset is split into training and testing sets (80% training, 20% testing), ensuring that the target variable is stratified to maintain class distribution.

### 4. Model Training
Four different machine learning models are trained to predict employee retention:

  - **Logistic Regression**
  - **Decision Tree Classifier**
  - **Random Forest Classifier**
  - **Gradient Boosting Classifier**

### 5. Model Evaluation
- **Metrics Used**: Accuracy, Precision, Recall, F1-Score, and confusion matrix are used to evaluate the performance of each model.
- **Comparison**: The models are compared based on their performance on the testing data.

### 6. Feature Importance
- **Gradient Boosting Model**: Feature importance is derived using the `feature_importances_` attribute of the Gradient Boosting model. A bar chart is plotted to visualize the relative importance of each feature in predicting employee retention.





## Key Insights from Employee Retention

- The median joining year is 2015, with 25% of employees joining before 2013 and 25% joining after 2017.

- The average payment tier is approximately 2.64, indicating that most employees are in the mid to upper tiers of the payment structure.

- The median age is 30 years, with 25% of employees younger than 27 and 25% older than 35.

- The median experience is 2 years, with 25% of employees having 1 year or less experience and 25% having 4 or more years of experience.

- Bachelor's degree holders high in the dataset, followed by those with Master's degrees and a smaller group with PhDs.

- Bangalore is the leading location for employees, followed by Pune and New Delhi.

- The workforce has a higher count of male employees, with a significant number of female employees as well.

- Most employees have not been benched, indicating strong engagement and utilization in their roles.

- The majority of employees (1676) have stayed with the company, while a smaller but notable portion (1088) have left. This indicates that while the company retains most of its employees, there are still opportunities to improve retention strategies.

- Employees who stayed with the company have a slightly higher median age compared to those who left. This suggests that older employees may have a higher tendency to stay with the company.

- Employees who left the company have a slightly higher median experience of around 3 years in their current domain.

- The majority of employees who have never been benched have stayed with the company.

- Joining year, payment tier, and city (Pune) are the top three factors influencing employee retention.
## Requirements


- Python 3.x
- Libraries: 
  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `scikit-learn`
  - `numpy`