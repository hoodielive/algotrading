from alpaca_trade_api.rest import REST, TimeFrame
import random
import time

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

def get_position(symbol):
    positions = api.list_positions()
    for p in positions:
        if p.symbol == symbol:
            return float(p.qty)
    return 0

SYMBOL = 'BTCUSD'
while True:
    # GET OUR CURRENT POSITION
    position = get_position(symbol=SYMBOL)
    
    # SCIENTIFICALLY CHECK IF WE SHOULD BUY OR SELL
    gods_say_buy = random.choice([True, False])
    print(f"Holding: {position} / Gods: {gods_say_buy}")
    #CHECK IF WE SHOULD BUY
    if position == 0 and gods_say_buy == True:
        # WE BUY ONE BITCOIN
        print('The gods have spoken:')
        print(f'Symbol: {SYMBOL} / Side: BUY / Quantity: 1')
        api.submit_order(SYMBOL, qty=1, side='buy', type='market', time_in_force='gtc')
    #HECK IF WE SHOULD SELL
    elif position > 0 and gods_say_buy == False:
        # WE SELL ONE BITCOIN
        print('The gods have spoken:')
        print(f'Symbol: {SYMBOL} / Side: SELL / Quantity: 1')
        api.submit_order(SYMBOL, qty=1, side='sell', type='market', time_in_force='gtc')
    print('Lets wait for the gods to manifest again...')
    print("*"*20)
    time.sleep(10)
