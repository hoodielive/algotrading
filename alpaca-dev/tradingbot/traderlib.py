# encoding: utf-8


class Trader:
    def __init__(self, ticker):
        lg.info('Trader initialized with ticker %s.' %ticker)
        self.ticker = ticker

# Check if asset is tradable->ask the broker/API if asset is tradable.
        # Input: String (asset)
        # Output: Boolean
            # If fails, return to OGBE
    def is_tradable(self, ticker):
        try:
            # Get asset from alpaca wrapper.
            if not asset.tradable:
                lg.info('The asset %s is not tradable.' %ticker)
                return False
            else:
                lg.info('The asset %s is tradable.' %ticker)
        except:
            lg.error('The asset %s is not available.' %ticker)
            return False

# Set stop loss->takes a price as input and sets the stop loss.
        # Input: entry price, direction (long/short)
        # Output: String (stop loss)

    def set_stoploss(self, entryPrice, direction):
        stopLossMargin = 0.05 # %margin

        try:
            if direction == 'long':




# Set take profit->takes a price as an input and sets take profit.
        # Input: entry price
        # Output: String (take profit)

# Load historical data:
        # Input: ticker, interval, entry->limit
        # Output: Array (ohlc data)

# Get open positions
        # Input: ticker
        # Output: boolean (True=already open, False=not open)

# Submit Order->gets our order through the API(retry)
        # Input: order data
        # Output: boolean (True=order succeeded, False=failed)

# Cancel order->cancels order (retry)
        # Input: order id
        # Output: boolean (True=order cancels, False=failed)

# Check position->check whether position is opened or not opened
        # Input: ticker
        # Output: boolean (True=order processed, False=failed)

    def run(self):
        pass
# OGBE-ALPHA
# Loop until timemout 2hrs.
# Perform the initial check.
# Check the position->ask the broker/API if we have an open position with asset.
        # Input: String
        # Output: Boolean (True if exists and False if it does NOT exist)
            # If fails, return to OGBE

# General Trend.
# Load 30 min candles->demand the API to chart with 30min candles.
    # Input: (Whatever API needs), time range*, candle size*
    # Output: 30 mins candles (OHLC for every candle)

# Perform general trade analysis->detect interesting trend (up/down/no-trend)
    # Input: 30 min candles data (close data)
    # Output: Up, Down, No trend Strings
    # If no trend defined, go back to start.

# OYEKU-BETA
# While->Loop until timeout (30 mins)
# Step 1->Load 5 min candles.
        # Input: asset (or whatever the API needs), time range*, candle size*
        # Output: boolean (True=confirmed, False=not confirmed)
        # If fails, return to OYEKU

# Step 2->Perform instant trend analysis->confirm the trend detected by GT analysis
        # Input: 5 min candles date (Close data), output of the GT analysis (Up/Down (String))
        # Output: boolean (True=confirmed, False=not-confirmed)
        # If fails, return to OYEKU

# Step 3->Perform RSI analysis
        # Input: 5 min candles date (Close data), output of the GT analysis (Up/Down (String))
        # Output: boolean (True=confirmed, False=not-confirmed)
        # If fails, return to OYEKU

# Step 4->Perform stochastic analysis
        # Input: 5 min candles date (Close data), output of the GT analysis (Up/Down (String))
        # Output: boolean (True=confirmed, False=not-confirmed)
        # If fails, return to OYEKU

# Submit Order(limit order)->Interact with Broker/API
    # Input: n of shares of asset, desired price
    # Output: boolean (confirmed=True or False), get position id
    # If fail, abort / got to Ogbe

# check position->does position exist?
    # Input: position ID (integer)
    # Output: boolean (confirmed=True or False)
    # If fail, abort / got to Ogbe

# Loop until timeout (~8h)
# Enter position mode->loop->check the conditions in parallel (If true - close position)
    # If->Check take profit->close position
        # Input: current gains
        # Output: boolean
    # Elif->Check stop loss->if True->close position
        # Input: are we losing $
        # Output: boolean
    # Elif->Check stochastic crossing->If True->close position
        # Step 1: Pull 5min ohlc data
            # Input: asset
            # Output: ohlc data (5 min candles)
        # Step 2: see whether the stochastic curves are crossing
            # Input: ohlc data (5 min candles)
            # Output: boolean

# Get out
# Submit Order(market)->Interact with Broker/API
    # Input: n of shares of asset, position id
    # Output: boolean
    # If fail, retry until it works

# check position->does position exist?
    # Input: position ID (integer)
    # Output: boolean (still exists?)
    # If false, abort / go back to Submit Order

# Wait 15 minutes
# End
