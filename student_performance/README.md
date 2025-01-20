
# Student Performance Prediction

This project focuses on predicting students' exam scores based on various demographic, academic, and socio-economic factors. By leveraging machine learning techniques, the aim is to identify key factors influencing student performance and develop models to make accurate predictions. This analysis can assist educators and policymakers in understanding and improving student outcomes.


## Dataset

- **Hours_Studied**: Number of hours a student studies per day.
- **Attendance**: Attendance percentage.
- **Sleep_Hours**: Average hours of sleep per day.
- **Previous_Scores**: Previous exam scores.
- **Tutoring_Sessions**: Number of tutoring sessions attended.
- **Physical_Activity**: Hours spent on physical activities per week.
- **Parental_Involvement** (High, Medium, Low)
- **Access_to_Resources** (High, Medium, Low)
- **Extracurricular_Activities** (Yes, No)
- **Motivation_Level** (High, Medium, Low)
- **Internet_Access** (Yes, No)
- **Family_Income** (High, Medium, Low)
- **Teacher_Quality** (High, Medium, Low)
- **School_Type** (Public, Private)
- **Peer_Influence** (Positive, Neutral, Negative)
- **Learning_Disabilities** (Yes, No)
- **Parental_Education_Level** (High School, College, Postgraduate)
- **Distance_from_Home** (Near, Moderate, Far)
- **Gender** (Male, Female)
- **Exam_Score**: The final exam score of the student.




## Data Preprocessing

1. **Handling Missing Values:**
   - Missing values in categorical features were replaced with the mode.
   - Numerical features had no missing values.

2. **Feature Selection:**
   - Used Mutual Information Regression to identify features with the highest predictive power.
   - Selected features with mutual information greater than zero.

3. **Data Scaling:**
   - Standardized numerical features using `StandardScaler` to ensure uniformity.

4. **Train-Test Split:**
   - Split the dataset into training (80%) and test (20%) sets.






## Model Development

1. **Linear Regression**
   - RMSE: 1.915
   - R² Score: 0.741

2. **Decision Tree Regressor**
   - RMSE: 3.161
   - R² Score: 0.293

3. **Random Forest Regressor**
   - RMSE: 2.215
   - R² Score: 0.653

4. **Support Vector Regressor (SVR)**
   - RMSE: 1.937
   - R² Score: 0.735

5. **K Nearest Neighbors (KNN) Regressor**
   - RMSE: 2.351
   - R² Score: 0.609

6. **Gradient Boosting Regressor**
   - RMSE: 1.976
   - R² Score: 0.724

## Results and Observations
- **Linear Regression** and **Support Vector Regressor (SVR)** achieved the highest performance with R² scores of 0.741 and 0.735, respectively.
- Feature selection and scaling significantly improved model performance.




## Key Insights

- Attendance and Hours_Studied were the most influential features in predicting exam scores.

- Socio-economic factors such as Parental Involvement and Access to Resources also contributed to performance but to a lesser extent.