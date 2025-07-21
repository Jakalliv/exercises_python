import unittest
from coffee_menu import CoffeeMenu




class TestCoffeeMenu(unittest.TestCase):
    def setUp(self):
        self.menu = CoffeeMenu().menu
        
    def test_get_price_existing_item(self):
        self.assertEqual(self.menu.get("Espresso"), 2.5)
        self.assertEqual(self.menu.get("Caffe Latte"), 3.0)
        self.assertEqual(self.menu.get("Cappuccino"), 3.5)
        self.assertEqual(self.menu.get("Brodaglia Imbevibile"), 30.0)
    def test_if_item_not_in_menu(self):
        self.assertIsNone(self.menu.get("Macchiato"))
        self.assertFalse("Macchiato" in self.menu)
        
        
if __name__ == '__main__':
  unittest.main()