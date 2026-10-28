pages = {
    1: [{"id": 1}, {"id": 2}],
    2: [{"id": 3}, {"id": 4}],
    3: [],
}
page_number = 1
while pages[page_number]:
    print(f"Page {page_number}: {[item['id'] for item in pages[page_number]]}")
    page_number += 1
print("Stop when a page is empty; real APIs may also set rate limits.")
