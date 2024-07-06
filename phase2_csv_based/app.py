import streamlit as st
from recipes import RecipeManager

# Initialize Recipe Manager
recipe_manager = RecipeManager()

# Create a dictionary to map dish types to recipes
dish_types = {
    "Pizza": recipe_manager.pizza_recipes,
    "Bread": recipe_manager.bread_recipes,
    }

# Streamlit App
st.title('Recipe Manager')

# User selects a type of dish
dish_type = st.selectbox('Select a type of dish:', list(dish_types.keys()))

# Display the recipes for the selected dish type
if dish_type:
    recipes = dish_types[dish_type]
    recipe_names = [recipe.name for recipe in recipes]
    selected_recipe_name = st.selectbox(f'Select a {dish_type} recipe:', recipe_names)

    if selected_recipe_name:
        selected_recipe = next(recipe for recipe in recipes if recipe.name == selected_recipe_name)
        
        st.subheader(f'{selected_recipe.name} ({dish_type})')
        st.text(selected_recipe)
