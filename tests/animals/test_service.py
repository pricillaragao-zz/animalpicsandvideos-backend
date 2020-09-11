from animalflix.animals import service
from animalflix.animals.animal import Animal
from animalflix.animals.species import Species


def test_get_animals():
    # Arrange
    dog = Animal(0, Species.DOG)
    expected_result = [dog]

    # Act
    result = service.get_animals()

    # Assert
    assert result == expected_result
