import requests
import json

# código estruturado 
"""
# defining the json file path
file_path = "football-data\server_data.json"

# defining the api url
url = "xxx"

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
"""

# versão orientada a objeto
class FootballData:
    def __init__(self, url, api_key, file_path):
        self.url = url
        self.api_key = api_key
        self.testing_key = ""
        self.file_path = file_path
        self.headers = {"Authorization": f"Bearer {self.api_key}"} 
        self.testing_headers = {"Authorization": f"Bearer {self.testing_key}"}


    def fetch_data(self):
        response = requests.get(self.url, headers = self.testing_headers)
        data = json.loads(response.text)
        with open(self.file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)
            print("Escrito com sucesso!")

        return data
