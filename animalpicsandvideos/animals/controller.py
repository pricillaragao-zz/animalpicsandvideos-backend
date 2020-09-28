import os
import psycopg2
from flask import jsonify
from animalpicsandvideos.unsplash import UnsplashService, UnsplashRepository
from . import api_v1
from .repository import AnimalsRepository
from .service import AnimalsService

DATABASE_URL = os.environ["DATABASE_URL"]

conn = psycopg2.connect(DATABASE_URL, sslmode="require")

unsplash_repository = UnsplashRepository(conn)

animals_service = AnimalsService(
    repository=AnimalsRepository(conn),
    unsplash_service=UnsplashService(unsplash_repository),
)


@api_v1.route("/")
def get_animals() -> str:
    return jsonify(animals_service.get_animals())
