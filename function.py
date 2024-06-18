from bs4 import BeautifulSoup
import requests


def getImage(name, form, link):
    r = requests.get(link)
    soup = BeautifulSoup(r.text, 'html.parser')
    img = soup.find('img')
    return img.get('src')


def getLink(name, form):
    if name == "Ho-oh":
        name = "Ho-Oh"
    url = f'https://bulbapedia.bulbagarden.net/wiki/{name}_(Pok%C3%A9mon)'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    table_roundy = soup.find('table', class_='roundy')
    table = table_roundy.find('table', class_='roundy')
    links = table.find_all('a', class_='image')

    if len(links) < 2:
        new_link = f"https://bulbapedia.bulbagarden.net{links[0]['href']}"
        return getImage(name, form, new_link)
    else:
        for i in links:
            new_link = f"https://bulbapedia.bulbagarden.net{i['href']}"
            # print(f'{form}')
            if form is None:
                # print(new_link)
                return getImage(name, form, new_link)
            else:
                if "Mega" in form:
                    if " X" in form and "Mega_X" in new_link:
                        # print(new_link)
                        return getImage(name, form, new_link)
                    elif " Y" in form and "Mega_Y" in new_link:
                        # print(new_link)
                        return getImage(name, form, new_link)
                    elif "-Mega." in new_link:
                        return getImage(name, form, new_link)
                elif "Alola" in form or "Galar" in form or "Paldea" in form or "Hisui" in form:
                    if "Alola" in new_link and "Galar" not in form:
                        return getImage(name, form, new_link)
                    elif "Galar" in new_link or "galar" in new_link:
                        if "Mode" in form:
                            if "Zen" in form and "Zen" in new_link:
                                return getImage(name, form, new_link)
                            elif "Standard" in form and "-Galar" in new_link:
                                return getImage(name, form, new_link)
                        else:
                            return getImage(name, form, new_link)
                    elif "Paldea" in new_link:
                        return getImage(name, form, new_link)
                    elif "Hisui" in new_link:
                        return getImage(name, form, new_link)
                elif "Breed" in form:
                    if "Combat" in form and "Combat" in new_link:
                        return getImage(name, form, new_link)
                    elif "Blaze" in form and "Blaze" in new_link:
                        return getImage(name, form, new_link)
                    elif "Aqua" in new_link and "Aqua" in new_link:
                        return getImage(name, form, new_link)
                elif "Partner" in form and "Partner" in new_link:
                    return getImage(name, form, new_link)
                elif "Form" in form:
                    if "Sunny" in form and "Sunny" in new_link:
                        return getImage(name, form, new_link)
                    elif "Rainy" in form and "Rainy" in new_link:
                        return getImage(name, form, new_link)
                    elif "Snowy" in form and "Snowy" in new_link:
                        return getImage(name, form, new_link)
                    elif "Speed" in form and "Speed" in new_link:
                        return getImage(name, form, new_link)
                    elif "Normal" in form:
                        return getImage(name, form, new_link)
                    elif "Attack" in form and "Attack" in new_link:
                        return getImage(name, form, new_link)
                    elif "Defense" in form and "Defense" in new_link:
                        return getImage(name, form, new_link)
                    elif "Origin" in form and "Origin" in new_link:
                        return getImage(name, form, new_link)
                    elif "Altered" in form:
                        return getImage(name, form, new_link)
                    elif "Land" in form:
                        return getImage(name, form, new_link)
                    elif "Sky" in form and "Sky" in new_link:
                        return getImage(name, form, new_link)
                    elif "Red-" in form and "-Red" in new_link:
                        return getImage(name, form, new_link)
                    elif "Blue-" in form and "-Blue" in new_link:
                        return getImage(name, form, new_link)
                    elif "White-" in form and "-White" in new_link:
                        return getImage(name, form, new_link)
                    elif "Incarnate" in form:
                        return getImage(name, form, new_link)
                    elif "Therian" in form and "Therian" in new_link:
                        return getImage(name, form, new_link)
                    elif "Ordinary" in form:
                        return getImage(name, form, new_link)
                    elif "Resolute" in form and "Resolute" in new_link:
                        return getImage(name, form, new_link)
                    elif "Aria" in form and name == "Meloetta":
                        return getImage(name, form, new_link)
                    elif "Pirouette" in form and "Pirouette" in new_link:
                        return getImage(name, form, new_link)
                    elif "Shield" in form and "Shield" in new_link:
                        return getImage(name, form, new_link)
                    elif "Blade" in form and "Blade" in new_link:
                        return getImage(name, form, new_link)
                    elif "50" in form and "Zygarde" in new_link:
                        return getImage(name, form, new_link)
                    elif "10" in form and "10Percent" in new_link:
                        return getImage(name, form, new_link)
                    elif "Complete" in form and "Complete" in new_link:
                        return getImage(name, form, new_link)
                    elif "Midday" in form:
                        return getImage(name, form, new_link)
                    elif "Midnight" in form and "Midnight" in new_link:
                        return getImage(name, form, new_link)
                    elif "Dusk" in form and "Dusk" in new_link:
                        return getImage(name, form, new_link)
                    elif "Solo" in form:
                        return getImage(name, form, new_link)
                    elif "School" in form and "School" in new_link:
                        return getImage(name, form, new_link)
                    elif "Core" in form and "Core" in new_link:
                        return getImage(name, form, new_link)
                    elif "Meteor" in form:
                        return getImage(name, form, new_link)
                    elif "Amped" in form and "Amped" in new_link:
                        return getImage(name, form, new_link)
                    elif "Low" in form and "Low" in new_link:
                        return getImage(name, form, new_link)
                    elif "Zero" in form:
                        return getImage(name, form, new_link)
                    elif "Hero" in form and "Hero" in new_link:
                        return getImage(name, form, new_link)
                    elif "Curly" in form:
                        return getImage(name, form, new_link)
                    elif "Droopy" in form and "Droopy" in new_link:
                        return getImage(name, form, new_link)
                    elif "Stretchy" in form and "Stretchy" in new_link:
                        return getImage(name, form, new_link)
                    elif "Two" in form:
                        return getImage(name, form, new_link)
                    elif "Three" in form and "HOME0982Th" in new_link:
                        return getImage(name, form, new_link)
                    elif "Chest" in form:
                        return getImage(name, form, new_link)
                    elif "Roaming" in form and "Roaming" in new_link:
                        return getImage(name, form, new_link)
                    elif "Terastal" in form and "Terastal" in new_link:
                        return getImage(name, form, new_link)
                    elif "Stellar" in form and "HOME1024S" in new_link:
                        return getImage(name, form, new_link)
                elif "Primal" in form and "Primal" in new_link:
                    return getImage(name, form, new_link)
                elif "Cloak" in form:
                    if "Plant" in new_link and "Plant" in form:
                        return getImage(name, form, new_link)
                    elif "Sandy" in new_link and "Sandy" in form:
                        return getImage(name, form, new_link)
                    elif "Trash" in new_link and "Trash" in form:
                        return getImage(name, form, new_link)
                elif "Rotom" in form:
                    if "Heat" in new_link and "Heat" in form:
                        return getImage(name, form, new_link)
                    elif "Wash" in new_link and "Wash" in form:
                        return getImage(name, form, new_link)
                    elif "Frost" in new_link and "Frost" in form:
                        return getImage(name, form, new_link)
                    elif "Fan" in new_link and "Fan" in form:
                        return getImage(name, form, new_link)
                    elif "Mow" in new_link and "Mow" in form:
                        return getImage(name, form, new_link)
                elif "Mode" in form:
                    if "Standard" in form:
                        return getImage(name, form, new_link)
                    elif "Standard" in form:
                        return getImage(name, form, new_link)
                    elif "Zen" in form and "Zen" in new_link:
                        return getImage(name, form, new_link)
                    elif "Zenith" in new_link and "Zenith" in form:
                        return getImage(name, form, new_link)
                    elif "Full" in new_link and "Full" in form:
                        return getImage(name, form, new_link)
                    elif "Hangry" in new_link and "Hangry" in form:
                        return getImage(name, form, new_link)
                elif "Kyurem" in form:
                    if "Black" in new_link and "Black" in form:
                        return getImage(name, form, new_link)
                    elif "White" in new_link and "White" in form:
                        return getImage(name, form, new_link)
                elif "Ash-" in form and "-Ash" in new_link:
                    return getImage(name, form, new_link)
                elif "Male" in form or "Female" in form:
                    return getImage(name, form, new_link)
                elif "Confined" in form:
                    return getImage(name, form, new_link)
                elif "Unbound" in form and "Unbound" in new_link:
                    return getImage(name, form, new_link)
                elif "Style" in form:
                    if "Baile" in form:
                        return getImage(name, form, new_link)
                    elif "Pom" in new_link and "Pom" in form:
                        return getImage(name, form, new_link)
                    elif "Pa" in new_link and "Pa" in form and name == "Oricorio":
                        return getImage(name, form, new_link)
                    elif "Sensu" in new_link and "Sensu" in form:
                        return getImage(name, form, new_link)
                    elif "Single" in new_link and "Single" in form:
                        return getImage(name, form, new_link)
                    elif "Rapid" in new_link and "Rapid" in form:
                        return getImage(name, form, new_link)
                elif "Tempo" in form and "Tempo" in new_link:
                    return getImage(name, form, new_link)
                elif "Necrozma" in form:
                    if "Dusk" in new_link and "Dusk" in form:
                        return getImage(name, form, new_link)
                    elif "Dawn" in new_link and "Dawn" in form:
                        return getImage(name, form, new_link)
                    elif "Ultra" in new_link and "Ultra" in form:
                        return getImage(name, form, new_link)
                elif "Face" in form:
                    if "Ice" in form:
                        return getImage(name, form, new_link)
                    elif "Noice" in new_link and "Noice" in form:
                        return getImage(name, form, new_link)
                elif "Hero of" in form and "Hero" in new_link:
                    return getImage(name, form, new_link)
                elif "Crown" in form and "Zacian." in new_link or "Zamazenta." in new_link:
                    return getImage(name, form, new_link)
                elif "Eternamax" in form and "HOME0890E" in new_link:
                    return getImage(name, form, new_link)
                elif "Rider" in form:
                    if "Ice" in new_link and "Ice" in form:
                        return getImage(name, form, new_link)
                    elif "Shadow" in new_link and "Shadow" in form:
                        return getImage(name, form, new_link)
                elif "Bloodmoon" in form and "Bloodmoon" in new_link:
                    return getImage(name, form, new_link)
                elif "Family of Four" in form:
                    return getImage(name, form, new_link)
                elif "Family of Three" and "HOME" in new_link:
                    return getImage(name, form, new_link)
                elif "Plumage" in form:
                    if "Green" in form:
                        return getImage(name, form, new_link)
                    elif "B" in new_link and "Blue" in form:
                        return getImage(name, form, new_link)
                    elif "Y" in new_link and "Yellow" in form:
                        return getImage(name, form, new_link)
                    elif "W" in new_link and "White" in form:
                        return getImage(name, form, new_link)
                elif "Mask" in form:
                    if "Teal" in new_link and "Teal" in form:
                        return getImage(name, form, new_link)
                    elif "Wellspring" in new_link and "Wellspring" in form:
                        return getImage(name, form, new_link)
                    elif "Hearthflame" in new_link and "Hearthflame" in form:
                        return getImage(name, form, new_link)
                    elif "Cornerstone" in new_link and "Cornerstone" in form:
                        return getImage(name, form, new_link)
                elif "Size" in form:
                    return getImage(name, form, new_link)
                else:
                    continue

