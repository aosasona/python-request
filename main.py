# Get data from API
import json
import requests

query = requests.get("https://swapi.dev/api/")

data = query.json()

print(data)