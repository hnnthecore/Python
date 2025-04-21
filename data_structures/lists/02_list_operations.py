# Exercise 02: List Operations

# Start with a list of numbers
numbers = [4, 2, 9, 1, 7]

print("Original list:", numbers)

# Insert a number at index 2
numbers.insert(2, 5)
print("After inserting 5 at index 2:", numbers)

# Remove a specific number (first match)
numbers.remove(9)
print("After removing 9:", numbers)

# Remove the last element using pop()
last = numbers.pop()
print("After popping last element:", numbers)
print("Popped element:", last)

# Sort the list in ascending order
numbers.sort()
print("Sorted list:", numbers)

# Reverse the list
numbers.reverse()
print("Reversed list:", numbers)

# Clear the entire list
numbers.clear()
print("Cleared list:", numbers)
