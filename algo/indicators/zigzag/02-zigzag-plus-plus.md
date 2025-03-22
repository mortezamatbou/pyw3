### Rewrite TradingView indicator by @author=lucemanb
### Convert pine script source codew to python with Grok3

#### Overview of the Pine Script
The script you shared is a custom ZigZag indicator for TradingView, inspired by the MT4 ZigZag indicator. It identifies key pivot points (Higher Highs, Lower Highs, Higher Lows, Lower Lows) in price action based on specific settings: Depth, Deviation, and Backstep. It also includes visual features like lines, labels, and alerts.

#### Simple Logic Explanation

*Inputs:* Price data (high and low prices of each candle) and three parameters: Depth (minimum lookback), Deviation (minimum price change percentage), and Backstep (minimum bars between pivots).

*How It Works:* The indicator looks for significant price swings (based on Deviation) where the direction changes (uptrend or downtrend). It connects these pivot points to form the ZigZag pattern.

*Output:* Key pivot points and the direction of movement (bullish or bearish).

#### Python Code
Since Pine Script runs in TradingView and isn’t directly translatable to Python, I’ve created a simplified version of the ZigZag logic in Python. Assuming price data is provided as lists (e.g., from pandas or an API), here’s the code:

```python
def zigzag(high_prices, low_prices, depth=12, deviation=5, backstep=2):
    # Lists to store ZigZag points and direction
    zigzag_points = []
    direction = 0  # 1 for bullish, -1 for bearish, 0 for start
    last_high = last_low = None
    last_pivot_idx = 0

    # Convert deviation to percentage
    deviation = deviation / 100

    for i in range(len(high_prices)):
        # Skip until we have enough data (depth)
        if i < depth:
            continue

        # Initialize the first point
        if last_high is None and last_low is None:
            last_high = high_prices[i]
            last_low = low_prices[i]
            last_pivot_idx = i
            zigzag_points.append((i, last_low, "Low"))
            direction = 0
            continue

        # Calculate price changes
        high_change = (high_prices[i] - last_low) / last_low if last_low else 0
        low_change = (last_high - low_prices[i]) / last_high if last_high else 0

        # Check for bullish pivot
        if direction >= 0 and high_change >= deviation:
            if i - last_pivot_idx >= backstep:
                last_high = high_prices[i]
                zigzag_points.append((i, last_high, "High"))
                direction = 1
                last_pivot_idx = i

        # Check for bearish pivot
        elif direction <= 0 and low_change >= deviation:
            if i - last_pivot_idx >= backstep:
                last_low = low_prices[i]
                zigzag_points.append((i, last_low, "Low"))
                direction = -1
                last_pivot_idx = i

    # Return points and direction
    return zigzag_points, direction

# Example usage
high_prices = [100, 102, 105, 103, 107, 110, 108, 104, 100, 98, 95, 97, 100]
low_prices = [99, 101, 104, 102, 106, 109, 107, 103, 99, 97, 94, 96, 99]

points, dir = zigzag(high_prices, low_prices, depth=3, deviation=5, backstep=2)

# Display results
for point in points:
    idx, price, type_ = point
    print(f"Index: {idx}, Price: {price}, Type: {type_}")

print(f"Direction: {'Bullish' if dir > 0 else 'Bearish' if dir < 0 else 'Neutral'}")
```
#### Explanation of the Python Code

*Inputs:*
*high_prices:* List of high prices.
*low_prices:* List of low prices.
*depth:* Minimum number of candles to start processing.
*deviation:* Minimum percentage price change to register a pivot.
*backstep:* Minimum distance (in bars) between two pivots.

#### *Logic:*

The code checks if the price has changed enough (based on Deviation).

If the change is significant and the distance from the last pivot (Backstep) is met, it registers a new pivot.

Direction is determined based on whether the movement is upward (bullish) or downward (bearish).

#### *Output:*

A list of ZigZag points, each containing the index, price, and type (High or Low).

The current direction (Bullish, Bearish, or Neutral).

Differences from the Original Pine Script

The Pine Script uses an external library (ZigLib) that I don’t have access to, so I’ve recreated the core ZigZag logic manually.

In Pine Script, lines and labels are drawn directly, which would require a plotting library like matplotlib in Python (I can add this if you want).

Features like color settings and transparency are omitted in this simplified version since Python doesn’t have a built-in graphical interface.

**Next Steps**

If you’d like me to add plotting (e.g., drawing the ZigZag lines) or any other feature, just let me know, and I’ll expand it for you! What do you think? Are you happy with this?

