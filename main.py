from utils.football_api import FootballData
from src.tokens import Tokens

tokens = Tokens()

football = FootballData(tokens.url, tokens.testing_key, "football-data\server_data.json")
football.fetch_data()