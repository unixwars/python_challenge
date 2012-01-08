#!/usr/bin/env python
#title: walk around 
#hint1: image is a spiral
#hint2: remember: 100*100 = (100+99+99+98) + .... (3+2+2+1)+1
#fact1: wire.jpg is 1x10000 pixels = 100*100
import Image
im = Image.open("wire.png")
new = Image.new(im.mode,[100,100])
doubled_steps=200
directions=[(1,0), (0,1), (-1,0), (0,-1)] # vectors in [x,y] format
x,y,p=-1,0,0
while doubled_steps//2 > 0:
    for v in directions: # we will be taking steps in 4 directions
        steps=doubled_steps//2
        for s in range(steps):
            x,y=x+v[0],y+v[1]
            new.putpixel((x,y),im.getpixel((p,0)))
            p+=1
        doubled_steps-=1
new.save('14.jpg')
#cat -> uzi.html
