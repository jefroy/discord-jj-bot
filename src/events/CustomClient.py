import discord


class CustomClient(discord.Client):
    def __init__(self):
        DICT_MEMBERS = {}

    async def on_ready(self):
        print(f'{self.user} has connected!')

    async def on_member_join(self, member):
        # working
        await member.create_dm()
        await member.dm_channel.send(
            f'Hi {member.name}, welcome to my Discord server!'
        )
