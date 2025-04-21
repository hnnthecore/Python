# Exercise 1: Basic enumerate with list
names = ["Alice", "Bob", "Charlie"]
for i, name in enumerate(names):
    print(f"{i}: {name}")  # Index starts from 0


# Exercise 2: Enumerate starting from 1
for i, name in enumerate(names, start=1):
    print(f"{i}. {name}")  # Index starts from 1


# Exercise 3: Enumerate over a string
word = "hello"
for i, char in enumerate(word):
    print(f"Character {i}: {char}")


# Exercise 4: Replace element at even index with "X"
colors = ["red", "green", "blue", "yellow", "purple"]
for i, color in enumerate(colors):
    if i % 2 == 0:
        colors[i] = "X"
print("Updated colors:", colors)  # ['X', 'green', 'X', 'yellow', 'X']


# Exercise 5: Track position of target word
sentence = "the quick brown fox jumps over the lazy dog".split()
for i, word in enumerate(sentence):
    if word == "the":
        print(f"'the' found at position {i}")


# Exercise 6: Create a numbered menu
menu = ["Start Game", "Load Game", "Options", "Exit"]
print("=== Main Menu ===")
for i, item in enumerate(menu, start=1):
    print(f"{i}) {item}")


# Exercise 7: Reverse with enumerate
numbers = [10, 20, 30, 40]
for i, val in enumerate(reversed(numbers)):
    print(f"{i}: {val}")  # 0: 40, 1: 30, ...


# Exercise 8: Zip + enumerate together
questions = ["Capital of France?", "5 + 7?", "Color of the sky?"]
answers = ["Paris", "12", "Blue"]

for i, (q, a) in enumerate(zip(questions, answers), start=1):
    print(f"Q{i}: {q} → A: {a}")
