from flask import jsonify
from . import api_v1
from .service import AnimalsService


@api_v1.route("/")
def get_animals() -> str:
    return jsonify(AnimalsService.get_animals())
