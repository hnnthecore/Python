# Exercise 07: Nested Conditions

age = int(input("Enter your age: "))

if age >= 18:
    has_id = input("Do you have a valid ID? (yes/no): ").lower()

    if has_id == "yes":
        print("Access granted.")
    else:
        print("Access denied. ID required.")
else:
    print("Access denied. You must be at least 18 years old.")
