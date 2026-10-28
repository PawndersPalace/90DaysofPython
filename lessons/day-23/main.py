menu = [
    {"name": "soup", "price": 5.50, "vegetarian": True},
    {"name": "pasta", "price": 9.00, "vegetarian": True},
    {"name": "fish", "price": 12.00, "vegetarian": False},
]
for item in menu:
    label = " (vegetarian)" if item["vegetarian"] else ""
    print(f"{item['name']}: ${item['price']:.2f}{label}")
