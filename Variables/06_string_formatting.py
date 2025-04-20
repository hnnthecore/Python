# Exercise 06: String Formatting

name = "Alice"
age = 30
height = 1.68

# 1. Concatenation (old style)
print("Name: " + name + ", Age: " + str(age) + ", Height: " + str(height))

# 2. Using f-strings (recommended!)
print(f"Name: {name}, Age: {age}, Height: {height} m")

# 3. Using .format()
print("Name: {}, Age: {}, Height: {} m".format(name, age, height))

# 4. Using .format() with placeholders
print("Name: {n}, Age: {a}, Height: {h} m".format(n=name, a=age, h=height))

# 5. Formatting numbers
pi = 3.1415926535
print(f"Pi (2 decimals): {pi:.2f}")
print("Pi (3 decimals): {:.3f}".format(pi))
