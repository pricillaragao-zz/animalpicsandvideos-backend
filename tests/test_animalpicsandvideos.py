import json
from animalpicsandvideos import __version__, create_app, animalpicsandvideosJSONEncoder
from animalpicsandvideos.animals import Animal, Species


app = create_app()


def test_version():
    assert __version__ == "0.1.0"


def test_get_animals():
    with app.test_client() as test_client:
        # Arrange
        dog = Animal(0, Species.DOG)
        expected_result = json.dumps([dog], cls=animalpicsandvideosJSONEncoder)

        # Act
        response = test_client.get("/api/v1/animals", follow_redirects=True)

        # Assert
        assert json.loads(response.data.decode()) == json.loads(expected_result)
