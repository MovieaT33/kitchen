import pickle
from pydantic import BaseModel


class Food(BaseModel):
    id: int
    name: str


class Foods:
    def __init__(self, foods: list[Food]) -> None:
        self.foods = foods

    def save(self, version: str) -> dict:
        try:
            with open(f"db/{version}_foods.pkl", "wb") as file:
                pickle.dump(self.foods, file)

            return {"status": 200}
        except OSError:
            return {"status": 405}

    def load(self, version: str) -> dict:
        try:
            with open(f"db/{version}_foods.pkl", "rb") as file:
                self.foods = pickle.load(file)

            return {"status": 200}
        except OSError:
            return {"status": 405}
