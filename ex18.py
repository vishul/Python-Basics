#demonstartion of functions and how to pass arguments
def print_one(args):
    print'I got one argument %r'%args
def print_two(arg1,arg2):
    print'I got two arguments%r and %d'%(arg1,arg2)

# not the * in *args converts multiple arguments into a list
def print_two_again(*args):
    arg1, arg2=args
    print'the arguments are %r and %r'%(arg1,arg2)
def print_nothing():
    print'Poor me! I got nothing!'
print_one(22)
print_two(22,23)
print_two_again("hello"," world")
print_nothing
