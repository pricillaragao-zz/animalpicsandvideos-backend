from typing import List
from animalpicsandvideos.unsplash import UnsplashService
from .repository import AnimalsRepository
from .animal import Animal


class AnimalsService:
    def __init__(
        self, repository: AnimalsRepository, unsplash_service: UnsplashService
    ):
        self.repository = repository
        self.unsplash_service = unsplash_service

    def get_animals(self) -> List[Animal]:
        animals = self.repository.list_animals()

        for animal in animals:
            photo = self.unsplash_service.get_photo(animal.id)
            animal.img_url = photo.img_url

        return animals
