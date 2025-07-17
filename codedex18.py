import unittest
import math

def get_sqrt(n):
  return math.sqrt(n)

def divide(a, b):
  return a / b

class TestUnexpected(unittest.TestCase):
    def test_sqrt(self):
        self.assertEqual(get_sqrt(4), 2)
        self.assertFalse(get_sqrt(9) == 2)
        self.assertGreater(get_sqrt(16), 3)
        with self.assertRaises(ValueError):
            get_sqrt(-1)
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)




if __name__ == '__main__':
  unittest.main()
  