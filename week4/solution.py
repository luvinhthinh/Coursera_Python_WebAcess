import urllib
import xml.etree.ElementTree as ET

url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_172700.xml'
print sum([ int(x.text) for x in ET.fromstring(urllib.urlopen(url).read()).findall('comments/comment/count')])
