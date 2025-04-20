# Exercise 04: Grading System

# Ask the user to enter a grade between 0 and 100
grade = int(input("Enter your grade (0 to 100): "))

# Evaluate the grade
if grade >= 90:
    print("Grade: Excellent")
elif grade >= 75:
    print("Grade: Good")
elif grade >= 60:
    print("Grade: Sufficient")
elif grade >= 0:
    print("Grade: Insufficient")
else:
    print("Invalid grade. Must be between 0 and 100.")
