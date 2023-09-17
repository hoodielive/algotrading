import pandas as pd
import yfinance as yf

# Grab the data.

df = yf.download (
    "AAPL",
    start="2023-01-01", end="2023-07-30", progress=False
)

# Inspect the downloaded data.

print(f'Downloaded {len(df)} rows of data.')

# The result of the request is a pandas DataFrame.
# It contains Open, High, Low and Close (OHLC) prices and adjusted close price and volume.

print(df)

google_data = yf.Ticker('goog')
print("Google Data: ")
print(google_data.get_shares_full(start="2022-01-01", end=None))
print(google_data.institutional_holders)
print(google_data.major_holders)
print(google_data.news)
