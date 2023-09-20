import matplotlib.pyplot as plt

stock_price = [190.64, 190.09, 192.25, 191.79, 194.45, 196.45, 196.42, 200.32, 200.32,
               200.85, 199.2, 199.2, 199.2, 199.46, 201.46, 197.54, 201.12, 203.12,
               203.12]

plt.plot(stock_price)
plt.title('Opening stock prices')
plt.xlabel('Days')
plt.ylabel('$ USD')
plt.show()
