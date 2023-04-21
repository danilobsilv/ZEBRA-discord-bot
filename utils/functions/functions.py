import requests
import json


def commands():
      pass

def sayOi():  # to trigger "#oi"
      return f"Oi, como você tá?"

def getTabela():

      url = 'https://api.api-futebol.com.br/v1/campeonatos/10/tabela'

      # Substitua {sua_chave_de_acesso} pela chave de acesso fornecida pela API
      headers = {'Authorization': f'Bearer {"live_2d712d4006ae19758252534d43d9ac"}'}

      # Faz a solicitação GET para a API
      response = requests.get(url, headers=headers)

      # Analisa a resposta JSON
      tabela = response.json()

      # Escreve a tabela em um arquivo JSON
      with open("football-data\serieA_data.json", "w") as outfile:
            json.dump(tabela, outfile, indent=4)

      # Faça o que desejar com a tabela obtida
      print(tabela)



