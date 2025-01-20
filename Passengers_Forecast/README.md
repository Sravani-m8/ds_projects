
# Airline Passengers Forecast

This project involves forecasting the number of airline passengers using time series analysis. The objective of the project is to apply time series modeling techniques to predict future passenger counts based on historical data.


## Dataset

The dataset airline_passengers.csv consists of the following columns:

- Month: The month and year of the data point.
- Passengers: The number of passengers for the corresponding month.
## Project Steps

### 1. Data Cleaning
- The dataset was loaded and cleaned. There were no duplicates or missing values found.
- The 'Month' column was converted to a `datetime` type for proper handling in time series analysis.

### 2. Time Series Decomposition
- The time series was decomposed using both additive and multiplicative models to examine trends, seasonality, and residual components. The decomposition helps in understanding the underlying patterns in the data.

  ![image](https://github.com/user-attachments/assets/a8952687-b1ab-4e75-b4e0-eb6b6d8ab7de)

### 3. Stationarity Check
- The **Augmented Dickey-Fuller (ADF) test** was used to check the stationarity of the time series.
  - The series was initially non-stationary.
  - First-order differencing (1st Diff) was applied, but it was still non-stationary.
  - After second-order differencing (2nd Diff), the series became stationary.

### 4. Seasonal Differencing
- Seasonal differencing (with a lag of 12 months) was applied to make the series stationary.

### 5. Autocorrelation and Partial Autocorrelation
- **ACF (Autocorrelation Function)** and **PACF (Partial Autocorrelation Function)** plots were generated to understand the autocorrelation structure and determine the appropriate AR (Auto-Regressive) and MA (Moving Average) components for the ARIMA model.

### 6. Model Selection
- The **auto_arima** function from the `pmdarima` library was used to find the best ARIMA model. The chosen model was `ARIMA(2,1,1)(0,1,0)[12]`.

### 7. Model Evaluation
- The **SARIMAX** (Seasonal ARIMA with Exogenous Regressors) model was used for forecasting the number of passengers based on the best-fit ARIMA parameters.

### 8. Forecasting
- The trained SARIMAX model was used to forecast future passenger counts.



## Results

- The SARIMAX model successfully fitted the passenger data with an AIC of 1017.847 and provided predictions for future passenger numbers.
## Requirements

- Python 3.x
- pandas
- numpy
- matplotlib
- seaborn
- statsmodels
- pmdarima
