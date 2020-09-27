from animalpicsandvideos.unsplash import UnsplashService
from .repository import AnimalsRepository


class AnimalsService:
    def __init__(
        self, repository: AnimalsRepository, unsplash_service: UnsplashService
    ):
        self.repository = repository
        self.unsplash_service = unsplash_service

    def get_animals(self):
        dog = self.repository.find_animal("0")
        photo = self.unsplash_service.get_photo(dog)
        dog.img_url = photo.img_url

        return [dog]
