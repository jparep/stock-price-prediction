import yfinance as yf
data = yf.download('AAPL', start='2018-01-01', end='2024-01-01')
data.to_csv('AAPL_stock_data.csv')
