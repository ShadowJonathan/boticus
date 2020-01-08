import json
from datetime import datetime

# Third party imports
import requests

# Local Imports
from config.loader import config


class Weather:
    _base: str
    _key: str

    def __init__(self):
        self._base = config.get('WEATHER', 'BASE')
        self._key = config.get('WEATHER', 'API_KEY')

    def get(self, _payload):
        url: str  = "{}{},{},&APPID={}&units=metric".format(
            self._base,
            _payload['city'],
            _payload['countryCode'],
            self._key
        )
        response = json.loads(requests.get(url).text)
        
        # Preparing return_data
        try:
            area: str = response['name']
            temp_now: int = response['main']['temp']
            temp_feel: int = response['main']['feels_like']
            description: str = response['weather'][0]['description']
            wind: float = response['wind']['speed']
            gust: float = response['wind']['gust']
            deg: float = response['wind']['gust']
            sun_rise: datetime = datetime.fromtimestamp(response['sys']['sunrise'])
            sun_rise = sun_rise.strftime('%H:%M:%S')
            sun_set = datetime.fromtimestamp(response['sys']['sunset'])
            sun_set = sun_set.strftime('%H:%M:%S')
        except KeyError:
            return "Could not load weather data, errno weather-1"

        return_data: str = (
            '```md\n'
            f'# Forecast for {area}\n'
            f'- Temperature: \n'
            f'\t- Now: {temp_now}°C\n'
            f'\t- Feels like: {temp_feel}°C\n'
            '- Weather:\n'
            f'\t- {description}\n'
            '- Wind:\n'
            f'\t- Wind: {wind}m/s\n'
            f'\t- Gusts: {gust}m/s\n'
            '- Sun:\n'
            f'\t- Sunrise: {sun_rise}\n'
            f'\t- Sunset: {sun_set}\n'
            '```'
        )

        return return_data
