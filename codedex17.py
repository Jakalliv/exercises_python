import unittest
from strings_utils import reverse_string, capitalize_string, is_capitalized

class TestStringUtils(unittest.TestCase):
    
    def test_revers_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("world"), "drow")
    def test_capitalize_string(self):
        self.assertEqual(capitalize_string("hello"), "Hello")
        self.assertEqual(capitalize_string("world"), "World")
    def test_is_capitalized(self):
        self.assertTrue(is_capitalized("Hello"))
        self.assertFalse(is_capitalized("Hello"))
        self.assertFalse(is_capitalized("world"))
        


if __name__ == '__main__':
  unittest.main()