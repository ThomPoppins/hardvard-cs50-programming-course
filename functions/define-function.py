# use def to define a function
def hello(to_whom):
    # print "Hello, " + to_whom + (end parameter=)"!"
    # and separated by (separator parameter=)""
    print("Hello, ", to_whom, "!", sep="")


name = input("What is your name?: ")
hello(name)