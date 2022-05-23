# Get the response data from the main file

import requests
import json

req = requests.get("https://swapi.dev/api/")
data = req.json()

routes: dict = {
    "people": data["people"],
    "planets": data["planets"],
    "films": data["films"],
    "species": data["species"],
    "vehicles": data["vehicles"],
    "starships": data["starships"]
}