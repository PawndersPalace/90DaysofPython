import unittest


def word_count(sentence):
    return len(sentence.split())


class WordCountTests(unittest.TestCase):
    def test_counts_words(self):
        self.assertEqual(word_count("learn Python daily"), 3)

    def test_empty_sentence(self):
        self.assertEqual(word_count(""), 0)


if __name__ == "__main__":
    unittest.main()
