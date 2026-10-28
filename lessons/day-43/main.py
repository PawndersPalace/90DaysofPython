import random

choices = ["read", "draw", "code"]
generator = random.Random(12)  # A seed makes this example repeatable.
print(f"Today's activity: {generator.choice(choices)}")
