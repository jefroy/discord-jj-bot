# bot.py
import os
import discord
from dotenv import load_dotenv

load_dotenv()  # get context from .env
TOKEN = os.getenv('DISCORD_TOKEN')
print(TOKEN)

"""
client object represents a connection to discord.
handles events, tracks state, interacts with discord APIs
"""
client = discord.Client()

"""
client on_ready event handler
- handles the event when the Client has established a connection to Discord
and as finished preparing the data that discord has sent, such as:
    - login state
    - server/guild
    - channel data ,etc.
"""


@client.event
async def on_ready():
    print(f'{client.user} has connected!')


client.run(TOKEN)  # runs the client using the token
