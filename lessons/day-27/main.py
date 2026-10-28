original = ["pen", "book", "lamp"]
copy = original.copy()
copy.remove("book")
available = [item for item in original if item != "lamp"]
print(f"Original is unchanged: {original}")
print(f"Edited copy: {copy}")
print(f"Filtered items: {available}")
