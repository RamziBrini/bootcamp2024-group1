class PizzaRecipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

    def __str__(self):
        ingredients_str = "\n".join(self.ingredients)
        return f"{self.name}\n\nIngredients:\n{ingredients_str}\n\nInstructions:\n{self.instructions}"

# Hardcoded Pizza Recipe
margherita = PizzaRecipe(
    name="Margherita Pizza",
    ingredients=["Dough", "Tomato Sauce", "Mozzarella Cheese", "Basil"],
    instructions="1. Prepare the dough.\n2. Spread tomato sauce on the dough.\n3. Add mozzarella cheese.\n4. Bake at 250°C for 10-15 minutes.\n5. Garnish with basil leaves."
)

# Function to get all hardcoded recipes
def get_pizza_recipes():
    return [margherita]

def main():
    recipes = get_pizza_recipes()
    for recipe in recipes:
        print(recipe)

if __name__ == "__main__":
    main()
