from fastapi import FastAPI
from config import TITLE, VERSION
from models.database import Foods, Food
from fastapi.responses import ORJSONResponse

app = FastAPI(
    title=TITLE,
    version=VERSION
)

foods: Foods = Foods([])


@app.post("/foods")
async def add_food(new_food: Food) -> dict:
    foods.foods.append(new_food)
    return {"status": 201, "data": foods.foods}


@app.get("/foods")
async def get_foods() -> dict:
    return {"status": 200, "data": foods.foods}


@app.get("/foods/{food_id}")
async def get_food(food_id: int) -> dict:
    return {"status": 200,
            "data": [food for food in foods.foods if food.id == food_id]}


@app.patch("/foods/{food_id}")
async def update_food(food_id: int, new_food: Food) -> dict:
    for i, food in enumerate(foods.foods):
        if food.id == food_id:
            foods.foods[i] = new_food
            return {"status": 200, "data": foods.foods}
    return {"status": 404}


@app.delete("/foods/{food_id}")
async def delete_food(food_id: int) -> dict:
    for food in foods.foods:
        if food.id == food_id:
            foods.foods.remove(food)
            return {"status": 200, "data": foods.foods}
    return {"status": 404}


@app.post("/foods/save", response_class=ORJSONResponse)
async def save(version: str) -> ORJSONResponse:
    return foods.save(version)


@app.post("/foods/load", response_class=ORJSONResponse)
async def load(version: str) -> ORJSONResponse:
    return foods.load(version)
