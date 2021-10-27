import unittest
from src.customer import Customer
from src.drinks import Drinks
from src.pub import Pub
from src.food import Food


class CustomerTest(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Frodo", 51, 10, 0)
        self.customer2 = Customer("Sam", 70, 0, 6)
        self.customer3 = Customer("Pippin", 35, 15, 5)
        self.drink = Drinks("Beer", 1, 3)
        self.pub = Pub("The Prancing Pony", 1000)
        self.food = Food("Pizza", 4, 4)

    def test_customer_has_name(self):
        self.assertEqual("Frodo", self.customer.name)

    def test_customer_age(self):
        self.assertEqual(51, self.customer.age)

    def test_customer_has_wallet(self):
        self.assertEqual(10, self.customer.wallet)

    def test_customer_drunkness(self):
        self.assertEqual(0, self.customer.drunkness)

    def test_cutomer_wallet_can_decrease(self):
        self.customer.reduce_wallet(self.drink.price)
        self.assertEqual(9, self.customer.wallet)

    def test_wallet_greaterThan_orEqualTo_drink_price(self):
        self.assertEqual(True, self.customer.enough_money(self.drink))

    def test_wallet_lessThan_drink_price(self):
        self.assertEqual(False, self.customer2.enough_money(self.drink))

    def test_can_customer_buy_drink(self):
        self.customer.buy_drink(self.drink)
        self.assertEqual(3, self.customer.drunkness)
        self.assertEqual(9, self.customer.wallet)

    def test_customer_can_buy_food(self):
        self.customer.buy_food(self.food)
        self.assertEqual(15, self.customer3.wallet)
        self.assertEqual(5, self.customer3.drunkness)
