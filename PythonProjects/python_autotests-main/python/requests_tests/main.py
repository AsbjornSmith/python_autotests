import requests

URL='https://api.pokemonbattle.ru/v2'
TOKEN='da90db636fdeb79b9098bc8f40f207ab'
HEADER={'Content-Type':'application/json', 'trainer_token':TOKEN}

body_create={
    "name": "Бульбазавр",
    "photo_id": 12
}

response_create=requests.post(url=f'{URL}/pokemons', headers=HEADER, json= body_create)
print(response_create.text)

pokemon_id=response_create.json()['id']

body_change={
    "pokemon_id": pokemon_id,
    "name": "Чармандер",
    "photo_id": 23
}

response_change=requests.put(url=f'{URL}/pokemons', headers=HEADER, json= body_change)
print(response_change.text)

body_catch={
    "pokemon_id": pokemon_id
}

response_catch=requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json= body_change)
print(response_catch.text)

response_list=requests.get(url=f'{URL}/pokemons', headers=HEADER, params={'in_pokeball':1})

enemy_id=response_list.json()['data'][3]['id']

body_battle={
    "attacking_pokemon": pokemon_id,
    "defending_pokemon": enemy_id
}

response_battle=requests.post(url=f'{URL}/battle', headers=HEADER, json= body_battle)
print(response_battle.text)