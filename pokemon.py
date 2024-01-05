import requests
import json

url = "https://pokeapi.co/api/v2/pokemon/"
pokemon_list = list()

while url != None:
    payload = {}
    headers = {}

    response = json.loads(requests.request("GET", url, headers=headers, data=payload).text)
    url = response ["next"]

    for item in response["results"]:
       pokemon_name = item["name"]
       url_pokemon = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
       response_pokemon = json.loads(requests.request("GET", url_pokemon, headers=headers, data=payload).text)

       pokemon_list.append(response_pokemon)
       print(response_pokemon["id"])


print(pokemon_list)

