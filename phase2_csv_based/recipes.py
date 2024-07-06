import csv
from pizza.pizza import PizzaRecipe
from bread.bread import BreadRecipe
from ingredients import Ingredients
from instructions import Instructions
from oven import Oven

class RecipeManager:
    def __init__(self):
        self.pizza_recipes = self.load_pizza_recipes('pizza/pizza_recipes.csv')
        self.bread_recipes = self.load_bread_recipes('bread/bread_recipes.csv')
        
    def get_all_recipes(self):
        return self.pizza_recipes + self.bread_recipes

    def load_pizza_recipes(self, filepath):
        recipes = []
        with open(filepath, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                ingredients = Ingredients(row['dough'], row['sauce'], row['toppings'].split(', '))
                instructions = Instructions(row['preparation'], row['cooking'])
                oven = Oven(int(row['temperature']), int(row['time']))
                recipes.append(PizzaRecipe(row['name'], ingredients, instructions, oven))
        return recipes

    def load_bread_recipes(self, filepath):
        recipes = []
        with open(filepath, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                ingredients = Ingredients(row['dough'])
                instructions = Instructions(row['preparation'], row['cooking'])
                oven = Oven(int(row['temperature']), int(row['time']))
                recipes.append(BreadRecipe(row['name'], ingredients, instructions, oven))
        return recipes
