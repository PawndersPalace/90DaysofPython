project = {
    "name": "Reading tracker",
    "must_have": ["add a book", "list books", "save books"],
    "later": ["search by author", "show reading statistics"],
}
for number, feature in enumerate(project["must_have"], start=1):
    print(f"Task {number}: {feature}")
print(f"Build later: {', '.join(project['later'])}")
