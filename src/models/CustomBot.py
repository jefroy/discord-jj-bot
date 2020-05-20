from discord.ext.commands import Bot
import os
import random
from dotenv import load_dotenv

"""
client object represents a connection to discord.
handles events, tracks state, interacts with discord APIs
"""


class CustomBot(Bot):  # inherit from discord.Client

    # CONSTRUCTOR
    def __init__(self):
        super().__init__(command_prefix='!')  # inherit from discord client object.
        # get context from .env
        load_dotenv()
        # get values from .env
        self.TOKEN = os.getenv('DISCORD_TOKEN')

    # EVENTS
    """
    client on_ready event handler
    - handles the event when the Client has established a connection to Discord
    and as finished preparing the data that discord has sent, such as:
        - login state
        - server/guild
        - channel data ,etc.
    """

    async def on_ready(self):
        print(f'{self.user.name} has connected! (bot)')

    # METHODS
    # ACCESSORS
    def get_token(self):
        return self.TOKEN

    # UTILITY
