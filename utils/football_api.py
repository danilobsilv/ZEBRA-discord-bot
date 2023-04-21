import requests
import json

class FootballData:
    def __init__(self, url, api_key, file_path):
        self.url = url
        self.api_key = api_key
        self.file_path = file_path
        self.headers = {"Authorization": f"Bearer {self.api_key}"} 


    def fetch_data(self):
        response = requests.get(self.url, headers = self.headers)
        data = json.loads(response.text)
        with open(self.file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)
            print("Escrito com sucesso!")

        return data
