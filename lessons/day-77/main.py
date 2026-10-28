def calculate_total(prices):
    """Add item prices and return the total."""
    if any(price < 0 for price in prices):
        raise ValueError("Prices cannot be negative.")
    return sum(prices)


print(f"Total: ${calculate_total([4.50, 2.25]):.2f}")
