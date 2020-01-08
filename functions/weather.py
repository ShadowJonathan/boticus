# Third party imports
import requests

# Local Imports
from config.loader import config


class Weather:
    _base: str

    def __init__(self):
        self._base = config.get('WEATHER', 'BASE')

    def get(self, city, countryCode):
        return requests.get(f"{self._base}{city},{countryCode}")
