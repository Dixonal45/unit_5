# # created by Allison Dixon
# # last updated October 17, 2019
# # unit 5 daily exercises
#
# import random
#
# # exercise 1: counting up or down based on user input
#
# print("Make sure the numbers you input and their order make sense.")
# m = int(input("What do you want the lowest value to be?"))
# n = int(input("What do you want the highest value to be?"))
# for x in range(m, n + 1):
#     print(x)
# if m > n + 1:
#     for x in range(m, n - 1, -1):
#         print(x)
#
# # exercise 2: loops printing 10 to 20 and every even number from 2 to 40
#
# for x in range(10, 21):
#     print(x)
#
# for x in range(2, 41, 2):
#     print(x)
#
# # exercise 3: program that prompts user to input a positive integer
#     # and prints the multiplication table of that number (up to 12)
#
# n = int(input("Please give a positive integer."))
# for x in range(13):
#     print(n, "*", x, "=", n * x)
#
# # exercise 4: program generates 10 random numbers and prints out the sum of the even and odd numbers
#
# even_sum = 0
# odd_sum = 0
# for x in range(10):
#     num = random.randint(1, 100)
#     if (num % 2) == 0:
#         even_sum = even_sum + num
#     else:
#         odd_sum = odd_sum + num
# print(even_sum)
# print(odd_sum)
#
# # exercise 5: sum of all the multiples of 3 o 5 below 1000
#
# multiples = 0
# for x in range(3, 1000):
#     if (x % 3) == 0 or (x % 5) == 0:
#         multiples = multiples + x
# print(multiples)
#
# # exercise 6: reads a number and prints a right triangle using "*"
#
# x = 0
# num = int(input("Give me a number."))
# while x < num + 1:
#     print("*" * x)
#     x = x + 1
#
# exercise 7: takes integer inputs until user presses 'q' and then prints avg and product of all numbers

total = 0
while True:
    num = input("Give me a number.")
    if num == "q":
        break
