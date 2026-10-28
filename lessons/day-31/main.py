def greet(name, greeting="Hello", punctuation="!"):
    return f"{greeting}, {name}{punctuation}"


print(greet("Ada"))
print(greet("Grace", greeting="Welcome", punctuation="."))
