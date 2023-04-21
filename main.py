from utils.football_api import FootballData
from config.tokens import Tokens
from src.bot_src import client

from utils.functions.functions import getTabela
tokens = Tokens()

# BOT_URL = tokens.url
# TESTING_KEY = tokens.testing_key

# football = FootballData(BOT_URL, TESTING_KEY, "football-data\server_data.json")
# football.fetch_data()
# getTabela()
client.run(tokens.bot_token)