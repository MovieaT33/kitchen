from fastapi import FastAPI
from config.config import TITLE, VERSION
from pydantic import BaseModel

app = FastAPI(
    title=TITLE,
    version=VERSION
)


class Food(BaseModel):
    id: int
    name: str


foods: list[Food] = [
    Food(id=0, name="Apple"),
    Food(id=1, name="Banana")
]


@app.get("/foods/{food_id}")
async def get_food(food_id: int) -> list:
    return [food for food in foods if food.id == food_id]


@app.post("/food")
async def add_food(food: Food) -> dict:
    foods.append(food)
    return {"status": 200, "foods": foods}
