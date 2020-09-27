import json
import requests
from animalpicsandvideos import __version__, create_app, animalpicsandvideosJSONEncoder


app = create_app()


def test_version():
    assert __version__ == "0.1.0"


def test_get_animals():
    with app.test_client() as test_client:
        # Act
        response = test_client.get("/api/v1/animals", follow_redirects=True)

        # Assert
        data = json.loads(response.data.decode())

        dog = data[0]

        assert dog["id"]
        assert dog["species"] == "dog"
        assert requests.get(dog["img_url"]).status_code == 200
