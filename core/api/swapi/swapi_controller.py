import requests

class SwapiController:
    def __init__(self, url="https://swapi.info/api/"):
        self.url = url

    def get_person(self, user_id):
        url = f"{self.url}/people/{user_id}/"
        return requests.get(url=url)