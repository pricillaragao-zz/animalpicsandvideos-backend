import json
import requests
from animalpicsandvideos import __version__, create_app


app = create_app()


def test_version():
    assert __version__ == "0.1.0"


def test_get_animals():
    with app.test_client() as test_client:
        # Act
        response = test_client.get("/api/v1/animals", follow_redirects=True)

        # Assert
        animals = json.loads(response.data.decode())

        for animal in animals:
            assert animal["id"]
            assert animal["species"]

            img_url = animal["img_url"]

            assert img_url
            assert requests.get(img_url).status_code == 200
