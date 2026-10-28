import unittest


def search_books(books, query):
    query = query.casefold()
    return [
        book for book in books
        if query in book["title"].casefold() or query in book["author"].casefold()
    ]


class SearchBooksTests(unittest.TestCase):
    def test_finds_author_without_case_sensitivity(self):
        books = [{"title": "Kindred", "author": "Octavia Butler"}]
        self.assertEqual(search_books(books, "BUTLER"), books)

    def test_returns_empty_list_when_not_found(self):
        self.assertEqual(search_books([], "unknown"), [])


if __name__ == "__main__":
    unittest.main()
