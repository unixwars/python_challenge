#title: eat?
#hint1: cookies
#hint2: image from level 4
#fact1: level 4 sets a cookie: info=you+should+have+followed+busynothing...; 
#fact2: the cookie info changes with each link of the linkedlist
#fact3: once obtained, the info seems to be a quote_plus string from a BZ2 piece of data
import urllib,re,bz2
url='http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='
seed="12345"
info=''
while True:
    req=urllib.urlopen(url+seed)
    text=req.read()
    seed=''.join(re.findall(r"busynothing is (\d+)",text))
    cookies=req.info().getheaders('Set-Cookie')[0]
    byte=cookies.split(';')[0].split('=')[1]
    info+=byte
    try :
        int(seed)
        print "   Info:",byte,"\t   Next:",seed
    except :
        print "   Info:",byte,"\t   Last:",text
        break
print "info:",bz2.decompress(urllib.unquote_plus(info))
# is it the 26th already? call his father and inform him that "the flowers are on their way". he'll understand.
# Using level 13's phonebook, phone('Leopold') -> violin
