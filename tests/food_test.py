import unittest

from src.food import Food


class FoodTest(unittest.TestCase):
    def setUp(self):
        self.food = Food("Lasagne", 7, 10)

    def test_food_has_name(self):
        self.assertEqual("Lasagne", self.food.name)

    def test_food_has_price(self):
        self.assertEqual(7, self.food.price)

    def test_food_has_rujuvination(self):
        self.assertEqual(10, self.food.rejuvination)
