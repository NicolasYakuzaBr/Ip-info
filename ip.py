import requests
import pprint

ip = input('\nTARGET IP ADDRESS: ')
url = f'https://ipinfo.io/{ip}'

r = requests.get(url)
pprint.pprint(r.json())
