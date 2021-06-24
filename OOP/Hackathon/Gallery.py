class Gallery:
    def __init__(self, client_name, photos=[]):
        self.client_name = client_name
        self.photos = photos

    def display(self):
        print(f"Gallery owner: {self.client_name}")
        print(f"Photos:")
        for photo in self.photos:
            print(f"{photo.filename}")