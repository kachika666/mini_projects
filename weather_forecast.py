import requests


def weather_forecat():
    location = ['london', 'svo', 'Череповец']
    headers = {'Accept-Language': 'ru'}
    for loc in location:
        url = f'https://wttr.in/{loc}?M?n?q?T'
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        print(response.text)


try:
    weather_forecat()
except requests.exceptions.HTTPError as error:
    exit("Can't get data from server:\n{0}".format(error))
