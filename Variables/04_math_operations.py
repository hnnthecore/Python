# Exercise 04: Math Operations

# Define two numbers
a = 10
b = 3

# Basic operations
print("Addition:", a + b)            # 13
print("Subtraction:", a - b)         # 7
print("Multiplication:", a * b)      # 30
print("Float division:", a / b)      # 3.333...
print("Integer division:", a // b)   # 3
print("Modulo (remainder):", a % b)  # 1
print("Exponentiation:", a ** b)     # 1000

# Using parentheses to control order
result = (a + b) * 2
print("Result of (a + b) * 2:", result)

# Operator precedence: ** > * / // % > + -
print("Without parentheses:", a + b * 2)  # 10 + 6 = 16
