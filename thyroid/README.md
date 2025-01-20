
# Thyroid Prediction 

This project focuses on predicting the recurrence of thyroid cancer using various medical and demographic features. The dataset includes multiple factors such as radiotherapy history, smoking history, type and physical examination details. We use machine learning techniques for classification to predict whether the thyroid will recur.



## Project Steps

## Data Preprocessing

### Label Encoding
The target variable "Recurred" is encoded as binary values (`0` for no recurrence, `1` for recurrence) using `LabelEncoder` from `sklearn.preprocessing`.

### Feature Engineering
Several categorical variables are encoded using one-hot encoding (e.g., thyroid function status, physical examination results, and cancer types). These features are included for analysis and model training.

### Missing Values and Scaling
The dataset has no missing values after preprocessing, and all categorical variables are one-hot encoded. Numerical features such as age are scaled for better model performance.

## Feature Selection

The feature selection step involves calculating the mutual information between the features and the target variable ("Recurred") using the `mutual_info_classif` method from `sklearn.feature_selection`. Features with low mutual information scores (close to 0) are dropped to improve model performance.

The selected features for model building include:

- **Age, Gender, Smoking History, Radiotherapy History, Thyroid Function**
- **Physical Examination results**
- **Adenopathy, Types, Tumor Stages, and Lymph Node Details**
- **Treatment Response**

## Model Building and Evaluation

Several classification models are built and evaluated using the selected features:

- **Logistic Regression**
- **Decision Tree Classifier**
- **Random Forest Classifier**
- **AdaBoost Classifier**
- **Gradient Boosting Classifier**

### Model Evaluation Metrics

Each model is evaluated based on the following metrics:

- Accuracy
- Precision (Macro average)
- Recall (Macro average)
- F1 Score (Macro average)
- Confusion Matrix
- Classification Report

### Model Performance

Sample output for **Logistic Regression**:

```
Logistic Regression Metrics:
Accuracy: 0.9452054794520548
Precision: 0.9272959183673469
Recall: 0.9478609625668449
F1 Score: 0.9373417632878003
Confusion Matrix:
[[55  1]
 [ 3 45]]
Classification Report:
              precision    recall  f1-score   support

           0       0.95      0.98      0.96        56
           1       0.98      0.94      0.96        48

    accuracy                           0.95       104
   macro avg       0.96      0.96      0.96       104
weighted avg       0.96      0.95      0.95       104
```

## Results

Logistic Regression showed the best balance between precision and recall, making it the top model for this prediction task.
