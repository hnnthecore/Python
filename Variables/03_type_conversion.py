# Exercise 03: Type Conversion

# Input from the user is always a string
age_str = input("Enter your age: ")
print("Type of age_str:", type(age_str))

# Convert string to integer
age = int(age_str)
print("Your age + 1:", age + 1)
print("Type of age:", type(age))

# Convert string to float
height_str = input("Enter your height in meters: ")
height = float(height_str)
print("Your height is:", height)
print("Type of height:", type(height))

# Convert number to string
age_str_again = str(age)
print("Age as string:", age_str_again)
print("Type of age_str_again:", type(age_str_again))

# Convert any value to boolean
print("Bool of 0:", bool(0))           # False
print("Bool of 42:", bool(42))         # True
print("Bool of empty string:", bool(""))  # False
print("Bool of 'hello':", bool("hello"))  # True
