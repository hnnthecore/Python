# Exercise 02: While Counter with Custom Range

# Ask the user for start and end values
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Start counting
print(f"Counting from {start} to {end}:")
while start <= end:
    print(start)
    start += 1
