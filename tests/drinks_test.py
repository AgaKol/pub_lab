import unittest
from src.drinks import Drinks


class DrinksTest(unittest.TestCase):
    def setUp(self):
        self.drinks = Drinks("Red Bull", 3, 0)

    def test_drink_has_name(self):
        self.assertEqual("Red Bull", self.drinks.name)
