import unittest


def double(number):
    return number * 2


class DoubleTests(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(double(4), 8)

    def test_zero(self):
        self.assertEqual(double(0), 0)


if __name__ == "__main__":
    unittest.main()
