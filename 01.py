#!/usr/bin/env python
#title: what about making trans
#k->m,o->q,e->g
import string
src = string.lowercase[:26]
dst = string.lowercase[2:26] + 'ab'
trans = string.maketrans(src, dst)
text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
print text.translate(trans)
#i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.
print "map".translate(trans)
#ocr.html
