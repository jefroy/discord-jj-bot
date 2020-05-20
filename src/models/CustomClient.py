import discord
import random
from models.Data import Data

"""
client object represents a connection to discord.
handles events, tracks state, interacts with discord APIs
"""


class CustomClient(discord.Client):  # inherit from discord.Client

    # CONSTRUCTOR
    def __init__(self):
        super().__init__()  # inherit from discord client object.
        self.data = Data()

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
        await member.dm_channel.send(self.data.get_welcome_msg(member.name))

    async def on_message(self, message):
        if message.author == self.user:  # prevent a loop of cancer
            return
        if message.content == '99!':
            response = random.choice(self.data.b99_quotes)
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

    # UTILITY

    def get_guilds(self):
        print(f'{self.user} is connected to the following guilds:\n')

        for guild in self.guilds:
            if guild.name == self.data.MYGUILD:
                print(f'{guild.name}(id: {guild.id})' + f' (my guild)')
            else:
                print(
                    f'{guild.name}(id: {guild.id})'
                )
            members_values = '\n - '.join([member.name for member in guild.members])
            self.data.DICT_MEMBERS[guild.name] = members_values
            # print(f'Guild Members:\n - {members}')

    def get_my_guildl(self):
        # return discord.utils.find(lambda g: g.name == GUILD, client.guilds)
        return discord.utils.get(self.guilds, name=self.data.MYGUILD)
