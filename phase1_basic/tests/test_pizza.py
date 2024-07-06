import unittest
from pizza.pizza_recipes import get_pizza_recipes

class TestPizzaRecipes(unittest.TestCase):
    def test_get_pizza_recipes_returns_list(self):
        """Tests if the function returns a list."""
        self.assertIsInstance(get_pizza_recipes(), list)

    def test_get_pizza_recipes_includes_margherita(self):
        """Tests if the Margherita Pizza is included in the recipes."""
        recipes = get_pizza_recipes()
        self.assertTrue(any(recipe.name == "Margheritta Pizza" for recipe in recipes))

    def test_get_pizza_recipes_includes_pizza_tonno(self):
        """Testet, ob die Pizza Tonno in den Rezepten enthalten ist."""
        recipes = get_pizza_recipes()
        self.assertTrue(any(recipe.name == "Pizza Tonno" for recipe in recipes), "Pizza Tonno found in recipes")

if __name__ == '__main__':
    unittest.main()

