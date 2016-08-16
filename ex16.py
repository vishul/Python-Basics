from sys import argv

first,filename = argv
print'we are about to erase %s'%filename
print'enter ctrl+c to stop or return to erase'
raw_input('>')
text=open(filename,'w')
print 'the data currently in the file is now deleted'
text.truncate()
print'now enter the data to be written to the file:'
r=raw_input()
text.write(r);
