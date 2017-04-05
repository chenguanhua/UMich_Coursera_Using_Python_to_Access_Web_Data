import urllib
from BeautifulSoup import *

#url=raw_input('Enter - ')
#url='http://python-data.dr-chuck.net/comments_42.html'

url='http://python-data.dr-chuck.net/comments_367937.html'

html=urllib.urlopen(url).read()
soup=BeautifulSoup(html)

tags=soup('span')


print sum([int(tag.contents[0]) for tag in tags])

