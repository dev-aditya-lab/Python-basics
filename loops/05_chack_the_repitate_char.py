inputString = input("Enter the character: ")

for char in inputString:
    if inputString.count(char) > 1:
        print(char)
        break
    


# """
# This script prompts the user to enter a string and checks for the first 
# repeated character in the input string. If a character appears more than 
# once, it prints that character and stops further checking.
# Variables:
#     inputString (str): The string input by the user.
# Usage:
#     Run the script and enter a string when prompted. The script will 
#     output the first character that repeats in the string.
# """
