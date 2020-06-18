import requests as r


def namelist():
    payload = {'limit':809}
    listpokemons = []
    response = r.get('https://pokeapi.co/api/v2/pokemon', params=payload)
    pokemons = response.json()
    for line in pokemons['results']:
        listpokemons.append(line['name'])
    return listpokemons


print(namelist())