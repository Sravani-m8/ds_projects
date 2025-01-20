
# Stock Price Prediction

This project aims to predict the stock prices of Apple Inc. using time series analysis models like SARIMA (Seasonal ARIMA) and Prophet. The project uses historical stock data to train the models and forecasts future stock prices.


## Data

The dataset used for this project contains historical stock prices for Apple Inc. (`AAPL`). The data includes columns such as:

- `Date`: The date of the stock price.
- `Close`: The closing price of the stock on that day.
- `Adj Close`: Adjusted closing price.
- `High`: Highest price during the trading day.
- `Low`: Lowest price during the trading day.
- `Open`: Opening price of the stock.
- `Volume`: Number of shares traded on that day.



## Models


## SARIMA Model

The SARIMA model is implemented using `statsmodels` to forecast the future stock prices. The optimal parameters `(p, d, q)` and seasonal parameters `(P, D, Q, m)` are selected using grid search to minimize the AIC (Akaike Information Criterion).

### Key steps:
- Load and preprocess the data.
- Split the data into training and test sets.
- Use grid search to identify the best parameters for the SARIMA model.
- Fit the SARIMA model and evaluate the forecast.
- Generate a forecast for the next 30 days and visualize the results with confidence intervals.

### SARIMA Results:
- **Best ARIMA Parameters**: (0, 1, 2)
- **Best Seasonal Parameters**: (0, 1, 1, 21)
- **AIC**: 2232.476

### SARIMA Forecast:
forecast for the next 30 days.

## Prophet Model

The Prophet model is used to model the time series data with the option to add custom seasonality.

### Prophet Forecast:
The Prophet model gives forecasts with uncertainty intervals, showing predictions for the next 30 days.