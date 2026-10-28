from datetime import date, timedelta

today = date.today()
next_week = today + timedelta(days=7)
days_left = (next_week - today).days
print(f"Today: {today:%A, %B %d}")
print(f"One week from now: {next_week:%A, %B %d}")
print(f"Days until then: {days_left}")
