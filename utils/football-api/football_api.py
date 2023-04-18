import requests
import json

# defining the json file path
file_path = "football-data\server_data.json"

# defining the api url
url = "https://api.api-futebol.com.br/v1/campeonatos/10"

# setting the header with the api key
testing_header = {
    "Authorization": "Bearer MY_TESTING_API_KEY"
}

# this is the live version of the server, use it when the app is running
headers = {
    "Authorization": "Bearer MY_LIVE_API_KEY"
}

# getting the data from the server
response = requests.get(url, headers=testing_header)

# decoding the response
data = json.loads(response.text)

# saving the data in the json file
with open(file_path, "w") as arquivo:
    json.dump(data, arquivo, indent=4)
    print("Dados salvos com sucesso em dados.json")

#function that will be set to get the data when requested to 
async def get_response(context): 
    pass