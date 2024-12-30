
# Customer Propensity to Purchase

In the banking sector, it is essential to efficiently target potential customers for specific products like term deposits. Traditional marketing methods can be costly and time-consuming, often leading to wasted efforts on customers who are unlikely to convert. By using machine learning models to predict customer behavior, banks can:

- Optimize Marketing Campaigns: Banks can identify high-potential customers who are more likely to subscribe to a term deposit, allowing them to target these customers more effectively with personalized offers and messages.

- Reduce Marketing Costs: By predicting customer behavior, banks can allocate their marketing budget efficiently, reducing spending on low-probability leads and focusing on high-value prospects.

- Increase Customer Retention: Understanding customer preferences and behavior enables banks to tailor products that meet customer needs, strengthen loyalty and increasing the chances of cross-selling other financial products.

#### Objective of the Project
The main objective of this project is to build a predictive model that can accurately classify whether a customer will subscribe to a term deposit or not.

## Dataset

- **age**: Age of the customer.
- **job**: Type of job.
- **marital**: Marital status.
- **education**: Level of education.
- **default**: Whether the customer has credit in default (binary: yes/no).
- **housing**: Whether the customer has a housing loan (binary: yes/no).
- **loan**: Whether the customer has a personal loan (binary: yes/no).
- **contact**: Contact communication type (e.g., cellular, telephone).
- **month**: Last contact month of the year.
- **day_of_week**: Last contact day of the week.
- **duration**: Duration of the last contact (seconds).
- **campaign**: Number of contacts performed during this campaign.
- **poutcome**: Outcome of the previous marketing campaign.
- **subscribe**: Whether the customer subscribed to the term deposit (target variable).


## Project Workflow

### Preprocessing Steps

1. **Handling Missing Values**:
  - Replaced 'unknown' values in categorical columns (`job`, `education`, `marital`, etc.) with `NaN`.
   - Imputed missing values in categorical columns with the mode (most frequent value).
   
2. **Data Transformation**:
  - Encoded categorical features using **one-hot encoding** to convert non-numeric variables into numeric representations.
   - Scaled numerical features using **RobustScaler** to handle outliers and improve model performance.

3. **Target Variable**:
  - Labeled the target feature `subscribe` as the binary classification variable (1 for subscribers, 0 for non-subscribers).

### Exploratory Data Analysis (EDA)

1. **Univariate Analysis**:
  - Visualized the distributions of numerical features (`age`, `duration`, `campaign`) using histograms.
   - Plotted the value counts of categorical features (`job`, `marital`, `education`, `contact`, etc.) using **count plots**.

2. **Bivariate Analysis**:
  - Investigated the relationship between numerical features and the target variable (`subscribe`) using **boxplots** and **scatter plots**.
   - Examined the associations between categorical features and the target using **crosstab analysis** and **chi-square tests**.


### Feature Engineering

1.  **Feature Selection**:
   - Identified relevant features for modeling using **mutual information**.
   - Dropped features with low relevance to the target, such as `duration`.

2. **Class Imbalance Handling**:
   - Used **SMOTE (Synthetic Minority Over-sampling Technique)** to balance the dataset by generating synthetic examples of the minority class.
   - Applied **class weights** in models like Logistic Regression to handle class imbalance.

### Model Building

1. **Model Selection**:
  - Implemented various classification algorithms, including:
     - Logistic Regression
     - Decision Tree
     - Random Forest
     - AdaBoost
     - Gradient Boosting

2. **Training and Validation**:
  - Split the data into training and test sets (80% training, 20% testing).
   - Trained the models using the **training set** and evaluated their performance on the **test set**.

3. **Evaluation Metrics**:
  - Used **recall** as the primary metric due to its importance in minimizing **False Negatives**.
   - Evaluated models using other metrics like **accuracy**, **precision**, **F1-score**, and **ROC-AUC**.

### Model Evaluation

1. **Model Comparison**:
  - Compared model performance based on recall, precision, and F1-score.
   - Logistic Regression and Random Forest performed well, with LogisticRegression slightly outperforming other models in terms of recall.

2. **Feature Importance**:
  - Analyzed the **feature importance** using LogisticRegression to identify the most influential variables.
   - `job`, `education`, and `contact` were the top predictors for customer subscription.

### Results

- **Best Performing Model**: LogisticRegression performed the best in terms of **recall** and **accuracy**, making it the final model for predicting customer subscription.
- **Key Predictors**: `job`, `education`, and `contact` were identified as the most influential features in determining whether a customer subscribes to a term deposit.



## Insights from Analysis 

![image](https://github.com/user-attachments/assets/22809eb6-9aac-48c3-ae83-c26374fc8ba8)

1. **Age Distribution**: Customers range in age from 17 to 98, with a median age of 38. Age does not significantly differ between subscribers and non-subscribers.  
2. **Call Duration**: Longer call durations correlate strongly with higher subscription rates (553 seconds for subscribers vs. 220 seconds for non-subscribers).  
3. **Contact Campaigns**: Subscribers were contacted fewer times on average, suggesting efficient targeting improves outcomes.  
4. **Job Type**: Customers in administrative roles and retirees are more likely to subscribe, while unemployed customers are less likely.  
5. **Marital Status**: Married customers exhibit higher subscription rates, reflecting potential financial planning habits.  
6. **Education**: Customers with university degrees are more likely to subscribe, likely due to financial awareness and stability.  
7. **Communication Channel**: Cellular communication is the most effective, while telephone outreach correlates with lower subscription rates.  
8. **Previous Campaigns**: Customers with no prior marketing outcomes are more responsive to new campaigns.  
9. **Seasonal Trends**: Subscriptions peak in May, followed by August, July, and April.  
10. **Economic Indicators**: High employment variation rates correlate with lower subscription likelihood, suggesting economic uncertainty influences decisions.  



## Requirements
 
- Python 3.x  
- Libraries: pandas, numpy, matplotlib, seaborn, scikit-learn, imbalanced-learn  
