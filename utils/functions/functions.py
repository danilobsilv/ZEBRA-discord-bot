import re
import requests
import json
# from config.tokens import Tokens

# tokens = Tokens()

def commands():
      pass

def sayOi(message):
    author_mention = message.author.mention
    return f"Oi, {author_mention},  como você tá?"


def getTabela():  # to do

      url = 'https://api.api-futebol.com.br/v1/campeonatos/10/tabela'

      
      headers = {'Authorization': f'Bearer {"live_2d712d4006ae19758252534d43d9ac"}'}
      # headers = tokens.api_key

      response = requests.get(url, headers=headers)


      tabela = response.json()


      with open("football-data\serieA_data.json", "w") as outfile:
            json.dump(tabela, outfile, indent=4)

getTabela()


