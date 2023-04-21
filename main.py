from utils.football_api import FootballData
from config.tokens import Tokens
from src.bot_src import client
from utils.functions.functions import getTable
tokens = Tokens()

client.run(tokens.bot_token)