
# Census Income Prediction

The Census Income Prediction project aims to predict whether an individual earns more or less than $50,000 annually based on demographic, academic, and socio-economic features. The project uses the Adult Census Income dataset, which contains detailed information such as age, education level, marital status, occupation, and more, to classify individuals into two income categories: "greater than 50K" and "less than or equal to 50K." 


#### Objective of the Project:
The main objective of this project is to build a machine learning model that accurately predicts whether a person earns more or less than $50,000 based on their demographic and socio-economic characteristics.
## Dataset Description

The dataset used in this project is the **Adult Census Income dataset**, which is available in the UCI Machine Learning Repository.

### Columns in the dataset:
1. **age**: Age of the individual (numeric).
2. **workclass**: Type of employment (e.g., Private, Self-emp-not-inc, etc.).
3. **education**: Highest level of education (e.g., Bachelors, Masters, Doctorate).
4. **education-num**: Numeric representation of education level.
5. **marital-status**: Marital status (e.g., Married-civ-spouse, Never-married).
6. **occupation**: Type of occupation (e.g., Tech-support, Craft-repair).
7. **relationship**: Relationship status (e.g., Husband, Not-in-family).
8. **race**: Race (e.g., White, Black, Asian-Pac-Islander).
9. **sex**: Gender (e.g., Male, Female).
10. **hours-per-week**: Average number of hours worked per week.
11. **native-country**: Country of origin.
12. **income**: Target variable, income level (">50K" or "<=50K").


## Preprocessing and Data Cleaning

1. **Data Cleaning**:
- Removed **duplicate rows** from the dataset to ensure the quality of the data.
- Some columns in the dataset contained missing values (represented as "?"), replaced **"?"** values in the dataset with **NaN** to standardize missing data and make it easier to handle.
- The columns **workclass**, **occupation**, and **native-country** had missing values, which were handled by filling them with the **mode (most frequent value)** for each respective column. 

2. **Feature Engineering**:
- Encoded categorical variables (e.g., **workclass**, **education**, **marital-status**, **occupation**, **sex**, **native-country**) using **one-hot encoding**. This converts categorical variables into binary format, making them suitable for machine learning models.
- Converted **income** target variable into binary format (0 for "<=50K" and 1 for ">50K") to prepare it for classification tasks.

3. **Feature Selection**
 - Used Chi2 hypothesis testing and mutual information feature selection techniques to select the variables which have significant association with target variable.

4. **Normalization**:
 - Scaled numerical features using **StandardScaler** to ensure that features with large numerical ranges do not dominate the model.



## Modeling and Evaluation

- Built and compare models like logistic regression, decision tree, random forest, ada boost and gradient boosing and compare the performance using metrics like precision, recall and fi1 score.
- Among the models Random Forest and Gradient Boosting models performed the best, with accuracies of around 86% and 85%, respectively.


## Analysis Insights

![image](https://github.com/user-attachments/assets/7b18199d-e038-4b76-8562-da4e3099e080)

### 1. Age vs. Income
- **Median Age**: Both income groups have a median age around 40 years.
- **Age Range**: Higher income group (>50K) has more outliers at older ages compared to the lower income group (≤50K).

### 2. Work Class vs. Income
- **Private Sector**: Majority of individuals earning ≤50K work in the private sector.
- **Higher Income Representation**: Individuals earning >50K are more represented in the private sector, federal government, and self-employed categories.

### 3. Marital Status vs. Income
- **Married-civ-spouse**: Individuals who are married-civ-spouse are more likely to earn >50K compared to other marital statuses.
- **Never-Married**: Predominantly earn ≤50K.

### 4. Education vs. Income 
- **Higher Education**: Individuals with a Bachelor's, Master's, or Doctorate degree are more likely to earn >50K.
- **Education Level (Num)**: Higher education levels are strongly associated with higher income. The median education num is higher for the >50K income group.

### 5. Occupation vs. Income 
- **High-Income Occupations**: Prof-specialty and Exec-managerial occupations have a higher count of individuals earning >50K.
- **Low-Income Occupations**: Other-service and Adm-clerical occupations have a higher count of individuals earning ≤50K.

### 6. Race vs. Income 
- **White Individuals**: Have the highest count in both income groups.
- **Asian-Pac-Islander**: Have a higher proportion of individuals earning >50K compared to other races.

### 7. Sex vs. Income 
- **Males**: More likely to earn >50K compared to females.
- **Females**: The count of females earning ≤50K is higher than those earning >50K.

### 8. Relationship vs. Income 
- **Husbands**: More likely to earn >50K compared to other relationship categories.
- **Not-in-Family and Unmarried**: Predominantly earn ≤50K.

### 9. Hours per Week vs. Income 
- **Higher Hours**: Individuals earning >50K tend to work more hours per week. The median hours per week is higher for the >50K income group.

### 10. Income Distribution

- Majority with Lower Income: 75.9% of individuals have an income of less than or equal to 50K. This indicates that the majority of the population falls within this lower income bracket.

- Minority with Higher Income: 24.1% of individuals have an income of more than 50K. This shows that a smaller portion of the population earns a higher income, highlighting a significant income disparity.
## Acknowledgments

The dataset used in this project is the Adult Census Income dataset from the UCI Machine Learning Repository. The dataset can be accessed at https://archive.ics.uci.edu/dataset/2/adult
