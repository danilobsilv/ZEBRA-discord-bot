from config.tokens import Tokens
from src.bot_src import client



if __name__ == "__main__":
      tokens = Tokens()

      client.run(tokens.bot_token)