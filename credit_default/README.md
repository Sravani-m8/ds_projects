
# Credit Card Default Prediction

Credit card companies and financial institutions face significant challenges in assessing the creditworthiness of their clients. A credit default can lead to financial losses and affect the overall stability of the institution. Early identification of customers at risk of default can help mitigate these risks by allowing institutions to take preventive actions. By utilizing predictive models, banks can improve their decision-making process and reduce the occurrence of defaults.

This predictive model assists credit card companies in identifying customers who are more likely to default on their payments in the future. By accurately predicting potential defaults, the company can take timely actions to reduce the risk of non-payment and enhance customer management. This will ultimately improve financial stability and customer satisfaction while minimizing losses.

#### Objective of the Project:
The primary objective of this project is to build a machine learning model that accurately predicts whether a client will default on their credit card payment based on various demographic, financial, and behavioral features.

## Data Description

The dataset used for this project is the **Credit Default Dataset**, which contains information about credit card clients, including demographic, financial, and behavioral features. Each row represents a credit card customer, and the columns provide details about the client’s personal information, payment history, and financial behavior.

The dataset is structured as follows:

| Column Name          | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| **ID**               | Unique identifier for each customer. |
| **SEX**              | Gender of the customer                                 |
| **EDUCATION**        | Education level of the customer. |
| **MARRIAGE**         | Marital status of the customer.        |
| **AGE**              | Age of the customer in years.                                                 |
| **LIMIT_BAL**        | Credit limit of the customer.                         |
| **BILL_AMT1**        | Bill statement amount for the first month.                                  |
| **BILL_AMT2**        | Bill statement amount for the second month.                                 |
| **BILL_AMT3**        | Bill statement amount for the third month.                                  |
| **BILL_AMT4**        | Bill statement amount for the fourth month.                                 |
| **BILL_AMT5**        | Bill statement amount for the fifth month.                                  |
| **BILL_AMT6**        | Bill statement amount for the sixth month.                                  |
| **PAY_AMT1**         | Payment made by the customer for the first month.                             |
| **PAY_AMT2**         | Payment made by the customer for the second month.                            |
| **PAY_AMT3**         | Payment made by the customer for the third month.                             |
| **PAY_AMT4**         | Payment made by the customer for the fourth month.                            |
| **PAY_AMT5**         | Payment made by the customer for the fifth month.                             |
| **PAY_AMT6**         | Payment made by the customer for the sixth month.                             |
| **DEFAULT_NEXT_MONTH** | Whether the customer defaulted on payment in the next month (1 = Default, 0 = No Default). This is the target variable for the model. |


## Data Cleaning and Modelling

- Duplicate Removal: The dataset does not contain any duplicates.

- Missing Values: The dataset does not contain any missing values after preprocessing.

- Categorical Data Encoding: The categorical columns SEX, EDUCATION, and MARRIAGE were transformed into numerical values using encoding techniques.

- Feature Scaling: Numerical features, including LIMIT_BAL (credit limit), BILL_AMT1 to BILL_AMT6 (bill amounts), and PAY_AMT1 to PAY_AMT6 (payment amounts), were scaled using normalization techniques to ensure that all features contributed equally to the model training process.

- Feature Selection: A feature selection technique using mutual information was applied to select the most important features for model training.

- Modelling: Multiple machine learning algorithms were used to train models on the dataset. The performance of the models was evaluated using various metrics such as accuracy, precision, recall, and F1-score.



## Analysis and Insights

The analysis provided the following insights into the dataset:

- **Credit Default Distribution**: Over 20,000 credit card holders did not default, and around 5,000 credit card holders defaulted.
- **Gender Analysis**: The number of female users who did not default on their payments is significantly higher than the number of male users who did not default. Both the non-defaulting and defaulting counts are higher for female users, possibly due to a larger proportion of female credit card users in the dataset.
- **Education Level**: The university level has the highest number of non-defaulters, and there is also a significant count of defaulters at this education level.
- **Marital Status**: Married individuals are the least likely to default, followed by single individuals and others.
- **Credit Limit (`LIMIT_BAL`)**:
  - Non-Defaulters (0): The average credit limit is approximately 178,100.
  - Defaulters (1): The average credit limit is significantly lower at approximately 130,110.
  - Insight: Individuals with higher credit limits are less likely to default.
- **Age (`AGE`)**:
  - Non-Defaulters (0): The average age is approximately 35.42 years.
  - Defaulters (1): The average age is slightly higher at approximately 35.73 years.
  - Insight: Age does not show a significant difference between defaulters and non-defaulters.
- **Bill Amounts (`BILL_AMT1 to BILL_AMT6`)**:
  - Non-Defaulters (0): The average bill amounts decrease over the six months.
  - Defaulters (1): The average bill amounts also decrease but are consistently lower than those of non-defaulters.
  - Insight: Both groups show decreasing bill amounts, but defaulters consistently have lower average bill amounts.
- **Payment Amounts (`PAY_AMT1 to PAY_AMT6`)**:
  - Non-Defaulters (0): The average payment amounts are significantly higher, starting at approximately 6,307 and decreasing slightly over six months.
  - Defaulters (1): The average payment amounts are lower, starting at approximately 3,397.
  - Insight: Non-defaulters make higher payments on average compared to defaulters.

## Requirements

- Python 3.x
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
## Acknowledgements

The dataset used in this project is from the https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients