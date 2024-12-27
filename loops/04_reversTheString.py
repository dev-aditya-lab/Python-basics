GivenString = input("Enter the string: ")
reversedString = ""
for char in GivenString:
    reversedString = char + reversedString
print(reversedString)



# """
# This script takes a user input string and reverses it.
# The script performs the following steps:
# 1. Prompts the user to enter a string.
# 2. Initializes an empty string to store the reversed string.
# 3. Iterates over each character in the input string and prepends it to the reversed string.
# 4. Prints the reversed string.
# """

# There is also an alternative method (commented out) that reverses the string using Python's slicing feature.
# ReverseString = GivenString[::-1]
# print(ReverseString)
