# Exercise 03: Infinite Loop with Break

# This loop will run forever unless we use break
while True:
    user_input = input("Type 'exit' to quit the loop: ")
    
    if user_input.lower() == "exit":
        print("Exiting the loop...")
        break  # Exit the loop
    else:
        print(f"You typed: {user_input}")
