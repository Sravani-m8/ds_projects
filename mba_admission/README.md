
# MBA Admission Prediction

This project aims to predict MBA admissions decisions ("Admit" or "Waitlist") based on applicants' demographic, academic, and professional profiles. By building a machine learning model, we help identify key factors influencing admissions and provide a systematic approach to evaluating candidates.

## Dataset Description

The dataset consists of MBA applications with the following features:

| Feature          | Description                                  |
|------------------|----------------------------------------------|
| `application_id` | Unique identifier for each application       |
| `gender`         | Gender of the applicant                     |
| `international`  | Whether the applicant is an international student |
| `gpa`            | Undergraduate GPA                           |
| `major`          | Undergraduate major                         |
| `race`           | Race/ethnicity of the applicant             |
| `gmat`           | GMAT score                                  |
| `work_exp`       | Years of work experience                    |
| `work_industry`  | Industry of work experience                 |
| `admission`      | Admission decision ("Admit" or "Waitlist")  |




## Project Steps

### Data Preprocessing
1. **Handling Missing Values:**
    - Filled missing values in the `admission` column with "Waitlist."
    - Dropped rows with missing values in other columns (e.g., `race`).

2. **Duplicate Removal:**
    - Verified there were no duplicate rows.

3. **Feature Removal:**
    - Dropped the `application_id` column and `international` column, as they were irrelevant for prediction.

4. **Encoding Categorical Variables:**
    - Applied one-hot encoding to categorical features (`gender`, `major`, `race`, `work_industry`).
    - Label encoded the target feature (`admission`).

5. **Scaling Numerical Features:**
   - Standardized numerical features (`gpa`, `gmat`, `work_exp`) using `StandardScaler`.

6. **Addressing Class Imbalance:**
   - Used SMOTE (Synthetic Minority Oversampling Technique) to balance the classes in the training data.


### Exploratory Data Analysis (EDA)

1.  **Categorical Features**:
   - Plotted count distributions of features like `gender`, `major`, `race`, and `work_industry` against the `admission` target.

2. **Numerical Features**:
   - Visualized distributions and boxplots for `gpa`, `gmat`, and `work_exp` to understand trends and detect outliers.


### Feature Engineering
1. **Categorical Encoding:**
   - One-hot encoded `gender`, `major`, `race`, and `work_industry`.
2. **Target Encoding:**
   - Encoded `admission` with 0 = "Admit" and 1 = "Waitlist."

### Model Building and Evaluation

   - Built and compare multiple models based on recall.
   - Random Forest and Gradient Boosting models showed robust performance with higher recall and AUC-ROC scores.


## Analysis Insights

![image](https://github.com/user-attachments/assets/6534e1d9-7136-4019-8271-378faa2ce881)

1. There are more male applicants compared to female applicants, indicating a higher interest or application rate among males for the MBA program.

2. All applicants are non-international, suggesting that the MBA program predominantly attracts domestic students.

3. The GPA of applicants ranges from approximately 2.8 to 3.8, with a peak around 3.3. This indicates a relatively high academic performance among the applicants.

4. The majority of applicants come from Humanities, followed by Business and STEM fields. This diversity in academic backgrounds showcases the interdisciplinary appeal of the MBA program.

5. White applicants constitute the highest number of applicants, followed by Asian, Black, Hispanic, and Other racial backgrounds. This highlights the racial diversity within the applicant pool.

6. GMAT scores range from approximately 550 to 800, with a peak around 650, indicating a wide range of test performance among the applicants.

7. The median work experience is around 5 years, with a range from 1 to 9 years. This suggests that the applicants have substantial professional experience prior to applying for the MBA program.

8. The largest number of applicants come from the Technology industry, followed by Consulting, Financial Services, and Health Care. This indicates the MBA program's strong appeal to professionals from diverse industries.


## Acknowledgements

The dataset used in this project is available on Kaggle: https://www.kaggle.com/datasets/taweilo/mba-admission-dataset
