#!/usr/bin/env python
#title: follow the chain
#hint1: urllib may help. DON'T TRY ALL NOTHINGS, since it will never end. 400 times is more than enough. 
#hint2: links to http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345
#When we get to 92118 it says "Yes. Divide by two and keep going.", so we'll reset the seed to 46059
import urllib,re
url='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
seed="46059"
for i in range(400):    
    text=urllib.urlopen(url+seed).read()
    seed="".join(re.findall(r"nothing is (\d+)",text))
    try :
        int(seed)
        print "   Next:",seed
    except :
        print "   Last:",text
        break
#peak.html
