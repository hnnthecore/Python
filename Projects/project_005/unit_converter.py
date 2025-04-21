# Project 005: Unit Converter

def convert_km_to_miles(km):
    return km * 0.621371

def convert_miles_to_km(miles):
    return miles / 0.621371

def convert_kg_to_lbs(kg):
    return kg * 2.20462

def convert_lbs_to_kg(lbs):
    return lbs / 2.20462

def show_menu():
    print("\n--- Unit Converter ---")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Kilograms to Pounds")
    print("4. Pounds to Kilograms")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        km = float(input("Enter kilometers: "))
        print(f"{km} km = {convert_km_to_miles(km):.2f} miles")

    elif choice == "2":
        miles = float(input("Enter miles: "))
        print(f"{miles} miles = {convert_miles_to_km(miles):.2f} km")

    elif choice == "3":
        kg = float(input("Enter kilograms: "))
        print(f"{kg} kg = {convert_kg_to_lbs(kg):.2f} lbs")

    elif choice == "4":
        lbs = float(input("Enter pounds: "))
        print(f"{lbs} lbs = {convert_lbs_to_kg(lbs):.2f} kg")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select a number from 1 to 5.")
