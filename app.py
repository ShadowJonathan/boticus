# Python core imports
import os

# Third-party imports
import discord
from discord.ext import commands

# Local imports
from config.loader import config
from functions.weather import Weather

# Loading settings
TOKEN = config.get('DEFAULT', 'TOKEN')
GUILD = config.get('DEFAULT', 'SERVER')
client = discord.Client()
# bot = commands.Bot(command_prefix='!')

@client.event
async def on_message(message):
    if message.content.startswith('!weather'):
        _input: str = message.content[8:]
        _raw:str = _input.strip().split(',')
        _payload: dict = {'city': _raw[0], 'countryCode': _raw[1]}
        _weather = Weather()
        _data = _weather.get(_payload)

        await message.channel.send(_data)


if __name__ == '__main__':
    # bot.run(TOKEN)
    client.run(TOKEN)