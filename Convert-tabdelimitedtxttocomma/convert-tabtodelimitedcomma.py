import os
import re
cwd = os.getcwd() + '\\test'
allfiles = os.listdir(cwd)
for i in range(len(allfiles)):
    fileobj  = open('test/'+ allfiles[i], 'r')
    contents = fileobj.read();
    newcontents= re.sub(r'\t', ',' , contents)
    fileobj2 = open('result/' + allfiles[i], 'w')
    fileobj2.write(newcontents)
    fileobj.close()

