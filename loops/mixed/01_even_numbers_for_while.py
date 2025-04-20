# Exercise 01: Even Numbers from 1 to 20 using both for and while

print("Using for loop:")
for i in range(1, 21):
    if i % 2 == 0:
        print(i, end=" ")
print("\n")

print("Using while loop:")
num = 1
while num <= 20:
    if num % 2 == 0:
        print(num, end=" ")
    num += 1
