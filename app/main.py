from fastapi import FastAPI

app = FastAPI()

foods: list[dict] = [
    {"id": 0, "name": "Apple"}
]


@app.get("/food/{food_id}")
def get_food(food_id: int) -> dict:
    return [food for food in foods if food == food_id][0]
