import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'bf935ec66a97fb04ef778b27b00a1ba1'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '4758' 

def test_status_code():
    response = requests.get(url=f'{URL}/pokemons',params= {'trainer_id' : TRAINER_ID} )
    assert response.status_code == 200 

def test_part_of_response():
    response_name = requests.get(url=f'{URL}/pokemons',params= {'trainer_id' : TRAINER_ID} )
    assert response_name.json()["data"][0]["trainer_id"] == "4758"