from .species import Species

class Animal:
    def __init__(self, id_: int, species: Species):
        self.id = id_
        self.species = species

    def __eq__(self, other):
        return self.id == other.id and self.species == other.species

    def __repr__(self):
        return f"{{id: {self.id}, species: {self.species.value}}}"

