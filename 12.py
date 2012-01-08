#!/usr/bin/env python
#title: dealing evil
#hint1: image with a shuffled deck and five piles
#hint2: filename is evil1.jpg
#fact1: there are more evil?.jpg and and evil2.gfx
#fact2: the gfx file, in an hex editor, shows signs of beeing a GIF87a header and JPEG header, only shuffled every 5 bytes
#fact3: we must deshuffle evil2.gfx into 5 piles
#fact4: when trying to retrieve file evil4.jpg a text appears "http://www.pythonchallenge.com/pc/return/evil4.jpg" and the source code is "Bert is evil! go back!"
info=open("evil2.gfx").read()
[open("12_f%d.dat" %i, "w").write(info[i::5]) for i in range(5)]
#By using 'file' in the shell, we can learn what type of file we're dealing with in case our image viewer cares for the extension

#disproportional.html
