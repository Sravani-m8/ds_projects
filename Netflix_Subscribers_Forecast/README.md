
# Netflix Subscribers Forecasting

The goal of this project is to forecast Netflix's subscriber count over time using historical subscription data. The data is analyzed using seasonal decomposition, stationarity tests, ARIMA modeling and SARIMA for seasonal effects. 


## Data

The dataset used in this project is the Netflix-Subscriptions.csv file, which contains the following columns:

- Time_Period: The date when the subscription count was recorded.
- Subscribers: The number of Netflix subscribers for that period.
## Project Steps

### 1. Data Preprocessing

- **Data Cleaning**: The `Time_Period` column is converted to a `datetime` format, and the data is set to a time series index.
- **Data Type Handling**: The `Subscribers` column is converted to numeric values.

### 2. Exploratory Data Analysis (EDA)

- Visualizations were created to analyze the trend of subscribers over time.
- Seasonal decomposition was performed to observe the trend, seasonal, and residual components of the time series.

### 3. Stationarity Test

- The Augmented Dickey-Fuller (ADF) test was used to test if the time series is stationary.
- differencing methods were applied to achieve stationarity.

### 4. ARIMA Modeling

- After stationarizing the data, Autocorrelation Function (ACF) and Partial Autocorrelation Function (PACF) plots were analyzed to determine the potential parameters (p, d, q).
- A SARIMA model was then fitted to the data using the optimal parameters.

### 5. SARIMA Model Selection

- grid search was performed over different combinations of (p, d, q) and seasonal (P, D, Q) parameters to select the best model based on the AIC (Akaike Information Criterion).

### 6. Model Evaluation

- The best SARIMA model was evaluated based on AIC, BIC, and residual analysis.

### 7. Forecasting

- The final SARIMA model was used to forecast future Netflix subscriber counts.


## Results

- The SARIMA model with the best parameters was used to forecast future subscribers.
- The AIC, BIC, and Ljung-Box test statistics were used to evaluate the model.