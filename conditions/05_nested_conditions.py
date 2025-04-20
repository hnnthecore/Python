# Exercise 05: Login Simulation

# Predefined correct credentials
correct_username = "admin"
correct_password = "1234"

# Ask the user to input credentials
username = input("Enter username: ")
password = input("Enter password: ")

# Check credentials
if username == correct_username and password == correct_password:
    print("Login successful!")
elif username != correct_username and password != correct_password:
    print("Both username and password are incorrect.")
elif username != correct_username:
    print("Incorrect username.")
else:
    print("Incorrect password.")
