from flask import jsonify
from animalpicsandvideos.unsplash import UnsplashService
from . import api_v1
from .repository import AnimalsRepository
from .service import AnimalsService

animals_service = AnimalsService(
    repository=AnimalsRepository(), unsplash_service=UnsplashService()
)


@api_v1.route("/")
def get_animals() -> str:
    return jsonify(animals_service.get_animals())
