from McScrp import mcscrp
import requests

t = requests.get('https://simple.wikipedia.org/wiki/List_of_colors').text
a = mcscrp()
tb = a.scrp(t, 'tbody')['tag'][0]
tr = a.scrp(tb, 'tr')['tag']
for i in tr:
    g = a.get_attr(i, 'href')
    print(g)

