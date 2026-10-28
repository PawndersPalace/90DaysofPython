import csv
from io import StringIO

sample_csv = StringIO("item,price\nbook,12.50\npen,1.50\n")
rows = csv.DictReader(sample_csv)
total = sum(float(row["price"]) for row in rows)
print(f"Total: ${total:.2f}")
