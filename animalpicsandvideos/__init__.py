__version__ = "0.1.0"


import animalpicsandvideos.animals
from flask import Flask
from flask_cors import CORS
from .json_encoder import AnimalPicsAndVideosJSONEncoder


def create_app() -> Flask:
    app = Flask(__name__)
    CORS(app)
    app.json_encoder = AnimalPicsAndVideosJSONEncoder

    app.register_blueprint(
        blueprint=animalpicsandvideos.animals.api_v1, url_prefix="/api/v1/animals"
    )

    return app
