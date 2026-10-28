contact = {"name": "Ada", "email": "ada@example.com"}
print(f"Name: {contact['name']}")
print(f"Phone: {contact.get('phone', 'not provided')}")
contact["phone"] = "555-0100"
print(f"Saved fields: {', '.join(contact.keys())}")
