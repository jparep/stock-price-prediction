# ARIMA/SARIMA Stock Price Prediction

This project demonstrates the use of ARIMA and SARIMA models for forecasting stock prices. The goal is to predict the closing prices of a specific stock (e.g., Apple Inc. - AAPL) for the next 30 days based on historical data.

## Table of Contents

- [Introduction](#introduction)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Modeling Process](#modeling-process)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Stock price prediction is a common application of time series forecasting techniques. ARIMA (AutoRegressive Integrated Moving Average) is a widely-used model for analyzing and forecasting time series data. SARIMA (Seasonal ARIMA) extends ARIMA by explicitly modeling seasonality in the data.

This project aims to:
1. Load historical stock price data.
2. Fit an ARIMA/SARIMA model to the data.
3. Forecast future stock prices.
4. Visualize the predicted prices against the actual prices.

## Dataset

The dataset used in this project consists of historical stock prices for Apple Inc. (AAPL) downloaded from Yahoo Finance.

### Data Fields:
- `Date`: The trading date.
- `Open`: The price of the stock at market open.
- `High`: The highest price of the stock during the trading day.
- `Low`: The lowest price of the stock during the trading day.
- `Close`: The price of the stock at market close.
- `Volume`: The number of shares traded.
- `Adj Close`: The adjusted closing price after accounting for corporate actions like dividends and stock splits.

### Downloading the Data:
You can download the dataset directly using the `yfinance` Python package:
```python
import yfinance as yf

# Download historical data for AAPL
data = yf.download('AAPL', start='2018-01-01', end='2024-01-01')
data.to_csv('AAPL_stock_data.csv')
