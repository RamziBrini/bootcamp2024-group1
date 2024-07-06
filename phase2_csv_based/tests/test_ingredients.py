import unittest
from ingredients import Ingredients

class TestIngredients(unittest.TestCase):

    def test_ingredients_initialization(self):
        ingredients = Ingredients(dough="Basic dough", sauce="Tomato sauce", toppings=["Mozzarella", "Basil"])
        self.assertEqual(ingredients.dough, "Basic dough")
        self.assertEqual(ingredients.sauce, "Tomato sauce")
        self.assertEqual(ingredients.toppings, ["Mozzarella", "Basil"])

    def test_ingredients_initialization_without_toppings(self):
        ingredients = Ingredients(dough="Basic dough", sauce="Tomato sauce")
        self.assertEqual(ingredients.dough, "Basic dough")
        self.assertEqual(ingredients.sauce, "Tomato sauce")
        self.assertEqual(ingredients.toppings, [])

    def test_to_dict(self):
        ingredients = Ingredients(dough="Basic dough", sauce="Tomato sauce", toppings=["Mozzarella", "Basil"])
        expected_dict = {
            'dough': "Basic dough",
            'sauce': "Tomato sauce",
            'toppings': ["Mozzarella", "Basil"]
        }
        self.assertEqual(ingredients.to_dict(), expected_dict)

    def test_from_dict(self):
        data = {
            'dough': "Basic dough",
            'sauce': "Tomato sauce",
            'toppings': ["Mozzarella", "Basil"]
        }
        ingredients = Ingredients.from_dict(data)
        self.assertEqual(ingredients.dough, "Basic dough")
        self.assertEqual(ingredients.sauce, "Tomato sauce")
        self.assertEqual(ingredients.toppings, ["Mozzarella", "Basil"])

if __name__ == '__main__':
    unittest.main()
