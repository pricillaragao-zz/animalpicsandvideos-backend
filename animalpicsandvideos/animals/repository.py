from .animal import Animal
from .species import Species


class AnimalsRepository:
    @staticmethod
    def find_animal(id_: str) -> Animal:
        if id_ == "0":
            return Animal(id_, Species.DOG)
        else:
            raise ValueError(f"id {id_} not found")
