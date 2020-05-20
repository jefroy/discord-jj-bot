import discord
import os
import random
from dotenv import load_dotenv

"""
client object represents a connection to discord.
handles events, tracks state, interacts with discord APIs
"""


class CustomClient(discord.Client):  # inherit from discord.Client

    # CONSTRUCTOR
    def __init__(self):
        super().__init__()  # inherit from discord client object.
        # get context from .env
        load_dotenv()
        # get values from .env
        self.TOKEN = os.getenv('DISCORD_TOKEN')
        self.MYGUILD = os.getenv('DISCORD_GUILD')
        self.DICT_MEMBERS = {}
        self.b99_quotes = [
            'I\'m the human form of the 💯 emoji.',
            'Bingpot!',
            'Cool. Cool cool cool cool cool cool cool,',
            'no doubt no doubt no doubt no doubt.'
        ]

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
        print(f'{self.user} has connected!')

    async def on_member_join(self, member):
        # working
        await member.create_dm()
        await member.dm_channel.send(
            f'Hi good day, whalecum 2 my server.\n'
            f'wait na.. ent youse {member.name}??\n'
            f'heh. you kinda famous around these parts bruddaman,'
            f'buh doh worry, we go take good care of yuh ;) xoxo'
        )

    async def on_message(self, message):
        if message.author == self.user: # prevent a loop of cancer
            return
        if message.content == '99!':
            response = random.choice(self.b99_quotes)
            await message.channel.send(response)
        elif message.content == 'raise-exception':
            raise discord.DiscordException
        if 'happy birthday' in message.content.lower():
            await message.channel.send('Happy Birthday! 🎈🎉')

    async def on_error(self, event, *args, **kwargs):
        with open('err.log', 'a') as f:
            if event == 'on_message':
                f.write(f'Unhandled message: {args[0]}\n')
            else:
                raise


    # METHODS
    # ACCESSORS
    def get_dict_members(self):
        return self.DICT_MEMBERS

    def get_token(self):
        return self.TOKEN

    def get_my_guild(self):
        return self.MYGUILD

    # UTILITY

    def get_guilds(self):
        print(f'{self.user} is connected to the following guilds:\n')

        for guild in self.guilds:
            if guild.name == self.MYGUILD:
                print(f'{guild.name}(id: {guild.id})' + f' (my guild)')
            else:
                print(
                    f'{guild.name}(id: {guild.id})'
                )
            members_values = '\n - '.join([member.name for member in guild.members])
            self.DICT_MEMBERS[guild.name] = members_values
            # print(f'Guild Members:\n - {members}')

    def get_my_guildl(self):
        # return discord.utils.find(lambda g: g.name == GUILD, client.guilds)
        return discord.utils.get(self.guilds, name=self.MYGUILD)
