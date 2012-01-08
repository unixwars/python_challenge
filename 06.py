#!/usr/bin/env python
#title: now there are pairs
#hint1: Image is a zipper and  there is a comment in the page <!-- <-- zip -->
#once we open channel.zip, there are some more hints: "welcome to my zipped list". 
#hint2: start from 90052
#hint3: answer is inside the zip
import zipfile,re
idx="90052"
file = zipfile.ZipFile("channel.zip", "r")
history = []
while True:
    history.append(idx)
    data = file.read(idx+".txt")
    print "File",idx+":\t"+ data
    idx="".join(re.findall('[0-9.]',data))
    if len(idx)==1:
        break

#When we get to the end of the linked list we get: "Collect the comments".
print ''.join([file.getinfo(i+'.txt').comment for i in history])
#hockey.htm says "it's in the air. look at the letters". 
#so hockey is made out of 'oxygen'
