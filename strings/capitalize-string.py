# Ask user for their name
name = input("What is your name?: ")

# strip whitespace from str
name = name.strip()

# capitalize str (first letter)
name = name.capitalize()

# capitalize letters from all words in str
name = name.title()

# Say hello to the user
print(f"Hello {name}")