from ingredients import Ingredients
from instructions import Instructions
from oven import Oven

class BreadRecipe:
    def __init__(self, name, ingredients, instructions, oven):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.oven = oven

    def __str__(self):
        return (f"{self.name}\nIngredients: {self.ingredients}\n"
                f"Instructions: {self.instructions}\nOven: {self.oven}")

    def to_dict(self):
        return {
            'name': self.name,
            'ingredients': self.ingredients.to_dict(),
            'instructions': self.instructions.to_dict(),
            'oven': self.oven.to_dict()
        }

    @classmethod
    def from_dict(cls, data):
        ingredients = Ingredients.from_dict(data['ingredients'])
        instructions = Instructions.from_dict(data['instructions'])
        oven = Oven.from_dict(data['oven'])
        return cls(data['name'], ingredients, instructions, oven)
