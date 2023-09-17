# encoding: utf-8
from traderlib import *
from logger import *
import sys

# Initialize the Logger
initialize_logger()
lg.info('Logger called from main.')

# Check trading account make sure we're good to go - i.e. balance
def check_account_ok():
    try:
        # get account.info
        pass
    except Exception as e:
        lg.error('Could not get account info.')
        lg.info(str(e))
        sys.exit()

# Close current orders (double-check)
def clean_open_orders():
    # get list of open orders
    open_orders = None
    lg.info('List of open orders: ')
    lg.info(str(open_orders))

    for order in open_orders:
        # close.order
        lg.info('Order %s closed.' %str(order.id))

    lg.info('Closing orders complete.')

# Define the asset and output it as a String.
def get_ticker():
    # Enter ticker with Keyboard.
    ticker = input('Enter the ticker you want to execute: ')
    return ticker

# Execute trading bot
def main():
    initialize_logger()
    check_account_ok()
    clean_open_orders()
    ticker=get_ticker()

    trader = Trader(ticker)
    # Run trading bot.

    # Input: String(ticker)
    # Output: boolean (success=True, failure=False)

if __name__ == '__main__':
    main()
