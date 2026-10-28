def parse_quantity(text):
    try:
        quantity = int(text)
    except ValueError:
        print(f"{text!r} is not a whole number.")
        return None
    if quantity < 0:
        print("Quantity cannot be negative.")
        return None
    return quantity


print(parse_quantity("3"))
print(parse_quantity("three"))
