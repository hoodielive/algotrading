from alpaca_trade_api.rest import REST, TimeFrame

BASE_URL = "https://paper-api.alpaca.markets"
KEY_ID = "PKOGTADT4DLEOEBVLFA4"
SECRET_KEY = "vRvQD7BpUBKZOWtalu8h4iufaeAwyr8sMLif9uWA"

# Instantiate REST API Connection
api = REST(key_id=KEY_ID,secret_key=SECRET_KEY,base_url=BASE_URL)

account = api.get_account()
print(account.account_number)
print(account.portfolio_value)
print(account.cash)

def buy_stock(stock, qty):
    api.submit_order(
        symbol=stock, 
        qty=qty, 
        side="buy", 
        type="market", 
        time_in_force="gtc"
    )

buy_stock('AAPL', 1)

def get_stock_price(symbol):
    """
    Returns the current stock price for the given symbol.
    """
    # Fetch current stock price
    barset = api.get_barset(symbol, 'minute', limit=1)  # Fetching the latest minute bar
    bar = barset[symbol][0]  # Access the first (and only) bar
    return bar.c  # Return the close price, which is the latest available price

# Test our function
stock_symbol = 'AAPL'
#print(f"The current price of {stock_symbol} is: ${get_stock_price(stock_symbol)}")

def get_stock_price2(symbol, timeframe):
    barset = api.get_bars(symbol, timeframe)
    return barset

print(get_stock_price2("AAPL", "1Min"))


