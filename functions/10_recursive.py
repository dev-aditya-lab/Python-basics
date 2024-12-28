# """
# Calculate the factorial of a non-negative integer n using recursion.
# The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.
# It is denoted by n! and defined as:
# - 0! = 1
# - n! = n * (n-1) * (n-2) * ... * 1 for n > 0
# Args:
#     n (int): A non-negative integer whose factorial is to be computed.
# Returns:
#     int: The factorial of the input integer n.
# Raises:
#     RecursionError: If the maximum recursion depth is exceeded.
#     ValueError: If n is a negative integer.
# Examples:
#     >>> factorial(5)
#     120
#     >>> factorial(0)
#     1
# """


# it is a function that calls itself. its called a recursive function

def factorial(n):
    if n == 0: # base case that means exit condition
        return 1
    else:
        return n * factorial(n - 1)
    

print(factorial(4))