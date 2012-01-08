#!/usr/bin/env python
#title: ocr
#hint1: recognize the characters. maybe they are in the book, but MAYBE they are in the page source.
#hint2: find rare characters in the mess below (stored in file 02.txt):
mess = open("02.txt").read()
dict = {}
for ch in mess:
    dict[ch] = dict.get(ch, 0) + 1
print "".join(ch for ch in mess if dict[ch] == 1)
#equality
