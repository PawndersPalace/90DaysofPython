import json

# An API returns data that programs can read; this is a sample response.
response_text = '{"name": "Ada", "language": "Python"}'
response = json.loads(response_text)
print(f"Name: {response['name']}")
print(f"Language: {response['language']}")
print("Before using a real API, read its documentation and usage limits.")
