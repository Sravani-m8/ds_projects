
# Car Evaluation Classification using Machine Learning

In the real world, car buyers are often overwhelmed by the vast number of available options. This project aims to streamline the decision-making process by predicting the suitability of cars based on various important features. It helps automate the classification of cars, offering a valuable tool for both consumers and dealerships to efficiently assess and rank cars according to individual preferences.

# Objective:
The primary objective of this project is to build and train machine learning models that accurately classify cars into one of four categories based on key attributes. These categories include:

- Unacceptable (unacc)

- Acceptable (acc)
- Good (good)
- Very Good (vgood)
By predicting the acceptability of cars, this project enables potential buyers to make well-informed decisions, considering factors such as cost, safety, and other crucial elements. The model's insights help users quickly determine which cars are the best fit for their specific needs.

## Dataset Description

The dataset used for this project is the Car Evaluation Dataset, obtained from the [https://archive.ics.uci.edu/dataset/19/car+evaluation]. This dataset contains information about various car attributes and their acceptability.

| **Column Name** | **Description**                                                                                   |
|------------------|---------------------------------------------------------------------------------------------------|
| **buying**       | Cost of the car (`vhigh`, `high`, `med`, `low`).                                                  |
| **maint**        | Maintenance cost of the car (`vhigh`, `high`, `med`, `low`).                                     |
| **doors**        | Number of doors (`2`, `3`, `4`, `5more`).                                                        |
| **persons**      | Seating capacity of the car (`2`, `4`, `more`).                                                  |
| **lug_boot**     | Size of the luggage boot (`small`, `med`, `big`).                                                |
| **safety**       | Safety rating of the car (`low`, `med`, `high`).                                                 |
| **class**        | Target variable indicating acceptability (`unacc`, `acc`, `good`, `vgood`).                      |

## Steps Performed

### 1. Data Preprocessing
- Renamed columns for better readability.
- Verified there were no missing or duplicate values.
- Encoded categorical variables:
  - Used **One-Hot Encoding** for feature columns.
  - Used **Label Encoding** for the target column.

### 2. Exploratory Data Analysis (EDA)
- Analyzed the distribution of each feature using `value_counts()` and visualized it with count plots.
- Explored relationships between features and the target variable using comparative bar plots.

### 3. Model Building
Built and evaluated the following models:
- **Decision Tree Classifier**
- **AdaBoost Classifier**
- **Gradient Boosting Classifier**
- **Naive Bayes Classifier**

### 4. Model Evaluation & Model Comparison

| **Model**             | **Accuracy** | **Precision** | **Recall** | **F1 Score** |
|------------------------|--------------|---------------|------------|--------------|
| Decision Tree          | 97.98%      | 96.36%        | 97.73%     | 96.89%       |
| AdaBoost               | 83.53%      | 80.13%        | 76.43%     | 75.75%       |
| Gradient Boosting      | 98.84%      | 95.90%        | 99.14%     | 97.46%       |
| Naive Bayes            | 86.42%      | 80.42%        | 63.85%     | 69.29%       |

## Key Insights

1. **Most cars are classified as unacceptable:**  
   A significant portion of cars in the dataset are labeled as "unacceptable," indicating they fail to meet key standards.  

2. **High buying price often leads to unacceptability:**  
   Cars with higher prices (`vhigh` and `high`) are more frequently classified as unacceptable, likely due to heightened expectations for premium-priced vehicles.  

3. **Passenger capacity strongly affects acceptability:**  
   Cars with a capacity of two passengers are more likely to be  unacceptable. Models accommodating four or more passengers show better acceptability ratings.  

4. **Luggage boot size has a minor influence:**  
   Cars with medium or large luggage boots are slightly more likely to be classified as acceptable or very good, reflecting a preference for better storage options.

   ![image](https://github.com/user-attachments/assets/ab85d2fa-3d34-4ecd-b1f5-a02af33c6bf8)
   
## Requirements

- Python 3.x  
- Libraries: pandas, numpy, matplotlib, seaborn, scikit-learn  
