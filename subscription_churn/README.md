
# Subscription Churn Prediction

Subscription churn refers to the phenomenon where customers cancel or discontinue their subscriptions to a service over a given period. High churn rates can significantly impact revenue, profitability, and long-term business growth.

The primary objective of this project is to develop a machine learning model to predict customer churn in a subscription-based service. By identifying customers who are likely to churn, the business can take proactive measures to retain them and optimize its customer relationship strategies.

## Dataset

The **Subscription Churn Prediction** project involves a dataset containing customer-related features and the target variable `Churn`, which indicates whether a customer has canceled their subscription (churned) or not. Below is a detailed description of the dataset:

- **AccountAge**: The duration (in months) that the customer has been subscribed to the service.
- **MonthlyCharges**: The amount the customer is billed monthly for the subscription.
- **TotalCharges**: The total amount billed to the customer over the course of their subscription.
- **ViewingHoursPerWeek**: The number of hours per week the customer spends watching content on the platform.
- **AverageViewingDuration**: The average duration (in minutes) the customer spends watching content per session.
- **ContentDownloadsPerMonth**: The number of content downloads per month by the customer.
- **UserRating**: The average rating (e.g., 1 to 5) the customer gives to the content on the platform.
- **SupportTicketsPerMonth**: The number of support tickets the customer raises per month.
- **WatchlistSize**: The number of items in the customer's watchlist.
- **SubscriptionType**: Type of subscription (e.g., Basic, Premium, etc.).
- **PaymentMethod**: Method used for payment (e.g., CreditCard, BankTransfer, etc.).
- **PaperlessBilling**: Whether the customer receives paperless billing (Yes/No).
- **ContentType**: Type of content the customer prefers (e.g., Movies, TV Shows, etc.). (Dropped for modeling)
- **MultiDeviceAccess**: Whether the customer has access to the platform across multiple devices (Yes/No). (Dropped for modeling)
- **DeviceRegistered**: Whether the customer has registered a device on the platform (Yes/No). (Dropped for modeling)
- **ViewingHoursPerWeek**: Number of hours the customer watches content per week.
- **AverageViewingDuration**: Average viewing time per session.
- **GenrePreference**: Preferred content genre (e.g., Drama, Comedy, etc.).
- **Gender**: Gender of the customer (Male/Female).
- **SubtitlesEnabled**: Whether subtitles are enabled for the customer (Yes/No).
- **ParentalControl**: Whether the customer has enabled parental controls (Yes/No). (Dropped for modeling)

- **Churn**: Binary indicator of whether the customer has churned (1) or remained subscribed (0).


## Project Workflow

1. **Missing and Duplicate Values:**

- No missing or duplicate values were found in the dataset.

2. **Feature Selection:**

- **Chi-Square and T-Tests:** Performed to identify significant features related to the target variable.
- Dropped irrelevant categorical columns.

3. **Encoding Categorical Variables:**

- One-hot encoding applied to `SubscriptionType`, `PaymentMethod`, `GenrePreference`, and `Gender`.

4. **Feature Scaling:**

- Standardized numerical features using `StandardScaler`.

5. **Train-Test Split:**

- Stratified split to ensure balanced representation of `Churn` in training and test sets.


6. **Modeling:**

- Several classification algorithms will be evaluated, such as Logistic Regression, Decision Trees, Random Forest, Gradient Boosting, and Neural Networks.

7. **Evaluation Metrics:**

- **Primary Metric:** Recall (to minimize False Negatives).
- Other Metrics: Precision, F1-score, ROC-AUC.

