class Animal:
    def __init__(self, id_: str, species: str, img_url: str = None):
        self._id = id_
        self._species = species
        self._img_url = img_url

    @property
    def id(self):
        return self._id

    @property
    def species(self):
        return self._species

    @property
    def img_url(self):
        return self._img_url

    @img_url.setter
    def img_url(self, img_url: str):
        self._img_url = img_url

    def __eq__(self, other):
        return self.id == other.id
