# Strings in python

name = "aditya"
print(name)

# print the length of the string
print(len(name))

# print the first character of the string
print(name[0])

# print the last character of the string
print(name[-1])

# print the first 3 characters of the string
print(name[0:3])

# print the last 3 characters of the string
print(name[-3:])

# print the string in reverse
print(name[::-1])

# convert the string to uppercase
print(name.upper())

# convert the string to lowercase
print(name.lower())

# check if the string starts with a specific character
print(name.startswith("a"))

# check if the string ends with a specific character
print(name.endswith("a"))

# check if the string contains a specific character
print("a" in name)

# check if the string does not contain a specific character
print("z" not in name)

# replace a character in the string
# hear 'a' is replaced with 'z'
print(name.replace("a", "z"))

# split the string into a list of substrings
print(name.split("d"))

# join the elements of a list into a string
print("-".join(["a", "d", "i", "t", "y", "a"]))

# remove leading and trailing whitespaces from the string
name = " ishika "
print(name.strip())

# remove leading whitespaces from the string
name = " aditya "
print(name.lstrip())

# remove trailing whitespaces from the string
name = " aditya "
print(name.rstrip())

# check if the string is alphanumeric
name = "aditya123"
print(name.isalnum())
# output: True

# check if the string is alphabetic
name = "aditya"
print(name.isalpha())
# output: True

# check if the string is numeric
name = "123"
print(name.isnumeric())
# output: True

# check if the string is decimal
name = "123.45"
print(name.isdecimal())
# output: True

# check if the string is digit
name = "123"
print(name.isdigit())
# output: True

# check if the string is identifier
# An identifier is a name given to entities like class, functions, variables, etc. It helps to differentiate one entity from another.
name = "aditya"
print(name.isidentifier())
# output: True

# hear frist_name, last_name = name.split(" ") 

name = "aditya gupta"
frist_name, last_name = name.split(" ")

