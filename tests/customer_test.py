import unittest
from src.customer import Customer


class CustomerTest(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Frodo", 51, 10)

    def test_customer_has_name(self):
        self.assertEqual("Frodo", self.customer.name)

    def test_customer_age(self):
        self.assertEqual(51, self.customer.age)
