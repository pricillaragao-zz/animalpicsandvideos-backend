from flask.json import JSONEncoder
from animalpicsandvideos.animals import Animal


class AnimalPicsAndVideosJSONEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, Animal):
            return {"id": o.id, "species": o.species, "img_url": o.img_url}
        return super(AnimalPicsAndVideosJSONEncoder, self).default(o)
