#title: go away!
#hint1: private property beyond this fence
#hint2: 'unreal.jpg': but inspecting it carefully is allowed.
#fact1: One of the headers is 'Content-Range: bytes 0-30202/2123456789'
#          Info about this at http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35
#fact2: beyond the fence would be 30203 and 2123456789 *IS* unreal. We'll have to dig for this one
import urllib
url = 'http://butter:fly@www.pythonchallenge.com/pc/hex/unreal.jpg'

##Private info found
for i in [(30237,30337), (30284,30384), (30295,30395), (30313,30413), 
            (2123456744,2123456788), (2123456712,2123456743)]:
    opener = urllib.FancyURLopener({})
    opener.addheader("range", "bytes=%d-%d" % i)
    f = opener.open(url)
    print f.read()
    
##Something hidden
opener = urllib.FancyURLopener({})
opener.addheader("range", "bytes=%d-%d" % (1152983631,1152983671))
f = opener.open(url)
print f.info()
open("20.zip", "w").write(f.read())

#Content-Range: bytes 30237-30283/2123456789
## we can go on in this way for really long time.
#Content-Range: bytes 30284-30294/2123456789
## stop this!
#Content-Range: bytes 30295-30312/2123456789
## invader! invader!
#Content-Range: bytes 30313-30346/2123456789
## ok, invader. you are inside now.
#2123456712-2123456743/2123456789
## and it is hiding at 1152983631
#2123456744-2123456788/2123456789
##esrever ni emankcin wen ruoy si drowssap eht
