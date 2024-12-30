
# Insurance Claims Fraud Detection

Fraudulent claims are a major issue for insurance companies, with billions of dollars lost globally each year. Detecting and preventing fraud can save significant amounts of money, which can be redistributed to legitimate customers and result in lower premiums for policyholders.
The ability to detect fraud early allows insurers to mitigate risks more effectively. Automating the fraud detection process using machine learning models reduces the need for manual interventions, speeding up the claim review process. It also minimizes human error, ensuring more accurate and consistent decision-making.

#### Objective of the Project:
The main objective of the Insurance Claims Fraud Detection project is to develop a machine learning model capable of identifying fraudulent claims based on historical data. The model will predict the likelihood of fraud based on various features such as customer demographics, policy details, and claim characteristics.






## Dataset

The dataset contains the following columns:
1. **months_as_customer**: Duration of the customer’s association with the insurance company.
2. **age**: Age of the insured individual.
3. **policy_number**: Unique identifier for the policy.
4. **policy_bind_date**: Date the policy was bound.
5. **policy_state**: State where the policy is issued.
6. **policy_csl**: Combined Single Limit (CSL) of the policy.
7. **policy_deductable**: Deductible amount on the policy.
8. **policy_annual_premium**: Annual premium paid for the policy.
9. **umbrella_limit**: Limit of the umbrella insurance coverage.
10. **insured_zip**: Zip code of the insured.
11. **insured_sex**: Gender of the insured.
12. **insured_education_level**: Education level of the insured.
13. **insured_occupation**: Occupation of the insured.
14. **insured_hobbies**: Hobbies of the insured.
15. **insured_relationship**: Relationship status of the insured.
16. **capital-gains**: Capital gains of the insured.
17. **capital-loss**: Capital losses of the insured.
18. **incident_date**: Date of the incident for which the claim is made.
19. **incident_type**: Type of incident (e.g., collision, theft).
20. **collision_type**: Type of collision (if applicable).
21. **incident_severity**: Severity of the incident (e.g., major damage, minor damage).
22. **authorities_contacted**: Whether the authorities were contacted after the incident.
23. **incident_state**: State where the incident occurred.
24. **incident_city**: City where the incident occurred.
25. **incident_location**: Location of the incident.
26. **incident_hour_of_the_day**: Hour of the day when the incident occurred.
27. **number_of_vehicles_involved**: Number of vehicles involved in the incident.
28. **property_damage**: Whether property damage occurred.
29. **bodily_injuries**: Number of bodily injuries from the incident.
30. **witnesses**: Number of witnesses to the incident.
31. **police_report_available**: Whether a police report is available.
32. **total_claim_amount**: Total amount of the claim.
33. **injury_claim**: Amount of the injury claim.
34. **property_claim**: Amount of the property claim.
35. **vehicle_claim**: Amount of the vehicle claim.
36. **auto_make**: Make of the vehicle involved.
37. **auto_model**: Model of the vehicle involved.
38. **auto_year**: Year of the vehicle.
39. **fraud_reported**: Whether the claim is fraudulent or not (Target variable).




## Data Cleaning & Modelling

1. **Handling Missing Values**: 
  - The dataset contains missing values represented by `?`. These are replaced with `NaN`, and relevant columns are filled with appropriate values or categories based on domain knowledge. 
   - Missing values in columns like `collision_type`, `property_damage`, and `police_report_available` were filled with default values.

2. **Data Transformation**:
  - Dates such as `policy_bind_date` and `incident_date` are converted to datetime objects for further analysis.
   - New columns are derived, such as `policy_bind_year`, `incident_year`, and `incident_month`, to capture more temporal features.

3. **Categorical Encoding**:
  - Categorical variables like `insured_sex`, `insured_occupation`, `incident_type`, etc., are encoded using one-hot encoding or ordinal encoding as appropriate.

4. **Scaling Numeric Features**:
  - Features like `months_as_customer`, `age`, `total_claim_amount`, etc., are standardized using `StandardScaler` to ensure they have the same scale.

5. **Feature Engineering**:
  - Extracted the year, month, day, and weekday from `policy_bind_date` and `incident_date`.
-  Applied one-hot encoding to categorical features.
- Encoded `incident_severity` and `insured_education_level` using `OrdinalEncoder`.

6. **Statistical Testing**:
 - Performed hypothesis testing to check the relationship between various features and fraud detection:
- **T-tests** for continuous variables to compare fraud and non-fraud groups.
- **Chi-Square Test** for categorical variables to examine if there is a significant association with fraud.

7. **Resampling**: 
- Used SMOTE (Synthetic Minority Over-sampling Technique) to handle class imbalance.

8. **Model Training**: 
- Train machine learning models like Logistic Regression, Decision Trees, and Random Forest on the preprocessed data and evaluate the models using recall, precision and f1score.

## Key Insights from Fraud Claims Project Statistics

1. **Customer Tenure**:
  - The average customer tenure is approximately 204 months (around 17 years), with a wide range from 0 to 479 months, indicating long-term customer relationships.

2. **Age of Policyholders**:
  - Policyholders' ages range from 19 to 64 years, with an average age of about 39 years, reflecting a diverse age group of insured individuals.

3. **Policy Deductibles and Premiums**:
  - The average policy deductible is $1136, with a range from $500 to $2000. The average annual premium is $1256.41, ranging from $433.33 to $2047.59, showing variability in policy costs.

4. **Incident Characteristics**:
  - Incidents most commonly occur around midday (average incident hour is 11:44), typically involve around 1.84 vehicles, and result in approximately 0.99 bodily injuries and 1.49 witnesses per incident.

5. **Claim Amounts**:
  - The average total claim amount is $52,761.94, with injury claims averaging $7433.42, property claims at $7399.57, and vehicle claims at $37,928.95, highlighting variability in claim amounts.

6. **Capital Gains and Losses**:
  - Policyholders experience significant capital gains and losses, with average gains of $25,126 and average losses of -$26,793.70, reflecting the financial dynamics of insured individuals.

7. **Policy CSL (Combined Single Limit) Coverage**:
  - The most common policy coverage is 250/500 with 351 policies, followed closely by 100/300 with 349 policies and 500/1000 with 300 policies. This indicates a diverse range of coverage preferences among policyholders.

8. **Incident Type**:
  - The majority of incidents involve Multi-vehicle Collisions (419) and Single Vehicle Collisions (403). Less common incidents include Vehicle Theft (94) and Parked Car incidents (84), indicating that collisions are the primary cause of claims.

9. **Property Damage and Police Reports**:
  - A significant number of incidents resulted in property damage (698) and had police reports available (686). This highlights the importance of property damage and official documentation in fraud claims.


## Technologies

- Python 3.x
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- imbalanced-learn (SMOTE)
- SciPy
## Acknowledgements

The dataset used in this project is from the https://www.kaggle.com/datasets/arpan129/insurance-fraud-detection/data