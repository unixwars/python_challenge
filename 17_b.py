#title: it's me. what do you want?
#fact1: we have to deliver a message to him
from urllib2 import Request,urlopen
from urllib import quote_plus
info='the flowers are on their way'
url='http://www.pythonchallenge.com/pc/stuff/violin.php'
req = Request(url, headers={'Cookie': 'info=' + quote_plus(info)})
print urlopen(req).read()

#balloons.html
