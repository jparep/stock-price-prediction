import yfinance as yf
data = yf.download('AAPL', start='2018-01-01', end='2024-01-01')
data.to_csv('AAPL_stock_data.csv')

# Load data
data = pd.read_csv('AAPL_stock_data.csv', index_col='Date', parse_dates=True)
closing_prices = data['Close']

# Differencing to make the series stationary
diff_series = closing_prices.diff().dropna()

# Fit ARIMA model
model = ARIMA(diff_series, order=(5,1,0))
model_fit = model.f