def make_page(title, message):
    return (
        "<!doctype html>\n"
        "<html lang=\"en\"><head><meta charset=\"utf-8\">"
        f"<title>{title}</title></head>"
        f"<body><h1>{title}</h1><p>{message}</p></body></html>"
    )


print(make_page("My first page", "I built this with Python."))
print("Optional next step: follow the official Flask or Streamlit quickstart.")
