#title: can you tell the difference?
#hint1: it is more obvious that what you might thin
#fact1: since the difference is brightness, we'll go to brightness.html where we find a new hint
#hint2: maybe consider deltas.gz
import gzip,difflib
deltas=gzip.GzipFile('deltas.gz', 'rb').read()
deltas=deltas.splitlines()
left,right,png=[],[],['','','']
for row in deltas:
    left.append(row[:53])
    right.append(row[56:])
diff = list(difflib.ndiff(left,right))

for row in diff:
    bytes = [chr(int(byte,16)) for byte in row[2:].split()]
    if row[0]=='-': png[0]+=''.join(bytes)
    elif row[0]=='+': png[1]+=''.join(bytes)
    elif row[0]==' ': png[2]+=''.join(bytes)

for i in range(3):
    open('18_%d.png' %i,'wb').write(png[i])

#18_0.png: fly
#18_1.png: butter
#18_2.png: ../hex/bin.html
