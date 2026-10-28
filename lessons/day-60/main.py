import re

text = "Contact ada@example.com or support@example.org."
pattern = r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}"
for address in re.findall(pattern, text):
    print(address)
print("A simple pattern is a starting point, not full email validation.")
