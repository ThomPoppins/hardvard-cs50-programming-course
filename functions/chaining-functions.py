# Ask user for their name
name = input("What is your name?: ")

# strip whitespace from str
# name = name.strip()

# capitalize str (first letter)
# name = name.capitalize()

"""
chaining the formatting functions is a good way to keep the code clean and readable
the order of the functions is important, if you capitalize the name first and then remove the whitespace, the name will not be capitalized
the order of the functions is from left to right, so the first function will be executed first
"""

# chain the functions in order to remove whitespace in the front and back of the string and then capitalize all letters from all words in the name
name = name.strip().title()

# Say hello to the user
print(f"Hello {name}")

# HINT: chain the formatting functions to the first input() function so you have your name formatted correctly from the start
name = input("What is your name?: ").strip().title()

# Say hello to the user
print(f"Hello {name}")