from bs4 import BeautifulSoup
import requests
from typing import List, NamedTuple
from function import getLink as link
from concurrent.futures import ThreadPoolExecutor
import json


class Pokemon(NamedTuple):
    dex_num: int
    name: str
    form: str
    gen: int
    pic1: str
    pic2: str
    details_path: str
    types: List[str]
    bst: int
    hp: int
    attack: int
    defense: int
    sp_attack: int
    sp_defense: int
    speed: int
    dex_entry_url: str



def fetch_data(pokemon):
    pokemon_data = pokemon.find_all('td')
    dex_num = pokemon_data[0]['data-sort-value']
    avatar1 = pokemon_data[0].find('img')['src']

    name = pokemon_data[1].find_all('a')[0].getText()
    if pokemon_data[1].find_all('small'):
        form = pokemon_data[1].find_all('small')[0].getText()
    else:
        form = None

    if int(dex_num) < 152:
        gen = 1
    elif 151 < int(dex_num) < 252:
        gen = 2
    elif 251 < int(dex_num) < 387:
        gen = 3
    elif 251 < int(dex_num) < 494:
        gen = 4
    elif 493 < int(dex_num) < 650:
        gen = 5
    elif 649 < int(dex_num) < 722:
        gen = 6
    elif 721 < int(dex_num) < 810:
        gen = 8
    elif int(dex_num) > 809:
        gen = 9

    if form:
        if "Mega" in form:
            gen = 6
        elif "Alolan" in form:
            gen = 7
        elif "Galarian" in form or "Hisuian" in form:
            gen = 8
        elif "Paldean" in form:
            gen = 9

    details_uri = pokemon_data[1].find_all('a')[0]['href']

    types = []
    for pokemon_type in pokemon_data[2].find_all('a'):
        types.append(pokemon_type.getText())

    # stats
    BST = pokemon_data[3].getText()
    hp = pokemon_data[4].getText()
    attack = pokemon_data[5].getText()
    defense = pokemon_data[6].getText()
    sp_attack = pokemon_data[7].getText()
    sp_defense = pokemon_data[8].getText()
    speed = pokemon_data[9].getText()

    entry_url = f'https://pokemondb.net{details_uri}'

    avatar2 = link(name, form)
    # print(f"{dex_num}. {name} (gen {gen})-{form}: {avatar2}")

    if name == "Mew":
        print(f"Generation 1 complete")
    elif name == "Celebi":
        print(f"Generation 2 complete")
    elif name == "Deoxys" and "Speed" in form:
        print(f"Generation 3 complete")
    elif name == "Arceus":
        print(f"Generation 4 complete")
    elif name == "Genesect":
        print(f"Generation 5 complete")
    elif name == "Zygarde" and "Complete" in form:
        print(f"Generation 6 complete")
    elif name == "Melmetal":
        print(f"Generation 7 complete")
    elif name == "Enamorus" and "Therian" in form:
        print(f"Generation 8 complete")
    elif name == "Pecharunt":
        print(f"Generation 9 complete")

    return Pokemon(
        dex_num=int(dex_num),
        name=name,
        form=form,
        gen=int(gen),
        pic1=avatar1,
        pic2=avatar2,
        details_path=details_uri,
        types=types,
        bst=int(BST),
        hp=int(hp),
        attack=int(attack),
        defense=int(defense),
        sp_attack=int(sp_attack),
        sp_defense=int(sp_defense),
        speed=int(speed),
        dex_entry_url=entry_url

    )

def main():
    print("Scraping started...")
    url = 'https://pokemondb.net/pokedex/all'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    pokemon_rows = soup.find_all('table', id='pokedex')[0].find_all("tbody")[0].find_all('tr')

    scraped_pokemon_data = []

    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(fetch_data, pokemon_rows))

    scraped_pokemon_data.extend(results)
    print('-------------------------DONE---------------------------')
    print(len(scraped_pokemon_data))

    scraped_pokemon_data = sorted(scraped_pokemon_data, key=lambda i: i.dex_num)

    data = [pokemon._asdict() for pokemon in scraped_pokemon_data]

    json_file = "pokemon_dataV3.json"

    with open(json_file, "w") as outfile:
        json.dump(data, outfile, indent=4)

    print(f"Pokemon data saved to {json_file}")

    # for pokemon in scraped_pokemon_data:
    #     print(f'{pokemon.name} - {pokemon.form}: {pokemon.pic2}')



if __name__ == '__main__':
    main()

