# Exercise 01: Set Basics and Operations

# Step 1: Create a set of fruits
fruits = {"apple", "banana", "orange", "apple"}  # 'apple' will appear only once
print("Fruits set:", fruits)

# Step 2: Add a new fruit
fruits.add("mango")
print("After adding mango:", fruits)

# Step 3: Remove a fruit
fruits.remove("banana")
print("After removing banana:", fruits)

# Step 4: Check membership
print("Is 'orange' in the set?", "orange" in fruits)
print("Is 'kiwi' in the set?", "kiwi" in fruits)

# Step 5: Set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("\nSet A:", set_a)
print("Set B:", set_b)

print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference (A - B):", set_a - set_b)
print("Symmetric Difference:", set_a ^ set_b)
