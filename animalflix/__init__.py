__version__ = "0.1.0"


import animalflix.animals
from flask import Flask
from .json_encoder import AnimalFlixJSONEncoder


def create_app() -> Flask:
    app = Flask(__name__)
    app.json_encoder = AnimalFlixJSONEncoder

    app.register_blueprint(
        blueprint=animalflix.animals.api_v1, url_prefix="/api/v1/animals"
    )

    return app
