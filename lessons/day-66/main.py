import json

def read_title(response_text):
    try:
        data = json.loads(response_text)
    except json.JSONDecodeError as error:
        print(f"Response was not valid JSON: {error.msg}")
        return None
    title = data.get("title")
    if not isinstance(title, str):
        print("Response has no text title.")
        return None
    return title


print(read_title('{"title": "Practice parsing"}'))
print(read_title("{broken"))
