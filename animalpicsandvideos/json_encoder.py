from flask.json import JSONEncoder
from animalpicsandvideos.animals import Animal


class animalpicsandvideosJSONEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, Animal):
            return {"id": o.id, "species": o.species.value}
        return super(animalpicsandvideosJSONEncoder, self).default(o)
