import random

secret = random.Random(7).randint(1, 10)
guesses = [3, 5, secret]
for turn, guess in enumerate(guesses[:3], start=1):
    print(f"Turn {turn}: guessed {guess}")
    if guess == secret:
        print("Correct!")
        break
    print("Too low!" if guess < secret else "Too high!")
