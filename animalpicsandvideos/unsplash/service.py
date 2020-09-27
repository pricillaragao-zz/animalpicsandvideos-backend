import os
import requests
from animalpicsandvideos.animals import Animal, Species
from .Photo import Photo


class UnsplashService:
    def __init__(self):
        self.base_url = "https://api.unsplash.com"
        self.access_key = os.environ["UNSPLASH_ACCESS_KEY"]

    def get_photo(self, animal: Animal) -> Photo:
        payload = {"client_id": self.access_key}

        url = f"{self.base_url}/photos/{self._get_unsplash_id(animal)}"

        response = requests.get(url, params=payload)

        response.raise_for_status()

        data = response.json()

        print(data)

        return Photo(data["urls"]["regular"])

    def _get_unsplash_id(self, animal: Animal) -> str:
        if animal.species == Species.DOG:
            return "sXU6BeWoZqI"
        else:
            raise ValueError(f"species {animal.species} not found")
