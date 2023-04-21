import requests
import json
from config.tokens import Tokens

tokens = Tokens()

def commands():
      pass

def sayOi(message):
    author_mention = message.author.mention
    return f"Oi, {author_mention},  como você tá?"


def getTable():
    url = 'https://api.api-futebol.com.br/v1/campeonatos/10/tabela'
    headers = {'Authorization': f'Bearer {tokens.api_key}'}
    response = requests.get(url, headers=headers)
    table = response.json()

    with open("football-data\serieA_data.json", "w") as outfile:
        json.dump(table, outfile, indent=4)

    formatted_table = ""
    for team in table:
        popular_name = team['time']['nome_popular']
        position = team['posicao']
        points = team['pontos']
        row = '{:2}º    {} -- {} pontos\n'.format(position, popular_name, points)
        formatted_table += row

    return formatted_table
