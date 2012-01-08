#!/usr/bin/env python
#Fact1: We're looking for color 8, as shown below. This can be found using im.getcolors() in every frame
import Image,ImageDraw
def get_vectors():
    # Return a list of movement vectors extracted from wiggling pixels
    im = Image.open("white.gif")
    vectors=[]
    try:
        while True:
            pix=list(im.getdata()).index(8)
            y,x=divmod(pix,200)
            v=(x-100,y-100)
            vectors.append(v)
            im.seek(im.tell()+1)
    except EOFError:
        pass # end of sequence
    return vectors

max_x, h, w = 0, 50, 250
im = Image.new('RGB', (w,h))
draw = ImageDraw.Draw(im)
src = (max_x,h//2) # (x,y)
for v in get_vectors():
    if v==(0,0):
        max_x+=30
        src = (max_x,h//2)
        continue
    dst=(src[0]+v[0],src[1]+v[1])
    max_x=max(max_x,dst[0])
    draw.line([src, dst], fill='white')
    src=dst
im.save('22.jpg')
