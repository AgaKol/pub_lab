import unittest

from src.pub import Pub
from src.customer import Customer
from src.drinks import Drinks


class PubTest(unittest.TestCase):

    def setUp(self):
        self.pub = Pub("The Prancing Pony", 1000)
        self.drinks = Drinks("Fanta", 1, 0)
        self.customer = Customer("Frodo", 51, 10, 0)
        self.customer2 = Customer("Sam", 17, 0, 6)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(1000, self.pub.till)

    def test_till_can_increase(self):
        self.pub.increase_till(self.drinks.price)
        self.assertEqual(1001, self.pub.till)

    def test_customer_of_age(self):
        self.assertEqual(True, self.pub.customer_of_age(self.customer))

    def test_customer_not_of_age(self):
        self.assertEqual(False, self.pub.customer_of_age(self.customer2))

    def test_customer_sober(self):
        self.assertEqual(True, self.pub.customer_sober(self.customer))

    def test_customer_drunk(self):
        self.assertEqual(False, self.pub.customer_sober(self.customer2))

    def test_pub_can_serve(self):
        self.pub.serve_customer(self.customer, self.drinks)
        self.assertEqual(1001, self.pub.till)
        self.assertEqual(9, self.customer.wallet)
        self.assertEqual(0, self.customer.drunkness)

    def test_pub_cannot_serve(self):
        self.assertEqual(False, self.pub.serve_customer(
            self.customer2, self.drinks))
