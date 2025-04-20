# Exercise 05: Multiple Assignment

# Assign multiple values to multiple variables
x, y, z = 5, 10, 15
print("x =", x)
print("y =", y)
print("z =", z)

# Assign the same value to multiple variables
a = b = c = 100
print("a =", a)
print("b =", b)
print("c =", c)

# Swap values between variables (without using a temp variable)
x, y = y, x
print("After swapping:")
print("x =", x)
print("y =", y)

# Unpack values from a list
fruits = ["apple", "banana", "orange"]
f1, f2, f3 = fruits
print("First fruit:", f1)
print("Second fruit:", f2)
print("Third fruit:", f3)
