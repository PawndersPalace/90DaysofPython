def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


assert celsius_to_fahrenheit(0) == 32
assert celsius_to_fahrenheit(100) == 212
assert round(celsius_to_fahrenheit(20), 1) == 68.0
print("All three temperature checks passed.")
