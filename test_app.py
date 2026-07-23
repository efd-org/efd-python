import unittest

from app import get_greeting


class TestApp(unittest.TestCase):
    def test_get_greeting(self):
        self.assertEqual(get_greeting(), "Welcome to EFD Python project!")


if __name__ == "__main__":
    unittest.main()
