# Define main function with def in order to call every
# function within the main function defined further
# down in the code and to keep the code clean
# call main function at the end of the code
def main():
    name = input("What is your name?: ")
    # call hello function and use default value for parameter
    hello()
    # call hello function and use name variable as argument
    hello(name)


"""
# use def to define a function and define a parameter within ()
# def hello(to_whom):
    # print "Hello, " + to_whom + (end parameter=)"!"
    # and separated by (separator parameter=)""
    print("Hello, ", to_whom, "!", sep="")
"""


# use def to define a function and use default value for parameter using =
def hello(to_whom="World"):
    # print "Hello, " + to_whom + (end parameter=)"!"
    # and separated by (separator parameter=)""
    print("Hello, ", to_whom, "!", sep="")


# call main function at the end of the code to execute the code
main()
