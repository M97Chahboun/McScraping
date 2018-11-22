from McScrp import mcscrp
import requests

d = requests.get('https://umggaming.com/leaderboards').text
a = mcscrp()
body = a.scrp(d, 'tbody')['tag'][0]
di = {}
for i in a.scrp(body, 'tr')['tag']:
    user = a.scrp(i, 'a')['txt'][0]
    info = a.scrp(i, 'td')['txt']
    di[user] = info
for i in di.keys():
    print('%s :%s, %s' % (i, di[i][0], di[i][1]))
