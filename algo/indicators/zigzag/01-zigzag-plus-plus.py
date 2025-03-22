"""
Rewrite TradingView indicator by @author=lucemanb
Convert pine script source codew to python with DeepSeek
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ZigZag config
Depth = 12
Deviation = 5
Backstep = 2

# ZigZag functions
def zigzag(high, low, depth, deviation, backstep):
    direction = 0
    z1 = 0
    z2 = 0
    last_high = high[0]
    last_low = low[0]
    zigzag_highs = []
    zigzag_lows = []
    zigzag_directions = []

    for i in range(len(high)):
        if direction == 0:
            if high[i] > last_high:
                last_high = high[i]
            if low[i] < last_low:
                last_low = low[i]
            if high[i] - last_low >= deviation:
                direction = 1
                z1 = last_low
                zigzag_lows.append(z1)
                zigzag_highs.append(np.nan)
                zigzag_directions.append(-1)
            elif last_high - low[i] >= deviation:
                direction = -1
                z1 = last_high
                zigzag_highs.append(z1)
                zigzag_lows.append(np.nan)
                zigzag_directions.append(1)
        elif direction == 1:
            if high[i] > last_high:
                last_high = high[i]
            if last_high - low[i] >= deviation:
                direction = -1
                z2 = last_high
                zigzag_highs.append(z2)
                zigzag_lows.append(np.nan)
                zigzag_directions.append(1)
                z1 = z2
        elif direction == -1:
            if low[i] < last_low:
                last_low = low[i]
            if high[i] - last_low >= deviation:
                direction = 1
                z2 = last_low
                zigzag_lows.append(z2)
                zigzag_highs.append(np.nan)
                zigzag_directions.append(-1)
                z1 = z2

    return zigzag_directions, zigzag_highs, zigzag_lows

# example and seed data
np.random.seed(42)
dates = pd.date_range('2023-01-01', periods=100, freq='D')
prices = np.cumsum(np.random.randn(100))
high = prices + np.random.rand(100) * 2
low = prices - np.random.rand(100) * 2

# ZigZag action
directions, zigzag_highs, zigzag_lows = zigzag(high, low, Depth, Deviation, Backstep)

# chart with 
plt.figure(figsize=(12, 6))
plt.plot(dates, prices, label='Price', color='blue', alpha=0.5)
plt.scatter(dates, zigzag_highs, color='red', label='ZigZag Highs', marker='v')
plt.scatter(dates, zigzag_lows, color='green', label='ZigZag Lows', marker='^')
plt.legend()
plt.title('ZigZag Indicator')
plt.show()


