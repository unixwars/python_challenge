#hint1: We used to play this game when we were kids
#hint2: When I had no idea what to do, I looked backwards.
#hint3: package.pack
import zlib,bz2
st=open('21_package.pack').read()
log=''
log_len=len(log)
while True:
    try: #zlib
        st=zlib.decompress(st)
        log+=' '
    except: 
        try: #bzip2
            st=bz2.decompress(st)
            log+='#'
        except: #reverse 
            if log_len==len(log): break
            st=st[::-1]
            print log[log_len:]
            log_len=len(log)
open('21_package.unpack','wb').write(st)
##Hint after the whole decompression process: look at your logs
##Originaly I kept a list with the number of zlib and bzip2 cycles run, expecting a banner(ish) run length encoding. I noticed that the sum of cycles needed to complete each direction was allways roughly the same. That is, before I had to reverse the string to start over, the sum of bzip+zip+bzip+... was more or less 73. And that meant that the output was meant to be directly graphical, so I sticked to simple string printig.