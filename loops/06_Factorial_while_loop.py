num = int(input("Enter a number: "))

factorial = 1
i = 1

while i <= num:
    factorial *= i
    i += 1

print(f"The factorial of {num} is {factorial}")


# """
# This script calculates the factorial of a given number using a while loop.
# The user is prompted to enter a number, and the script computes the factorial
# of that number by multiplying all integers from 1 up to the entered number.
# Variables:
#     num (int): The number for which the factorial is to be calculated.
#     factorial (int): The result of the factorial calculation.
#     i (int): Loop counter used to iterate from 1 to the entered number.
# """

