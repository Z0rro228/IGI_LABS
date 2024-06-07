import requests


class JokeService:
    @staticmethod
    def get_random_joke():
        return requests.get('https://official-joke-api.appspot.com/random_joke').json()
