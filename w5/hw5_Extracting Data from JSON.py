import urllib
#fhand=urllib.urlopen('http://python-data.dr-chuck.net/comments_42.json')
fhand=urllib.urlopen('http://python-data.dr-chuck.net/comments_367938.json ')

import json

info = json.loads(fhand.read())

print sum([comment['count'] for comment in info['comments']])
