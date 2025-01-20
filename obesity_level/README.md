
# Obesity Classification Using Lifestyle and Demographic Data

This project focuses on analyzing and predicting obesity levels based on lifestyle, demographic, and behavioral data from individuals. Using the Obesity Dataset, the goal is to classify individuals into predefined categories based on their eating habits, physical activity, and other socio-demographic factors.

The aim is to develop an accurate model to assist in understanding the contributing factors to obesity and aid in early detection and preventive healthcare measures.


## Project Workflow


### **Data Cleaning**
1. **Duplicate Handling:**
- Found and removed 24 duplicate rows from the dataset.

2. **Data Overview:**
- Checked the dataset's structure using `df.info()` and confirmed all columns have non-null values.
- Verified no missing values.

3. **Numerical Features:**
- Extracted and summarized numerical columns using `.describe()`.
- Plotted boxplots to check for outliers.

4. **Categorical Features:**
- Extracted categorical columns (excluding the target `NObeyesdad`) and analyzed their value counts.
- Visualized distributions using count plots and pie charts.

5. **Target Variable:**
- Analyzed the distribution of obesity classes in the `NObeyesdad` column with count plots and pie charts.

6. **Feature Relationships:**
- Created visualizations (e.g., count plots and boxplots) to explore the relationships between features and the target variable.

7. **Encoding Categorical Features:**
- Applied one-hot encoding to categorical features and label encoding to the target variable.


![image](https://github.com/user-attachments/assets/08e15dbb-0e52-4c97-9c89-00fa31c24350)

### **Model Building**
1. **Train-Test Split:**
- Used `train_test_split` from `sklearn.model_selection` to split the data into training and test sets (e.g., 80%-20%).

2. **Feature Scaling:**
- Normalized numerical features using `StandardScaler` to standardize data for model training.

3. **Model Selection:**
 - Trained multiple classification models to predict obesity categories:
     - Logistic Regression
     - Decision Tree Classifier
     - Random Forest Classifier
     - Support Vector Machine (SVM)
     - Gradient Boosting 

4. **Evaluation Metrics:**
- Evaluated models using metrics such as accuracy, precision, recall, F1-score, and confusion matrix and achieved highest recall and f1 score with gradient boosting model.

