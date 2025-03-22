"""
Rewrite TradingView indicator by @author=lucemanb
Convert pine script source codew to python with Grok3
"""

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