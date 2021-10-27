import unittest
from src.customer import Customer
from src.drinks import Drinks
from src.pub import Pub


class CustomerTest(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Frodo", 51, 10)
        self.drink = Drinks("Beer", 1, 3)
        self.pub = Pub("The Prancing Pony", 1000)

    def test_customer_has_name(self):
        self.assertEqual("Frodo", self.customer.name)

    def test_customer_age(self):
        self.assertEqual(51, self.customer.age)

    def test_customer_has_wallet(self):
        self.assertEqual(10, self.customer.wallet)

    # def test_customer_can_buy_drink(self):
    #     self.pub.till.increase_till(self.drink.price)
    #     self.customer.wallet.reduce_wallet(self.drink.price)
    #     self.assertEqual(9, self.customer.buy_drink(self.drink.name))

    def test_cutomer_wallet_can_decrease(self):
        self.customer.reduce_wallet(self.drink.price)
        self.assertEqual(9, self.customer.wallet)
