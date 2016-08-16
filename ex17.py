from sys import argv
from os.path import exists

first, readfrom,writeto = argv

print 'copying from %s to %s'%(readfrom,writeto)
#r = open(readfrom).read()
re=open(readfrom)
r=re.read()
print'the length of the input file is %d'%len(r)
print'Does the output file exists %r'%exists(writeto)

wr=open(writeto,'w+')
print'all done'

wr.write(r)

wr.close()
re.close()
