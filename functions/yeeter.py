from bot import bot

class Yeeter:
    @bot.command('yeet')
    async def yeeter(ctx):
        print('yeeeter triggered')
        await ctx.send('YEET')