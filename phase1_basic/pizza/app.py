import streamlit as st
from pizza_recipes import get_pizza_recipes

# Streamlit App
st.title('Simple Recipe Manager')

# Load hardcoded recipes
recipes = get_pizza_recipes()

# User selects a recipe to view details
recipe_names = [recipe.name for recipe in recipes]
selected_recipe_name = st.selectbox('Select a Pizza Recipe:', recipe_names)

if selected_recipe_name:
    selected_recipe = next(recipe for recipe in recipes if recipe.name == selected_recipe_name)
    st.subheader(f'{selected_recipe.name}')
    st.text(selected_recipe)