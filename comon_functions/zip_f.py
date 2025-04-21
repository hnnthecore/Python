names = ["Alice", "Bob"]
ages = [25, 30]

zipped = zip(names, ages)
print(list(zipped))  # [('Alice', 25), ('Bob', 30)]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# Exercise 1: Basic zip
students = ["Anna", "Luca", "Sara"]
grades = [85, 90, 78]

for student, grade in zip(students, grades):
    print(f"{student} got a grade of {grade}")


# Exercise 2: Multiple zips (3 lists)
products = ["Apple", "Banana", "Milk"]
prices = [0.5, 0.3, 1.2]
quantities = [3, 5, 2]

for product, price, qty in zip(products, prices, quantities):
    total = price * qty
    print(f"{product}: {qty} x ${price} = ${total:.2f}")


# Exercise 3: Compare values from two lists
scores1 = [90, 85, 78]
scores2 = [88, 85, 80]

for s1, s2 in zip(scores1, scores2):
    if s1 > s2:
        print(f"{s1} > {s2}")
    elif s1 < s2:
        print(f"{s1} < {s2}")
    else:
        print(f"{s1} == {s2}")


# Exercise 4: Combine first and last names
first_names = ["John", "Jane", "Alice"]
last_names = ["Doe", "Smith", "Johnson"]

full_names = [f"{f} {l}" for f, l in zip(first_names, last_names)]
print("Full Names:", full_names)


# Exercise 5: Create a dictionary from two lists
keys = ["name", "age", "city"]
values = ["Alice", 30, "New York"]

person = dict(zip(keys, values))
print("Dictionary:", person)
