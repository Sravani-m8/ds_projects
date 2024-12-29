

# Academic Dropout Prediction

Student dropout rates are a significant concern for educational institutions globally. High dropout rates can negatively impact a university's reputation, financial stability, and the overall success of students. Predicting and identifying students at risk of dropping out allows schools, colleges, and universities to provide targeted support and resources to these students. By addressing factors such as financial aid, mental health support, and academic assistance, institutions can reduce dropout rates and improve student retention.

#### Objective of the Project:
The primary objective of this project is to develop a predictive model that can identify students at risk of dropping out based on their personal, academic, and socio-economic characteristics. Leveraging machine learning techniques, the project aims to build an effective and accurate model that will help educational institutions proactively intervene and support at-risk students, ensuring they stay on track to graduate successfully.


## Dataset Description

The dataset used for this project contains several features that provide insights into the academic, demographic, and socio-economic aspects of students. Below is a detailed description of the columns in the dataset:

### **Demographic Features**
1. **Marital Status**: The marital status of the student (e.g., single, married).
2. **Nationality**: The nationality of the student, indicating their country of origin.
3. **Gender**: The gender of the student (e.g., male, female).
4. **Age at Enrollment**: The age of the student when they enrolled in the program.
5. **Displaced**: Indicates if the student is displaced (e.g., living away from their hometown).
6. **International**: Indicates if the student is an international student.

### **Family Information**
7. **Mother's Qualification**: The highest educational qualification of the student's mother.
8. **Father's Qualification**: The highest educational qualification of the student's father.
9. **Mother's Occupation**: The occupation of the student's mother.
10. **Father's Occupation**: The occupation of the student's father.

### **Academic Information**
11. **Application Mode**: The method through which the student applied to the institution.
12. **Application Order**: The preference order in which the student applied to the institution.
13. **Course**: The course in which the student is enrolled.
14. **Daytime/Evening Attendance**: Indicates whether the student attends classes during the day or in the evening.
15. **Previous Qualification**: The prior educational qualification of the student.
16. **Curricular Units 1st Sem (Credited)**: The number of curricular units credited in the first semester.
17. **Curricular Units 1st Sem (Enrolled)**: The number of curricular units the student enrolled in during the first semester.
18. **Curricular Units 1st Sem (Evaluations)**: The number of curricular units evaluated in the first semester.
19. **Curricular Units 1st Sem (Approved)**: The number of curricular units approved in the first semester.
20. **Curricular Units 1st Sem (Grade)**: The average grade of the curricular units in the first semester.
21. **Curricular Units 1st Sem (Without Evaluations)**: The number of curricular units in the first semester where no evaluations occurred.
22. **Curricular Units 2nd Sem (Credited)**: The number of curricular units credited in the second semester.
23. **Curricular Units 2nd Sem (Enrolled)**: The number of curricular units the student enrolled in during the second semester.
24. **Curricular Units 2nd Sem (Evaluations)**: The number of curricular units evaluated in the second semester.
25. **Curricular Units 2nd Sem (Approved)**: The number of curricular units approved in the second semester.
26. **Curricular Units 2nd Sem (Grade)**: The average grade of the curricular units in the second semester.
27. **Curricular Units 2nd Sem (Without Evaluations)**: The number of curricular units in the second semester where no evaluations occurred.

### **Financial Information**
28. **Debtor**: Indicates whether the student has unpaid tuition fees.
29. **Tuition Fees Up to Date**: Indicates whether the student has paid their tuition fees on time.
30. **Scholarship Holder**: Indicates whether the student is a scholarship recipient.

### **Socio-Economic Indicators**
31. **Unemployment Rate**: The unemployment rate during the student's enrollment.
32. **Inflation Rate**: The inflation rate during the student's enrollment.
33. **GDP**: The Gross Domestic Product (GDP) during the student's enrollment.

### **Target Variable**
34. **Target**: The final status of the student:
   - **Dropout**: The student has left the program without completing it.
   - **Graduate**: The student has successfully completed the program.
   - **Enrolled**: The student is still actively pursuing the program.


## Preprocessing and Model building


1. **Data Import and Inspection**:  
   - Imported the dataset successfully and inspected the structure of the data.
   - Verified there were no missing values or duplicated rows in the dataset.

2. **Exploratory Data Analysis (EDA)**:  
   - Checked the statistical summary of numerical columns to understand their distributions, ranges, and potential outliers.
   - Visualized the data distribution using boxplots to identify outliers for each numerical column.
   - Plotted the correlation heatmap to understand relationships among numerical features and identify multicollinearity.

3. **Target Variable Analysis**:  
   - Performed a count plot to visualize the distribution of the target classes (`Graduate`, `Dropout`, and `Enrolled`).
   - There is class imbalance with the majority class being `Graduate` followed by `Dropout` and `Enrolled`.

4. **Feature Encoding**:  
   - Performed Encoding on the target variable.

5. **Modelling**:  
   - Implemented models like Logistic Regression, Decision Trees, Random Forest, Ada Boost and Gradient Boosting. 

## Key Findings from Data Analysis

![image](https://github.com/user-attachments/assets/f1e02962-74a5-4003-9e38-124f43b01302)

1. **Marital Status Distribution**:
 -  Most students with a marital status of 1 have higher counts in all target categories, particularly "Dropout."
- Other marital statuses have significantly lower representation across all targets, indicating marital status may influence educational outcomes.

2. **Course Enrollment**:
 - Course 13 has the highest number of graduates, significantly more than other courses.
 - Dropout rates are distributed relatively evenly across different courses.

4. **Gender Distribution**:
 - Male students have a significantly higher dropout rate compared to female students.
   -Female students have higher rates of graduation compared to male students.

5. **Strong Correlation Between Curricular Unit Metrics**:
  - Metrics related to curricular units (e.g., "Curricular units 1st sem enrolled," "approved," "evaluations," "grade") have high positive correlations with each other. This suggests that performance in one curricular unit is strongly linked to performance in others.

6. **Negative Correlation with Age at Enrollment**:
 - "Age at enrollment" shows a negative correlation with variables like "Curricular units 1st sem (approved)" and "Curricular units 2nd sem (grade)." Older students may face challenges in academic performance compared to younger students.

7. **No Significant Correlation for Socioeconomic Factors**:
  - Variables such as "Unemployment rate," "Inflation rate," and "GDP" show weak correlations with most other features, indicating they might have minimal direct impact on academic performance or dropout rates.

