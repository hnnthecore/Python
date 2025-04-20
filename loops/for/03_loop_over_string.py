# Exercise 03: Loop Over a String

# Define a string
text = "Python"

# Loop through each character
for char in text:
    print(char)

# Print each character with its position
print("\nCharacters with index:")
for index in range(len(text)):
    print(f"Character at index {index} is {text[index]}")
