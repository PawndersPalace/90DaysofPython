prices = [4.50, 2.25, 3.00]
subtotal = sum(prices)
tax_rate = 0.08
total = subtotal * (1 + tax_rate)
print(f"Subtotal: ${subtotal:.2f}")
print(f"With tax: ${total:.2f}")
