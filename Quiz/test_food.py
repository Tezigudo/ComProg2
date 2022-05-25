"""This is testfile for quiz contain problem3 xD"""

import unittest
from food import Food


# Problem3
class TestFood(unittest.TestCase):
    """test for class Food"""

    def setUp(self) -> None:
        self.banana = Food("Banana", 100, 89, 20.2)
        self.egg = Food("Egg", 50, 30, 4.8)

    def test_equal(self):
        """Test that eq method work correctly"""
        dup_banana = Food("Banana", 100, 89, 20.2)
        self.assertEqual(self.banana, dup_banana)

    def test_add_same_name_food(self):
        """ adding food can do when same name"""
        dup_egg = Food("Egg", 200, 80, 6.6)
        self.assertAlmostEquals(self.egg + dup_egg, Food("Egg", 250, 110, 11.399999), places=4)

    def test_add_food_with_different_name(self):
        """Adding food with different name must raise ValueError """
        with self.assertRaises(ValueError):
            self.banana + self.egg

    # testing behind requirement(external)
    def test_init(self):
        """ testing Initialization """
        self.assertEqual(self.banana.name, "Banana")
        self.assertEqual(self.banana.weight, 100)
        self.assertEqual(self.banana.calories, 89)
        self.assertEqual(self.banana.carbs, 20.2)

    def test_property(self):
        """test that property work correctly"""
        command_list = ['self.banana.name = "Apple"',
                        'self.banana.weight = 200',
                        'self.banana.calories = 20',
                        'self.banana.carbs = 10']

        for command in command_list:
            with self.assertRaises(AttributeError):
                exec(command)

    def test_mul(self):
        """test that mul work correctly"""
        self.assertEqual(self.banana * 2, Food("Banana", 200, 178, 40.4))

    def test_reverse_mul(self):
        """test that reverse mul work correctly"""
        self.assertEqual(2 * self.banana, Food("Banana", 200, 178, 40.4))

    def test_str(self):
        """test that str function work correctly"""
        self.assertEqual(str(self.banana), "Banana (100g)")
