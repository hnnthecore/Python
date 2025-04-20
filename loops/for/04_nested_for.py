# Exercise 04: Nested For Loops

# Print a simple 3x3 grid of stars
print("3x3 Grid of *:")
for row in range(3):
    for col in range(3):
        print("*", end=" ")
    print()  # Move to the next line

# Print a multiplication table from 1 to 5
print("\nMultiplication Table (1 to 5):")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:2}", end=" ")  # :2 = fixed width
    print()
