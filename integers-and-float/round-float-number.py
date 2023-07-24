"""
x = float(input("What is x?: "))
y = float(input("What is y?: "))

# OPTIONAL: round the output to 2 decimals or any other number of decimals
# by using the second parameter of the round function
z = round(x / y, 2)

print(f"{x} / {y} = {z}")
"""

x = float(input("What is x?: "))
y = float(input("What is y?: "))

# round the output
# z = round(x / y)

# format the output of the sum for visual clarity:

# by using the comma as a thousands separator (US format)
# print(f"{x} + {y} = {z:,}")
"""
The way you specify to a f string (formatted string) how many decimals you want to show
is by using a colon a dot and the number of decimals you want to show
followed by the f at the end of the number.
"""

z = x / y

print(f"{x} + {y} = {z:.2f}")