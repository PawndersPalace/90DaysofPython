records = [
    {"name": " Ada ", "score": "90"},
    {"name": "Grace", "score": "85"},
]
cleaned = [
    {"name": row["name"].strip(), "score": int(row["score"])}
    for row in records
]
for row in cleaned:
    print(f"{row['name']}: {row['score']}")
