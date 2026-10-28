catalog = {
    "python": {"description": "A programming language", "year": 1991},
    "turtle": {"description": "A beginner-friendly drawing module", "year": 1967},
}
query = "python".strip().lower()
result = catalog.get(query)
if result:
    print(f"{query}: {result['description']} ({result['year']})")
else:
    print("No matching entry.")
