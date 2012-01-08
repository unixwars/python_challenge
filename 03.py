#!/usr/bin/env python
#title: re
#One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.
import re
mess = open("03.txt").read()
print "".join(re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]',mess))
#linkedlist: linkedlist.html-> linkedlist.php
