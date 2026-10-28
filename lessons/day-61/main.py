from datetime import datetime

date_text = "2026-10-28"
parsed_date = datetime.strptime(date_text, "%Y-%m-%d")
print(f"Long form: {parsed_date:%B %d, %Y}")
print(f"ISO form: {parsed_date.date().isoformat()}")
