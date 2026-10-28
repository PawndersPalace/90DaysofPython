items = ["apples", "bread"]
actions = [("add", "tea"), ("show", ""), ("remove", "bread"), ("show", "")]
for action, item in actions:
    if action == "add":
        items.append(item)
    elif action == "remove" and item in items:
        items.remove(item)
    elif action == "show":
        print(f"Shopping list: {items}")
