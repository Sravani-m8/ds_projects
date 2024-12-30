![Uploading image.png…]()

# Job Outcome Prediction

The job market is highly competitive, and understanding the factors that drive successful career outcomes is essential for employers, job seekers, and educational institutions. This project helps individuals understand how their educational background, skills, and personality traits influence their career opportunities, enabling them to make informed decisions about skill enhancement and career planning.

The main objective is to analyze and identify the key factors that influence job outcomes by analyzing the relationships between demographic, educational, and job-related variables and their impact on salary and job designation.

## Data Description

The dataset contains diverse features that can be broadly classified into **Personal Background**, **Career Information**, **Academic Details**, **AMCAT Scores**, and **Personality Traits**. Here's a detailed explanation of each feature:


### **Personal Background**
1. **Gender**: Indicates the gender of the individual:

2. **Date of Birth (DOB)**: The birth date of the individual.

3. **10percentage**: Percentage scored in the 10th-grade board examination.

4. **10board**: The board of education for the 10th-grade exam (e.g., CBSE, state boards).

5. **12percentage**: Percentage scored in the 12th-grade board examination.

6. **12board**: The board of education for the 12th-grade exam (e.g., CBSE, ICSE, state boards).



### **Career Information**
1. **Salary**: The annual salary offered to the individual.

2. **Designation**: The job role/title assigned to the individual (e.g., Software Engineer, Senior Quality Engineer).

3. **JobCity**: The city where the job is located.

4. **Date of Joining (DOJ)**: The start date of employment.

5. **Date of Leaving (DOL)**: The end date of employment.

---

### **Academic Details**
1. **Degree**: The degree pursued by the individual (e.g., B.Tech/B.E.).

2. **Specialization**: The specific field of study (e.g., Computer Engineering, Electronics).

3. **CollegeGPA**: The cumulative GPA achieved during college.

4. **CollegeID**: A unique identifier for the college attended by the individual.

5. **CollegeTier**: Classification of colleges into tiers based on reputation and resources.

6. **CollegeCityID**: A unique identifier for the city where the college is located.

7. **CollegeCityTier**: Classification of the college city based on development (e.g., metropolitan, urban, rural).

8. **CollegeState**: The state where the college is located.

9. **GraduationYear**: The year of graduation.


### **AMCAT Scores**
AMCAT (Aspiring Minds Computer Adaptive Test) assesses candidates' employability based on various domains:
1. **English**: Assesses verbal ability, including grammar, comprehension, and vocabulary.
2. **Logical**: Evaluates logical reasoning and problem-solving skills.
3. **Quant**: Tests numerical ability and mathematical aptitude.
4. **Domain**: Measures domain-specific knowledge in engineering and technology, such as:
   - **ComputerProgramming**: Knowledge of programming concepts and coding skills.
   - **ElectronicsAndSemicon**: Understanding of electronics and semiconductor principles.
   - **ComputerScience**: Knowledge of fundamental computer science topics.
   - **MechanicalEngg**: Skills in mechanical engineering principles.
   - **ElectricalEngg**: Understanding of electrical engineering concepts.
   - **TelecomEngg**: Knowledge of telecommunications engineering.
   - **CivilEngg**: Expertise in civil engineering principles.


### **Personality Traits**
These scores are derived from personality assessments and are rated on a scale:
1. **Conscientiousness**: Reflects how organized, responsible, and dependable an individual is.

2. **Agreeableness**: Indicates an individual's ability to work well with others.

3. **Extraversion**: Measures sociability and enthusiasm.

4. **Neuroticism**: Represents emotional stability.

5. **Openness to Experience**: Reflects creativity and willingness to explore new ideas.


## Data Cleaning and Analysis

1. **Standardizing `JobCity` Names**:
   - Cleaned and standardized city names in the `JobCity` column by replacing variations and misspellings with consistent names (e.g., “Banglore”, “Bangalore ”, and “Bengaluru” were all replaced with “Bangalore”).
   - Consolidated cities into fewer categories based on a threshold (e.g., cities with fewer than 120 occurrences were grouped into “Other”).

2. **Standardizing Education Board Names**:
   - Cleaned and standardized entries in the `10board` column using a function to categorize boards into common types (“CBSE”, “ICSE”, “State Board”, etc.).
   - Applied a similar process to the `12board` column to ensure consistency in naming conventions for education boards.

3. **Cleaning `DOL` (Date of Leaving) Column**:
   - Removed unnecessary timestamps from the `DOL` column.
   - Replaced entries labeled as “present” with a consistent end date (“1/1/16”).
   - Converted the `DOL` column to datetime format for proper analysis.

