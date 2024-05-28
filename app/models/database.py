import pickle
from pydantic import BaseModel
from fastapi.responses import ORJSONResponse
import os


class Food(BaseModel):
    id:          int
    name:        str
    description: str | None


class Foods:
    def __init__(self, foods: list[Food]) -> None:
        self.foods = foods

    def save(self, version: str) -> ORJSONResponse:
        try:
            with open(
                f"db/{os.path.basename(version)}_foods.pkl", "wb"
                    ) as file:
                pickle.dump(self.foods, file)

            return ORJSONResponse({"status": 200, "filename": file.name})
        except OSError:
            return ORJSONResponse({"status": 405})

    def load(self, version: str) -> ORJSONResponse:
        try:
            with open(
                f"db/{os.path.basename(version)}_foods.pkl", "rb"
                    ) as file:
                self.foods = pickle.load(file)

            return ORJSONResponse({"status": 200, "filename": file.name})
        except OSError:
            return ORJSONResponse({"status": 405})
