
# Diabetes Prediction 

Diabetes is one of the leading health issues that many individuals face worldwide. Early detection of diabetes is crucial for managing it effectively and preventing its complications. By predicting who might develop diabetes, healthcare providers can intervene in a timely manner, offering lifestyle changes, medications, or other preventive measures.

The Diabetes Prediction project aims to build a predictive model that identifies individuals at risk of developing diabetes based on their health and lifestyle data. The dataset includes various factors such as age, gender, BMI, blood glucose levels, and other lifestyle indicators. By utilizing machine learning algorithms, the project will classify individuals into two categories: diabetic or non-diabetic. This early detection model can enable individuals to take preventive steps before the disease develops, ultimately improving health outcomes and reducing long-term healthcare costs.



## Dataset

The dataset used for this project contains various health-related and demographic attributes of individuals, such as:

- **gender**: Gender of the individual
- **age**: Age of the individual (in years)
- **hypertension**: Whether the individual has hypertension (0 = No, 1 = Yes)
- **heart_disease**: Whether the individual has heart disease (0 = No, 1 = Yes)
- **smoking_history**: Smoking habits of the individual (e.g., never, current, former)
- **bmi**: Body mass index
- **HbA1c_level**: HbA1c (Glycated Hemoglobin) level
- **blood_glucose_level**: Blood glucose level
- **diabetes**: The target variable (0 = No, 1 = Yes)


## Steps in the Project


### 1. **Data Loading and Inspection**
The dataset is loaded from a CSV file into a pandas DataFrame. Initial exploration includes viewing the first few rows, checking for duplicate entries, and inspecting data types and missing values.

### 2. **Data Cleaning**
Duplicates are removed from the dataset and there were no missing values in the dataset.

### 3. **Data Exploration and Visualization**
- Descriptive statistics are generated for numerical attributes.
- Boxplots and distribution plots are created to visualize the spread of numerical variables.
- Count plots are used to visualize the distribution of categorical features and their correlation with the target variable (diabetes).

### 4. **Feature Engineering**
Categorical features (`gender` and `smoking_history`) are encoded using one-hot encoding. This step converts categorical variables into binary columns, allowing the model to interpret them effectively.

### 5. **Data Preprocessing**
- Numerical features are standardized using `StandardScaler` to scale the data to a mean of 0 and a standard deviation of 1. This ensures that all numerical variables are on the same scale for model training.

### 6. **Model Building and Evaluation**
- **Decision Tree Classifier**: A decision tree model is trained to predict diabetes, and performance metrics (accuracy, precision, recall, F1-score) are calculated.
- **Random Forest Classifier**: A random forest model is used to improve accuracy by averaging the results of multiple decision trees.
- **Model Comparison**: The performance of both models is compared based on various evaluation metrics. The final choice of model is based on F1-score.The decision tree model achieves f1-score (71.8%) and random forest model shows an improved f1-score 80%.


## Key Insights

- The majority of the dataset consists of non-diabetic cases (91.2%), indicating a significant class imbalance with only 8.8% diabetic cases.

- The median age of individuals with diabetes is higher than that of non-diabetics. Diabetics tend to be older, with a narrower age range compared to non-diabetics. This suggests a correlation between increasing age and the likelihood of diabetes.

- Individuals with diabetes have higher median BMI values compared to non-diabetics. The variability in BMI is also greater among diabetics, highlighting that higher BMI is a significant risk factor for diabetes.

- Diabetics have significantly higher and more variable HbA1c levels than non-diabetics. The overlap and outliers in HbA1c levels indicate that some non-diabetic individuals have higher HbA1c levels.

- Diabetics exhibit significantly higher median blood glucose levels with outliers.

- Females have a higher count of non-diabetic individuals compared to males.

- Smoking history does not appear to be a strong differentiating factor for diabetes status in this dataset, with non-diabetics significantly outnumbering diabetics across all categories.