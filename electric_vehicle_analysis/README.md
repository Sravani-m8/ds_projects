
# Analysis of Electric Vehicle (EV)

This project analyzes a dataset of electric vehicles registered in Washington state. The goal is to extract meaningful insights about EV adoption patterns, popular makes/models, and eligibility for clean alternative fuel vehicle (CAFV) incentives. The analysis includes data cleaning, descriptive statistics, and visualizations to uncover trends and patterns in electric vehicle registrations.




## Data

| **Feature Name**                                         | **Description**                                                                                     |
|----------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| `VIN (1-10)`                                             | The first 10 characters of the Vehicle Identification Number.                                       |
| `County`                                                 | County where the vehicle is registered.                                                             |
| `City`                                                   | City where the vehicle is registered.                                                               |
| `State`                                                  | State where the vehicle is registered (all entries are "WA").                                        |
| `Postal Code`                                            | Zip code of the vehicle's location.                                                                 |
| `Model Year`                                             | Manufacturing year of the vehicle.                                                                  |
| `Make`                                                   | Manufacturer of the vehicle (e.g., Tesla, Nissan).                                                  |
| `Model`                                                  | Specific model of the vehicle (e.g., Model 3, Leaf).                                                |
| `Electric Vehicle Type`                                  | Type of electric vehicle (e.g., Battery Electric Vehicle or Plug-in Hybrid Electric Vehicle).        |
| `Clean Alternative Fuel Vehicle (CAFV) Eligibility`      | Eligibility status for clean alternative fuel vehicle incentives.                                    |
| `Electric Range`                                         | Range of the vehicle on a full charge (in miles).                                                   |
| `Base MSRP`                                              | Manufacturer's Suggested Retail Price (in dollars).                                                 |
| `Legislative District`                                   | Legislative district of the vehicle's registration.                                                 |
| `DOL Vehicle ID`                                         | Unique ID for each vehicle in the Department of Licensing database.                                 |
| `Vehicle Location`                                       | Geographical coordinates of the vehicle's location.                                                 |
| `Electric Utility`                                       | Electric utility provider in the vehicle's area.                                                    |
| `2020 Census Tract`                                      | Census tract number for demographic and geographic analysis.                                         |


## Data Cleaning

1. **Missing Value Handling**:
   - Identified missing values in columns such as `Model`, `Legislative District`, `Vehicle Location`, and `Electric Utility`.
   - Dropped rows containing missing values to ensure data consistency.
2. **Duplicate Removal**:
   - Checked for duplicates and confirmed no duplicate rows in the dataset.
3. **Data Type Validation**:
   - Verified and ensured correct data types for numerical and categorical variables.
4. **Final Dataset**:
   - After cleaning, all columns were complete with no missing values.




## Data Analysis and Insights

### **Statistical Summary**
- Key numerical features like `Electric Range`, `Base MSRP`, and `Legislative District` were summarized:
  - Average electric range: **87.83 miles**
  - Minimum and maximum electric ranges: **0 miles** and **337 miles** respectively.
  - MSRP varied significantly, with a high standard deviation due to luxury vehicles.
  
### **Categorical Analysis**
- Most popular electric vehicle manufacturers: **Tesla, Nissan, Chevrolet**.
- Dominant electric vehicle type: **Battery Electric Vehicle (BEV)**.
- Eligibility for CAFV incentives:
  - **Clean Alternative Fuel Vehicle Eligible**: ~52%
  - **Not eligible**: ~13%
  - **Eligibility unknown**: ~35%

---

## **Visualizations**
### **Numerical Features**
- Histograms and box plots were created for `Electric Range`, `Base MSRP`, and `Legislative District`.
- Outliers in `Base MSRP` were observed, with values exceeding $800,000.

### **Categorical Features**
- Frequency distributions for `Make`, `Model`, `Electric Vehicle Type`, and `CAFV Eligibility` were analyzed.
- Bar plots revealed Tesla as the leading manufacturer in terms of vehicle registrations.


## **Observations**
1. **Tesla Dominance**: Tesla is the most popular electric vehicle manufacturer in the dataset, with models like `Model 3` and `Model Y` leading registrations.
2. **Electric Range**: Vehicles with higher electric ranges are more likely to qualify for CAFV incentives.
3. **Geographic Concentration**: The majority of electric vehicles are registered in urban areas like Seattle, Bellevue, and Redmond.


