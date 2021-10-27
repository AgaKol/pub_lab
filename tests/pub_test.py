import unittest

from src.pub import Pub

from src.drinks import Drinks


class PubTest(unittest.TestCase):

    def setUp(self):
        self.pub = Pub("The Prancing Pony", 1000)
        self.drinks = Drinks("Fanta", 1, 0)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(1000, self.pub.till)

    def test_till_can_increase(self):
        self.pub.increase_till(self.drinks.price)
        self.assertEqual(1001, self.pub.till)
