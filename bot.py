import os
import discord
from discord.ext import commands

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_SERVER')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@bot.command('yeet')
async def yeeter(ctx):
    print('yeeeter triggered')
    await ctx.send('YEET')
       


if __name__ == '__main__':
    bot.run(TOKEN)