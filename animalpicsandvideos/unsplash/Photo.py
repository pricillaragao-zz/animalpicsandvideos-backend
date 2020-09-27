class Photo:
    def __init__(self, img_url: str):
        self._img_url = img_url

    @property
    def img_url(self):
        return self._img_url
