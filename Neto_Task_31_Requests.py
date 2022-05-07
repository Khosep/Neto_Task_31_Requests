import requests

NAMES = ['Hulk', 'Captain America', 'Thanos']
URL = 'https://superheroapi.com/api/2619421814940190/'


def most_intelligence():
    heroes_intelligence = {}
    for name in NAMES:
        res = requests.get(URL + f'search/{name}').json()
        if res['results'][0]['name'] == name:
            heroes_intelligence[res['results'][0]['name']] = int(res['results'][0]['powerstats']['intelligence'])
    return sorted(heroes_intelligence.items(), key=lambda h: h[1], reverse=True)


first, second, third = most_intelligence()
print(f'{first[0]} (intelligence: {first[1]}) is the most intelligence hero '
      f'compared to {second[0]}({second[1]}) and {third[0]}({third[1]}).')
