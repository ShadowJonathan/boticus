# Python core imports

# Third-party imports
from discord.ext import commands

# Local imports
from config.loader import config

# Loading settings
TOKEN = config.get('DEFAULT', 'TOKEN')
GUILD = config.get('DEFAULT', 'SERVER')

bot = commands.Bot(command_prefix='!')

bot.load_extension("cogs.weather")

if __name__ == '__main__':
    bot.run(TOKEN)
    # client.run(TOKEN)
