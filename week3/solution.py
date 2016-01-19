# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

# Retrieve all of the anchor tags
print sum([int(x.contents[0]) for x in BeautifulSoup(urllib.urlopen('http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_172703.html').read())('span') ]) 
