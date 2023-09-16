# Define the asset and output it as a String.

# OGBE-ALPHA
# Loop until timemout 2hrs.
# Perform the initial check.
# Check the position: ask the broker/API if we have an open position with asset.
    # Input: String
    # Output: Boolean (True if exists and False if it does NOT exist)
        # If fails, return to OGBE

# Check if asset is tradable: ask the broker/API if asset is tradable.
    # Input: String
    # Output: Boolean
        # If fails, return to OGBE

# General Trend.
# Load 30 min candles: demand the API to chart with 30min candles.
    # Input: (Whatever API needs), time range*, candle size*
    # Output: 30 mins candles (OHLC for every candle)

# Perform general trade analysis: detect interesting trend (up/down/no-trend)
    # Input: 30 min candles data (close data)
    # Output: Up, Down, No trend Strings
    # If no trend defined, go back to start.

# OYEKU-BETA
# While->Loop until timeout (30 mins)
# Step 1->Load 5 min candles.
        # Input: asset (or whatever the API needs), time range*, candle size*
        # Output: boolean (True=confirmed, False=not confirmed)
        # If fails, return to OYEKU

# Step 2->Perform instant trend analysis: confirm the trend detected by GT analysis
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


