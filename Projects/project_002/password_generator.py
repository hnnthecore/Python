# Project 002: Password Generator

import random
import string

# Display welcome message
print("🔐 Password Generator")

# Ask the user for password length
length = int(input("Enter desired password length: "))

# Define character sets
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

# Combine all characters
all_chars = letters + digits + symbols

# Generate password
password = "".join(random.choice(all_chars) for _ in range(length))

# Display the generated password
print("Generated password:", password)
