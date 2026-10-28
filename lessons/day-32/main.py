def make_message(name):
    message = f"Welcome, {name}!"  # Local to this function
    return message


result = make_message("Ada")
print(result)
# print(message)  # Try uncommenting: local names are not available here.
