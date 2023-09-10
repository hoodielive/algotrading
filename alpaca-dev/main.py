from alpaca_trade_api.rest import REST, TimeFrame
import pandas as pd

BASE_URL = "https://paper-api.alpaca.markets"
KEY_ID = "PKOGTADT4DLEOEBVLFA4"
SECRET_KEY = "vRvQD7BpUBKZOWtalu8h4iufaeAwyr8sMLif9uWA" 

# Instantiate REST API Connection
api = REST(key_id=KEY_ID,secret_key=SECRET_KEY,base_url=BASE_URL)

# Fetch 1 Minute Historical bars of Bitcoin
bars = api.get_crypto_bars('BTCUSD', TimeFrame.Minute).df

# Filter by exchange
bars = bars[bars.exchange == 'CBSE']
print(bars)

# Create a market order to buy 1 Bitcoin
# best_buy = api.submit_order(symbol='BTCUSD', qty=1, side='buy', type='market', time_in_force='gtc')

api.get_position('BTCUSD')

positions = api.list_positions()
position_qty = 0

for p in positions:
    if p.symbol == 'BTCUSD':
        position_qty = float(p.qty)
print(positions)
print(position_qty)

