#!/usr/bin/env python
#title: peak hell
#hint1: pronounce it
#fact1: refference to a file named banner.p in the html source
#fact2: once depickled, it looks like a run-length encoding
import urllib,pickle
url='http://www.pythonchallenge.com/pc/def/banner.p'
obj=pickle.load(urllib.urlopen(url))
for line in obj:
    print "".join(map(lambda pair: pair[0]*pair[1], line))
#The banner shown says: channel
