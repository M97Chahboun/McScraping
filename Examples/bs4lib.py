import requests
from bs4 import BeautifulSoup

data = requests.get('https://umggaming.com/leaderboards')
soup = BeautifulSoup(data.text, 'html.parser')
leaderboard = soup.find('table', {'id': 'leaderboard-table'})
tbody = leaderboard.find('tbody')
di = {}
for tr in tbody.find_all('tr'):
    place = tr.find_all('td')[0].text.strip()
    username = tr.find_all('td')[1].find_all('a')[1].text.strip()
    xp = tr.find_all('td')[3].text.strip()
    di[username] = [xp, place]
for i in di.keys():
    print('%s :%s, %s' % (i, di[i][0], di[i][1]))
