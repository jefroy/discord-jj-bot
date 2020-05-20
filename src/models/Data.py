import os
from dotenv import load_dotenv


class Data:

    def __init__(self):
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

    def get_welcome_msg(self, name):
        return str(
            f'Hi good day, whalecum 2 my server.\n'
            f'wait na... ent youse {name}??\n'
            f'heh. you kinda famous around these parts bruddaman, '
            f'buh doh worry, we go take good care of yuh ;) xoxo'
        )
