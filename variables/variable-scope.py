def main():
    name = input("What is your name?: ")
    hello()

def hello():
    # the variable name is not defined in this scope
    print("Hello, ", name)

main()
# This will result in an error:
