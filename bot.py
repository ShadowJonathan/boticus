import os
import discord
from discord.ext import commands

# Local imports
from config.loader import config
from functions import yeeter

# Loading settings
TOKEN = config.get('DEFAULT', 'TOKEN')
GUILD = config.get('DEFAULT', 'SERVER')

# Setting up bot
bot = commands.Bot(command_prefix='!')

# @bot.event
# async def on_ready():
#     for guild in bot.guilds:
#         if guild.name == GUILD:
#             break

#     print(
#         f'{bot.user} is connected to the following guild:\n'
#         f'{guild.name}(id: {guild.id})'
#     )

# @bot.command('yeet')
# async def yeeter(ctx):
#     print('yeeeter triggered')
#     await ctx.send('YEET')
       


if __name__ == '__main__':
    yeeter.Yeeter(bot)
    bot.run(TOKEN)  # Run the bot