import urllib
from BeautifulSoup import *

url='http://python-data.dr-chuck.net/known_by_Sinem.html'
count=7
position=17

print url
for i in range(0,count):
    html=urllib.urlopen(url).read()
    soup=BeautifulSoup(html)
    tags=soup('a')
    url=tags[position].get('href',None)
    print url