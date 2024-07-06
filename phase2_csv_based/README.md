**Task Instructions: Adding a Pizza Recipe to pizza_recipe.csv**

Welcome to your task! In this task, you will be adding a new pizza recipe to the `pizza-recipe.csv` file. Follow the instructions below to create a new branch, add your recipe, and push your changes to GitHub. Finally, you will create a pull request to merge your changes into the main branch.

**Step 1: Create a New Branch**

1. Open your terminal.
2. Navigate to your project directory.

```sh
cd phase2_csv_based/pizza
```

3. Create a new branch for your changes.

```sh
git checkout -b add-new-pizza-recipe
```

**Step 2: Add Your Recipe to pizza_recipe.csv**

1. Open `pizza-recipe.csv` in your preferred text editor or IDE.
2. Add a new row with your pizza recipe details. Follow the format of the existing rows. For example:

```lua
name,dough,sauce,toppings,preparation,cooking,temperature,time
BBQ Bacon,Basic dough,BBQ sauce,"Mozzarella, Bacon, Red Onion, Cilantro","Spread BBQ sauce, add toppings.","Bake for 12-15 minutes.",230,14
```

3. Save the file.

**Step 3: Stage Your Changes**

1. Check the status of your working directory to see the changes.

```sh
git status
```

2. Stage the changes to `pizza_recipe.csv`.

```sh
git add pizza_recipe.csv
```

**Step 4: Commit Your Changes**

1. Commit the changes with a meaningful message.

```sh
git commit -m "Add BBQ Bacon pizza recipe"
```

**Step 5: Push Your Changes**

1. Push your branch to the remote repository on GitHub.

```sh
git push origin add-new-pizza-recipe
```

**Step 6: Create a Pull Request**

1. Go to your repository on GitHub.
2. You will see a prompt to create a pull request for your recently pushed branch. Click on "Compare & pull request".
3. Provide a meaningful title and description for your pull request.
4. Click "Create pull request".

**Step 7: Review and Merge**

1. Notify your team or project maintainer to review your pull request.
2. Once approved, your pull request will be merged into the main branch.

Congratulations! You have successfully added a new pizza recipe to `pizza_recipe.csv` and followed the process to create a branch, make changes, and create a pull request on GitHub.

If you have any questions or run into any issues, please feel free to reach out for help. Happy coding!

