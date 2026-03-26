import pandas as pd
import numpy as np

# Generate realistic-looking stock data
np.random.seed(42)
n = 500

price = 1500.0
rows  = []

for i in range(n):
    open_p  = round(price + np.random.uniform(-10, 10), 2)
    high_p  = round(open_p + np.random.uniform(0, 20), 2)
    low_p   = round(open_p - np.random.uniform(0, 20), 2)
    close_p = round(open_p + np.random.uniform(-15, 15), 2)
    volume  = int(np.random.uniform(500000, 5000000))
    rows.append([open_p, high_p, low_p, close_p, volume])
    price   = close_p

df = pd.DataFrame(rows, columns=['Open', 'High', 'Low', 'Close', 'Volume'])
df.to_csv('data/stock.csv', index=False)
print(f"Generated {n} rows of stock data -> data/stock.csv")