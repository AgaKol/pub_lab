import unittest

from src.food import Food


class FoodTest(unittest.TestCase):
    def setUp(self):
        self.food = Food("Lasagne", 7, 10)

    def test_food_has_name(self):
        self.assertEqual("Lasagne", self.food.name)
