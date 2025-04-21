# Exercise 01: Dictionary Basics

# Step 1: Create a dictionary to store person information
person = {
    "name": "Alice",
    "age": 28,
    "country": "Canada"
}

# Step 2: Print the dictionary
print("Person info:", person)

# Step 3: Access values by keys
print("Name:", person["name"])
print("Age:", person["age"])

# Step 4: Modify a value
person["age"] = 29
print("Updated age:", person["age"])

# Step 5: Add a new key-value pair
person["email"] = "alice@example.com"
print("After adding email:", person)

# Step 6: Remove a key
del person["country"]
print("After removing country:", person)

# Step 7: Use .get() to safely access a key
print("Phone number:", person.get("phone", "Not available"))

# Step 8: Print all keys and values
print("Keys:", person.keys())
print("Values:", person.values())
