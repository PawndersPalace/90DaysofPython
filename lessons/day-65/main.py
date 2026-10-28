import json
from urllib.request import Request

url = "https://jsonplaceholder.typicode.com/todos/1"
request = Request(url, headers={"Accept": "application/json"})
sample_response = '{"userId": 1, "id": 1, "title": "learn Python", "completed": false}'
print(f"Prepared a GET request for: {request.full_url}")
print(f"Sample JSON title: {json.loads(sample_response)['title']}")
print("The example does not need a network connection to run.")
