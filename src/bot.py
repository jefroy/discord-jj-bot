# bot.py
import os
import discord
from dotenv import load_dotenv

from events.CustomClient import CustomClient

# get context from .env
load_dotenv()
# get values from .env
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

"""
client object represents a connection to discord.
handles events, tracks state, interacts with discord APIs
"""
# client = discord.Client()

"""
client on_ready event handler
- handles the event when the Client has established a connection to Discord
and as finished preparing the data that discord has sent, such as:
    - login state
    - server/guild
    - channel data ,etc.
"""

DICT_MEMBERS = {}


def get_guilds():
    dict_members = {}
    print(f'{client.user} is connected to the following guilds:\n')

    for guild in client.guilds:
        if guild.name == GUILD:
            print(f'{guild.name}(id: {guild.id})' + f' (my guild)')
        else:
            print(
                f'{guild.name}(id: {guild.id})'
            )
        members_values = '\n - '.join([member.name for member in guild.members])
        dict_members[guild.name] = members_values
        # print(f'Guild Members:\n - {members}')
    global DICT_MEMBERS
    DICT_MEMBERS = dict_members



def get_my_guild():
    # return discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    return discord.utils.get(client.guilds, name=GUILD)

print('members dictionary = ', DICT_MEMBERS)


client = CustomClient()
client.run(TOKEN)  # runs the client using the token
