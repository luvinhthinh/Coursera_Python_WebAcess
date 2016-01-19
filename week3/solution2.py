import urllib
from BeautifulSoup import *

def findName(url, pos, iteration):
    for i in range(0, iteration):
        tag = findTag(url, pos)
        url = tag.get('href', None)
    return tag.contents[0]

def findTag(url, pos): 
    return BeautifulSoup(urllib.urlopen(url).read())('a')[pos]
    
print findName('http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Ijay.html', 17, 7)
