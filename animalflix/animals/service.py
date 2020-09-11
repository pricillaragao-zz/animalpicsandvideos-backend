from typing import List
from .animal import Animal
from .species import Species

def get_animals() -> List[Animal]:
    dog = Animal(0, Species.DOG)

    return [dog]
