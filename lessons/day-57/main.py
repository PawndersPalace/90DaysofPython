import json

profile = {"name": "Ada", "topics": ["Python", "math"], "finished": False}
text = json.dumps(profile, indent=2)
restored_profile = json.loads(text)
print(text)
print(f"Decoded name: {restored_profile['name']}")
