# Bot Structure

1. Asset
2. Check Position
3. Check if tradable
4. load 30-min data
5. get general trend
- clear trend
6. load 5-min data
7. get instant trend
8. get rsi
9. get stochastic
- loop in series until all conditions are met
10. Enter trade
11. Submit Order
12. Check Position
13. Enter position mode
if we can't enter the position - go back to step one
- Decision tree:
If ok: 
  check take-profit
elif: 
  check stochastic
elif:
  check stop-loss
close
Take some time (wait, 30mins)
Check Position
Wait some time


