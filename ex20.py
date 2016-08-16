# this is a program to illustrate "how to use files and functions together"
from sys import argv

def print_file (a):
    read=a.read()
    print read
#function to rewind the file indicator  back to the beginning of the file
def rewind(a):
    a.seek(0)
def print_line(l,a):
    line=a.readline()
    print"%d:%r"%(l,line)
name, input_file = argv
a=open(input_file,'r')
print 'function call to print the entire file content'
print_file(a)
print'function call to rewind to the start'
rewind(a)
print'function call to print the first line'
print_line(1, a)
print'function call to print the second line'
print_line(2, a)
