from McScrp import mcscrp
import requests

t = requests.get('https://www.britannica.com/topic/list-of-countries-1993160').text
a = mcscrp()
tb = a.scrp(t, 'article')['tag'][0]
f = a.scrp(tb,'section')['tag'][0]
g = a.scrp(tb,'ul')['tag'][1]
g = a.scrp(g,'a')['txt']
print(g)
