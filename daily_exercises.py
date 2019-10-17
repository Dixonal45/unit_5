# created by Allison Dixon
# last updated October 17, 2019
# unit 5 daily exercises

import random

# exercise 1: counting up or down based on user input

print("Make sure the numbers you input and their order make sense.")
m = int(input("What do you want the lowest value to be?"))
n = int(input("What do you want the highest value to be?"))
for x in range(m, n + 1):
    print(x)
if m > n + 1:
    for x in range(m, n - 1, -1):
        print(x)

# exercise 2: loops printing 10 to 20 and every even number from 2 to 40

for x in range(10, 21):
    print(x)

for x in range(2, 41, 2):
    print(x)

# exercise 3: program that prompts user to input a positive integer
    # and prints the multiplication table of that number (up to 12)

n = int(input("Please give a positive integer."))
for x in range(13):
    print(n, "*", x, "=", n * x)

# exercise 4: program generates 10 random numbers and prints out the sum of the even and odd numbers

even_sum = 0
odd_sum = 0
for x in range(1, 100):
    random.randint(10)
    if (x % 2) == 0:
        even_sum = even_sum + x
    else:
        odd_sum = odd_sum + x
