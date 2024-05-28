from fastapi import FastAPI
from config import TITLE, VERSION
from models.database import Foods, Food

app = FastAPI(
    title=TITLE,
    version=VERSION
)

foods: Foods = Foods([
    Food(id=0, name="Apple"),
    Food(id=1, name="Banana")
])


@app.post("/food")
async def add_food(food: Food) -> dict:
    foods.foods.append(food)
    return {"status": 200, "foods": foods.foods}


@app.get("/foods")
async def get_foods() -> list:
    return foods.foods


@app.get("/foods/{food_id}")
async def get_food(food_id: int) -> list:
    return [food for food in foods.foods if food.id == food_id]


@app.delete("/food")
async def delete_food(food_id: int) -> dict:
    for food in foods.foods:
        if food.id == food_id:
            foods.foods.remove(food)
            return {"status": 200, "foods": foods.foods}
    return {"status": 404}


@app.post("/save")
async def save(version: str) -> dict:
    return foods.save(version)


@app.post("/load")
async def load(version: str) -> dict:
    return foods.load(version)
