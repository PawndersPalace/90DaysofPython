def total_prices(prices):
    total = 0
    for price in prices:
        total += price
    return total


print(f"Total: ${total_prices([2.50, 3.00]):.2f}")
print("Try: ruff check lessons/day-75/main.py")
