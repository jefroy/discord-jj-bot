import random
from discord.ext import commands

from models.Data import Data

data = Data()
bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='99')
async def nine_nine(ctx):
    response = random.choice(data.b99_quotes)
    await ctx.send(response)


@bot.command(name='kirsten')
async def kirsten(ctx):
    response = random.choice(data.kirsten_quotes)
    await ctx.send(response)


@bot.command(name='dinesh')
async def dinesh(ctx):
    response = random.choice(data.dinesh_quotes)
    await ctx.send(response)


bot.run(data.TOKEN)
