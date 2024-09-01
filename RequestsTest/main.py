import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'bf935ec66a97fb04ef778b27b00a1ba1'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

BODY_CREATE = {
    "name": "КУК",
    "photo_id": -1
}
BODY_RENAME = {
    "pokemon_id": "66038",
    "name": "BOBBY",
    "photo_id": 66
}
BODY_POKEBALL = { "pokemon_id": "66038" }

'''RESPONSE_CREATE = requests.post(url = f'{URL}/pokemons', headers = HEADER , json = BODY_CREATE)
print(RESPONSE_CREATE.text)'''

'''RESPONSE_POKEBALL = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER , json = BODY_POKEBALL)
print(RESPONSE_POKEBALL.text)'''

RESPONSE_RENAME = requests.put(url = f'{URL}/pokemons', headers = HEADER , json = BODY_RENAME)
print(RESPONSE_RENAME.json())