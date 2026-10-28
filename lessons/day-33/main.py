def add(first, second):
    return first + second


def divide(first, second):
    if second == 0:
        raise ValueError("The divisor cannot be zero.")
    return first / second


print(f"4 + 3 = {add(4, 3)}")
print(f"8 / 2 = {divide(8, 2)}")