4. **Cleaning `DOJ` (Date of Joining) Column**:
   - Removed unnecessary timestamps from the `DOJ` column.
   - Converted the `DOJ` column to datetime format.

5. **Calculating Tenure**:
   - Derived a new feature, `tenure`, by calculating the absolute difference between `DOL` and `DOJ` in months.
   - Converted `tenure` to an integer for better interpretability.

### **Exploratory Data Analysis (EDA)**

#### **Numerical Features**
1. **Distribution Analysis**:
   - Plotted histograms and boxplots for all numerical features to understand their distributions and identify outliers.

#### **Categorical Features**
1. **Frequency Distribution**:
   - Created count plots for all categorical features to visualize the distribution of categories.

2. **Salary by Categorical Features**:
   - Generated boxplots to analyze the relationship between `Salary` and categorical features such as `Gender`, `10board`, `12board`, and `JobCity`.

3. **Designation Analysis**:
   - Created count plots for `Designation` with the following comparisons:
     - `Designation` by `Gender`
     - `Designation` by `10board`
     - `Designation` by `12board`
     - `Designation` by `JobCity`

#### **Statistical Tests**

1. **One-Sample T-Test for Salaries**:
   - Tested whether the average salary for roles of interest (“Engineering”, “Software Development”, “Data Analytics”) was significantly different from a claimed mean of 2.75 lakhs.
   - **Result**: If \( p < 0.05 \), rejected the null hypothesis; otherwise, failed to reject it.

2. **Chi-Square Test for Independence**:
   - Analyzed relationships between categorical variables:
     - `Gender` and `Specialization`
     - `Gender` and `Designation`
   - **Result**: If \( p < 0.05 \), concluded significant relationships exist; otherwise, no significant relationship.

3. **ANOVA Test for Salaries Across Job Cities**:
   - Compared mean salaries across different `JobCity` categories to determine significant differences.
   - **Result**: If \( p < 0.05 \), concluded significant differences; otherwise, no significant difference.

4. **Two-Sample T-Test for Gender Salary Differences**:
   - Compared mean salaries of male and female employees.
   - **Result**: If \( p < 0.05 \), concluded significant differences; otherwise, no significant difference.




## Insights from Analysis

![image](https://github.com/user-attachments/assets/88a800c3-d152-4bdd-b300-701edc96ba1f)

1. **Academic Performance Trends:**  
- Most students scored around 85 in their 10th-grade exams and around 80 in their 12th-grade exams. A similar pattern was observed in college GPAs, with most students achieving around 80.  

2. **Distribution of Educational Institutions:**  
- The majority of students graduated from tier 2 colleges, with only a few from tier 1 institutions. However, most colleges attended were located in tier 1 cities.  

3. **Aptitude and Skill-Based Scores:**  
- Scores in English, Logical, and Quantitative sections typically clustered around 500, while Computer Programming scores averaged 400. Specialized technical sections like Electronics, Computer Science, and Mechanical Engineering had lower average scores, typically around 50-100.   

4. **Demographic Patterns:**  
- Most candidates were around 25 years old, with a smaller group of older individuals.  

5. **Job Tenure Insights:**  
 - The average job tenure among candidates was approximately 50 months, though some individuals had significantly longer tenures.  


6. **Employment and Career Trends:**  
- Most engineering graduates are employed in engineering-related roles, with software development being the second most common career path. Key hubs for engineering jobs in India include Bangalore, Chennai, and Gurgaon, although many graduates work in smaller towns or rural areas.

7. **Demographics and Educational Background:**  
- The majority of engineering graduates are male, and most completed their 10th and 12th-grade education following the State Board curriculum, with CBSE being the second most common choice.

8. **Educational Qualifications and Specializations:**  
- Most graduates hold a Bachelor of Technology (B.Tech) or Bachelor of Engineering (B.E.) degree, while a smaller proportion pursued Master’s degrees in specialized fields. Popular specializations include "Electronics and Communication Engineering," "Computer Science," "Information Technology," and "Mechanical Engineering."

9. **Academic Performance Relationships:**              - - 

 - There is a strong positive correlation between 10th and 12th-grade scores (0.87), indicating consistent academic performance. Additionally, 12th-grade percentage and college GPA show a moderate positive correlation (0.35), suggesting a link between higher school grades and better college outcomes.

 10. There is a significant difference in mean salaries between male and female employees.

 11. There is a significant difference in mean salaries across different JobCity categories.
