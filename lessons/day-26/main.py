names = ["Grace", "Ada", "Linus", "Guido"]
by_length = sorted(names, key=len)
by_last_letter = sorted(names, key=lambda name: name[-1].lower())
print(f"By length: {by_length}")
print(f"By last letter: {by_last_letter}")
