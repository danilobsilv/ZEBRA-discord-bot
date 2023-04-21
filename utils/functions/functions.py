import requests
import json


def commands():
      pass

def sayOi():  # to trigger "#oi"
      return f"Oi, como você tá?"

def getTabela():

      url = 'https://api.api-futebol.com.br/v1/campeonatos/10/tabela'

      headers = {'Authorization': f'Bearer {"live_2d712d4006ae19758252534d43d9ac"}'}

      response = requests.get(url, headers=headers)

      tabela = response.json()

      with open("football-data\serieA_data.json", "w") as outfile:
            json.dump(tabela, outfile, indent=4)

