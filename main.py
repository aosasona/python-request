# Get data from API
import json
import requests
from utils.dir import routes


entry = input("What do you want to find in the amazing Star Wars archive? ")

if entry in routes:
    query = requests.get(routes[entry])
    data: dict = query.json()
    print(data)
elif entry not in routes:
    print(f"{entry} does not exist!")
