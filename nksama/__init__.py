from pyrogram import filters, Client
from redis import Redis
import os

help_message = []

# class bot(Client):
#     super().__init__(
#         'bot',
#                      api_id=os.environ.get('API_ID', '20533795'),
#                      api_hash=os.environ['API_HASH', 'f6cadf28523943f525e706e6ace8a250'],
#                      bot_token=os.environ['BOT_TOKEN', '7116566735:AAFOSx0aTLfpWpkM73OYjCypy6tUG4s6VfM'],
#                      plugins=dict(root=f"{__name__}/plugins"))

#     def add_cmd(module, help):
#         help_message.append({"Module_Name": module})
#         help.update({f"{module}_help": help})

bot = Client('bot',
             api_id=os.environ.get('API_ID', '20533795'),
             api_hash=os.environ['API_HASH', 'f6cadf28523943f525e706e6ace8a250'],
             bot_token=os.environ['BOT_TOKEN', '7116566735:AAFOSx0aTLfpWpkM73OYjCypy6tUG4s6VfM'],
             plugins=dict(root=f"{__name__}/plugins"))

PYRO_SESSION = os.environ['PYRO_SESSION', 'BQE5UiMAn3Lsbv-RvFd-fg5SFj_atrbjibKf5GBq_Sbbjd8MXJ7uG6ebLyubkv1JUgT6wzwxYTHRvGtsaqXQ_M7NA1KHy5FrDGEp3k33R8zD7bKlirgJ7lf6xhF9EkWJt7yBxCMiVZdRXBvGuk6KSYFVjS0yMLhrBu3ebSqLCHk079UVCsDglYRcPC8zH9kadQsGoCvgW_85_T1GWvsdmr2-VVWIaQ2JhcWqS_Iqw9uonqAAxFdW2bufPFGajeojKWVaE-R5Ss_DMVZtkp3_4kPQ9Y_ZAyVUybJJ4B2BVCu0dAm9wGGWLbpWEiOseJYEADihEfdDLS0JC-in4ydTx4x-zTdwcQAAAAF-Ni2lAA']

musicbot = Client(
    PYRO_SESSION,
    api_id=os.environ.get('API_ID', '20533795'),
    api_hash=os.environ['API_HASH', 'f6cadf28523943f525e706e6ace8a250'],
)
