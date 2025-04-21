# Exercise 01: Tuple Basics

# Step 1: Create a tuple of colors
colors = ("red", "green", "blue", "green")

# Step 2: Print the tuple
print("Colors:", colors)

# Step 3: Access elements by index
print("First color:", colors[0])
print("Last color:", colors[-1])

# Step 4: Count how many times an element appears
print("Green appears:", colors.count("green"), "times")

# Step 5: Find the index of an element
print("Index of 'blue':", colors.index("blue"))

# Step 6: Try to modify an element (this will cause an error)
# colors[1] = "yellow"  # Uncomment to test immutability
