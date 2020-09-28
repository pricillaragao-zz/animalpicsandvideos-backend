import os
import requests
from .Photo import Photo
from .repository import UnsplashRepository


class UnsplashService:
    def __init__(self, repository: UnsplashRepository):
        self.base_url = "https://api.unsplash.com"
        self.access_key = os.environ["UNSPLASH_ACCESS_KEY"]
        self.repository = repository

    def get_photo(self, animal_id: str) -> Photo:
        unsplash_id = self.repository.find_by_animal_id(animal_id)

        payload = {"client_id": self.access_key}

        url = f"{self.base_url}/photos/{unsplash_id}"

        response = requests.get(url, params=payload)

        response.raise_for_status()

        data = response.json()

        print(data)

        return Photo(data["urls"]["regular"])
