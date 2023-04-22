import requests
import json
from config.tokens import Tokens

tokens = Tokens()

def commands():
    formated_row = ""
    with open("config\commands.txt" ,'r') as arquivo:
        linhas = arquivo.readlines()
    commands_list =  [linha.strip() for linha in linhas]

    for command in commands_list:
        formated_row += command+"\n"
    return formated_row



def sayOi(message):
    author_mention = message.author.mention
    return f"Oi, {author_mention},  como você tá?"


def getTable():
    headers = {'Authorization': f'Bearer {tokens.api_key}'}
    response = requests.get(tokens.table_endpoint, headers=headers)
    table = response.json()

    with open("football-data\serieA_tabela.json", "w") as table_file:
        json.dump(table, table_file, indent=4)

    formatted_table = ""
    for team in table:
        popular_name = team['time']['nome_popular']
        position = team['posicao']
        points = team['pontos']
        row = '{:2}º    {} -- {} pontos\n'.format(position, popular_name, points)
        formatted_table += row

    return formatted_table

def getTopScorers():
    headers = {"Authorization": f"Bearer {tokens.api_key}"}
    response = requests.get(tokens.topscorers_endpoint, headers=headers)
    table = response.json()

    with open("football-data\serieA_artilharia.json", "w") as topscorers_file:
        json.dump(table, topscorers_file, indent=4)

    
