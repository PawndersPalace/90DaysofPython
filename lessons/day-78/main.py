import csv
from io import StringIO

data = StringIO("month,visitors\nJan,12\nFeb,18\nMar,15\n")
rows = list(csv.DictReader(data))
best_month = max(rows, key=lambda row: int(row["visitors"]))
average = sum(int(row["visitors"]) for row in rows) / len(rows)
print(f"Most visitors: {best_month['month']} ({best_month['visitors']})")
print(f"Monthly average: {average:.1f}")
