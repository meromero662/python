import requests
import json

for i in range (2 , 100):
    url = 'https://4bbh01oqwj.execute-api.eu-north-1.amazonaws.com/numcheck?integer=' + str(i)

    r = requests.get(url)
    if json.loads(r.text)['prime'] :
        print(i)

