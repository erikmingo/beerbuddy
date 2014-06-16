import requests
import json


_API_KEY_ = 'c682be4ef9381532d5d9603138f6f598'
_BASE_URL_ = 'http://api.brewerydb.com/v2/beers/?key=%s' % _API_KEY_

def getCatagories():
    _CAT_BASE_URL_ = 'http://api.brewerydb.com/v2/categories/?key=%s' % _API_KEY_
    payload = requests.get(_CAT_BASE_URL_)
    formatedjson = json.dumps(payload.json(), indent=4, sort_keys=True)
    with open('beer_categories.json', 'w') as f:
        f.write(formatedjson)

def getStyles():
    _CAT_BASE_URL_ = 'http://api.brewerydb.com/v2/styles/?key=%s' % _API_KEY_
    payload = requests.get(_CAT_BASE_URL_)
    formatedjson = json.dumps(payload.json(), indent=4, sort_keys=True)
    with open('beer_styles.json', 'w') as f:
        f.write(formatedjson)

def iterateStyles():
    with open('beer_styles.json', 'r') as f:
        jsonDump = f.read()
    data = json.loads(jsonDump)
    styles = data[u"data"]
# k this works, don't touch, obviously printing is not what we really want here
#this function creates a dictionary with id (int) : style
    styleIds = []
    styleNames = []
    for style in styles:
        styleIds.append(style[u"id"])
        styleNames.append(style[u"name"].encode("utf8").replace(' ', '_'))
        #styleIdDic.update({style[u"id"] : style[u"name"]})

    # print and see if it looks about right.
#    for i, style in zip(styleIds, styleNames):
#        print("id: {0} style: {1}".format(i, style))
    return styleIds, styleNames

def scrapeBeersStyle(styleId, style):
    _CAT_BASE_URL_ = 'http://api.brewerydb.com/v2/beers/?key=%s&styleId=%s' % (_API_KEY_, styleId)
    payload = requests.get(_CAT_BASE_URL_)
    data = json.loads(payload.text)

    try:
        numPages = data[u"numberOfPages"]
    except:
        numPages = 1

    i = 1
    while i <= numPages:
        iterationUrl = 'http://api.brewerydb.com/v2/beers/?key=%s&styleId=%s&p=%s&withBreweries=Y&withIngredients=Y' % (_API_KEY_, styleId, i)
        payload = requests.get(iterationUrl)
        formatedjson = json.dumps(payload.json(), indent=4, sort_keys=True)
#        print formatedjson
        f = open('beerjson/beer_%s.json' % style, 'a')
        f.write(formatedjson)
        f.close()
        i = i + 1

def scrapeAllBeers():
    styleIds, styleNames = iterateStyles()
    for i, style in zip(styleIds, styleNames):
        scrapeBeersStyle(str(i), style.replace('/', '_'))
        print i, style


scrapeAllBeers()



