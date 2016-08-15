# this program opens a file and prints its content on terminal.
#files name is entered as a command line argument to the program.

#this line is needed so we can use command line arguments in our program.
from sys import argv
#the first command line argument i.e program call is saved in name and the
#second CLA is stored in filename this is the name of the file to be opened
name,filename=argv
txt=open(filename)
#everything inside the file is printed on the terminal.
print txt.read()
txt.close()
