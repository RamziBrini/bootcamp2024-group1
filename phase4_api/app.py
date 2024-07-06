from fastapi import FastAPI, HTTPException
import csv

app = FastAPI()

# Load pizza data from CSV
def load_pizzas_from_csv():
    pizzas = []
    with open('data/pizzas.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            pizzas.append(row)
    return pizzas

pizzas_data = load_pizzas_from_csv()

# Define endpoints
@app.get("/")
def read_root():
    return {"message": "Welcome to the Pizza API"}

@app.get("/pizzas/")
def read_pizzas():
    return pizzas_data

@app.get("/pizza/{name}")
def read_pizza(name: str):
    for pizza in pizzas_data:
        if pizza['name'] == name:
            return pizza
    raise HTTPException(status_code=404, detail="Pizza not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
