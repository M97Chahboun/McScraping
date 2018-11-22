from McScrp import mcscrp
import requests

t = requests.get('https://simple.wikipedia.org/wiki/List_of_colors').text
a = mcscrp()
tb = a.scrp(t, 'tbody')['tag'][0]
tr = a.scrp(tb, 'tr')['tag']
di = {}
for i in tr:
    name = a.scrp(i, 'a')['txt']
    par = a.scrp(i, 'td')['txt']
    print('%s : %s' % (name, par))
