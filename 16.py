#title: let me get this straight
#hint1: there are 5 pink pixels in each row
#fact1: pink is color 195 in the image's color index (says Gimp)
import urllib, Image,cStringIO 
def straighten(line): # five equal consecutive pink pixels are the clue
    idx=0
    while line[idx]!=195:
        idx+=1
    return line[idx:]+line[:idx]
    
url = 'http://huge:file@www.pythonchallenge.com/pc/return/mozart.gif'
im = Image.open(cStringIO.StringIO(urllib.urlopen(url).read()))
for y in range(im.size[1]):
    line=[im.getpixel((x, y)) for x in range(im.size[0])]
    line=straighten(line)
    [im.putpixel((x, y),line[x]) for x in range(len(line))]
im.save('16.gif')
#romance.html
