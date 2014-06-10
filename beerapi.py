import requests


_API_KEY_ = 'c682be4ef9381532d5d9603138f6f598'
_BASE_URL_ = 'http://api.brewerydb.com/v2/beers/?key=%s' % _API_KEY_


r = requests.get(_BASE_URL_)

print(r.json())

with open('beers.json', 'w') as f:
    f.write(r.text)
