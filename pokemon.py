import requests

url = "https://pokeapi.co/api/v2/pokemon/"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

