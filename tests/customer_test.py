import unittest
from src.customer import Customer


class CustomerTest(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Frodo", 51, 10)

    def test_customer_has_name(self):
        self.assertEqual("Frodo", self.customer.name)
