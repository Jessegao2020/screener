import yfinance as yf

ticker = yf.Ticker("AAPL")
print(ticker.balance_sheet)
