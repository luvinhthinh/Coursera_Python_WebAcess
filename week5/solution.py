import json
import urllib

url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_172704.json'
print sum([ int(x['count']) for x in json.loads(urllib.urlopen(url).read())['comments']])
