import urllib
#fhand=urllib.urlopen('http://python-data.dr-chuck.net/comments_42.xml')
fhand=urllib.urlopen('http://python-data.dr-chuck.net/comments_367934.xml')

import xml.etree.ElementTree as ET
tree = ET.fromstring(fhand.read())
counts = tree.findall('.//count')
print sum([int(count.text) for count in counts])

