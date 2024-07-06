import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_ingredients(data):
    ingredient_counts = data['ingredients'].str.split(',').explode().value_counts()
    return ingredient_counts

def plot_ingredient_counts(ingredient_counts):
    plt.figure(figsize=(10, 6))
    sns.barplot(x=ingredient_counts.head(10).values, y=ingredient_counts.head(10).index)
    plt.title('Top 10 Ingredients in Pizza Recipes')
    plt.xlabel('Frequency')
    plt.ylabel('Ingredients')
    plt.show()

