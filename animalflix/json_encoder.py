from flask.json import JSONEncoder
from animalflix.animals import Animal


class AnimalFlixJSONEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, Animal):
            return {"id": o.id, "species": o.species.value}
        return super(AnimalFlixJSONEncoder, self).default(o)
