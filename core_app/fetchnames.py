import requests as r


def namelist():
    listpokemons = []
    response = r.get('https://pokeapi.co/api/v2/pokemon?limit=809')
    pokemons = response.json()
    for line in pokemons['results']:
        listpokemons.append(line['name'])
    return listpokemons
