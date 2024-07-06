Pandas is a powerful Python library used for data manipulation and analysis. It provides flexible data structures and powerful tools to work with structured data. One of the core data structures in Pandas is the DataFrame, which is akin to a table or spreadsheet with rows and columns.

# Preparation 
install the necessary libraries:

```
pip install -r requirements.txt
```

# Instructions

To start Jupyter Notebook, you can run the following command in your terminal:
```
jupyter notebook --ip 0.0.0.0 --no-browser --allow-root
```

This command will start the Jupyter Notebook server and make it accessible on all network interfaces (`--ip 0.0.0.0`). It will also disable opening a web browser automatically (`--no-browser`) and allow running the server with root privileges (`--allow-root`).

Once the server is running, you can access the Jupyter Notebook interface by opening a web browser and navigating to the provided URL.

Copy the access token and open browser

![grafik](https://github.com/RamziBrini/bootcamp2024/assets/8480566/ab090f1a-b5d5-446e-9f47-eb0ef329d0ca)

Paste the access token

![grafik](https://github.com/RamziBrini/bootcamp2024/assets/8480566/9dbc531c-3451-4a4a-93e0-93c3859b0822)



In this repository, you will find two notebooks:

1. `data_exploration.ipynb`: This notebook provides a few commands to explore the data.

2. `data_analysis.ipynb`: This notebook provides a way to connect two tables (also known as data frames) with simple merge operations. It also shows how to visualize data.

## Reading and Presenting Pizza Recipes in Pandas

This documentation describes how to read and present a CSV file containing pizza recipes using the `pandas` library in Python.

### CSV File Format

The CSV file contains information about various pizza recipes. Below is an example of the file structure:

```csv
name,dough,sauce,toppings,preparation,cooking,temperature,time
Margherita,Basic dough,Tomato sauce,"Mozzarella, Basil","Roll out dough, spread sauce, add toppings.","Bake for 10-12 minutes.",220,12
Pepperoni,Basic dough,Tomato sauce,"Mozzarella, Pepperoni","Roll out dough, spread sauce, add toppings.","Bake for 10-12 minutes.",220,12
```

### Reading the CSV File with Pandas

To read the CSV file, we use the pandas library, which provides powerful data manipulation and analysis tools.
Step-by-Step Instructions

    1. Import the pandas library: Ensure you have pandas installed in your environment. You can install it using pip install pandas if not already installed.

    2. Read the CSV file: Use the pandas.read_csv function to read the CSV file into a DataFrame.

    3. Display the DataFrame: Use various pandas functions to display and analyze the data.

Example Code

```python
import pandas as pd
```
### Read the CSV file into a DataFrame

```python
df = pd.read_csv('path/to/your/csv/pizza_recipes.csv')
```

### Display the DataFrame

```python
print(df)
```

Output
The output will be a pandas DataFrame displaying the pizza recipes:

```sql
        name        dough         sauce                toppings                     preparation               cooking  temperature  time
0  Margherita  Basic dough  Tomato sauce      Mozzarella, Basil  Roll out dough, spread sauce, add toppings.  Bake for 10-12 minutes.         220    12
1   Pepperoni  Basic dough  Tomato sauce  Mozzarella, Pepperoni  Roll out dough, spread sauce, add toppings.  Bake for 10-12 minutes.         220    12
```
### Analyzing the Data

You can perform various operations on the DataFrame to analyze the pizza recipes. For example:

View the first few rows:

```python
print(df.head())
```

Describe the dataset:

```python
print(df.describe())
```

Filter pizzas by baking temperature:

```python
hot_pizzas = df[df['temperature'] > 220]
print(hot_pizzas)
```

Group by sauce type:

```python
grouped = df.groupby('sauce').size()
print(grouped)
```

## Visualizing Data Using Pandas

Pandas integrates well with data visualization libraries like Matplotlib and Seaborn. This allows you to create a variety of plots directly from your DataFrames. Here are some examples of what you can do:

1. **Bar Plots**:

```python
import matplotlib.pyplot as plt
import pandas as pd
# Sample DataFrame
data = {
    'name': ['Margherita', 'Pepperoni', 'BBQ Chicken'],
    'total_calories': [540, 820, 890]
}
df = pd.DataFrame(data)

    # Plotting a bar chart
df.plot(kind='bar', x='name', y='total_calories', legend=False)
plt.ylabel('Total Calories')
plt.title('Total Calories in Different Pizzas')
plt.show()
```

![grafik](https://github.com/RamziBrini/bootcamp2024/assets/8480566/8227280b-0ebf-4ac3-82c7-115e41bd1936)

2. **Pie Charts**:

```python
import matplotlib.pyplot as plt
import pandas as pd
# Sample DataFrame
data = {
    'ingredient': ['Dough', 'Sauce', 'Toppings'],
    'calories': [200, 50, 290]
}
df = pd.DataFrame(data)

# Plotting a pie chart
df.set_index('ingredient').plot.pie(y='calories', autopct='%1.1f%%')
plt.title('Calories Distribution in a Pizza')
plt.ylabel('')
plt.show()
```

![grafik](https://github.com/RamziBrini/bootcamp2024/assets/8480566/5c1c1c87-e1d2-4e53-8ab2-de4f44453263)

3. **Histograms**:

```python
import matplotlib.pyplot as plt
import pandas as pd
# Sample DataFrame
 # Sample DataFrame
data = {
   'name': ['Margherita', 'Pepperoni', 'BBQ Chicken', 'Vegetarian', 'Hawaiian'],
   'total_calories': [540, 820, 890, 410, 650]
}
df = pd.DataFrame(data)

# Plotting a histogram
df['total_calories'].plot(kind='hist', bins=5, edgecolor='black')
plt.xlabel('Total Calories')
plt.title('Distribution of Total Calories in Pizzas')
plt.show()
```
![grafik](https://github.com/RamziBrini/bootcamp2024/assets/8480566/c4ca539c-bf53-42bf-bff7-8b83e2299d89)


Conclusion

Using pandas to read and present the CSV file provides a simple yet powerful way to analyze and manipulate the pizza recipes data. You can further extend this analysis by adding more complex operations and visualizations.
