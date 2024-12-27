myList = ["aditya", "ishika", "manshi", "ishika", "Gupta", "pathak"]

uniqueList = set()

for item in myList:
    if item in uniqueList:
        print(item)
        break
    else:
        uniqueList.add(item)
        
        

# """
# This script identifies and prints the first duplicate element in a list of strings.
# The list `myList` contains a series of names. The script iterates through this list and uses a set `uniqueList` to keep track of unique elements encountered so far. When a duplicate element is found (i.e., an element that is already in `uniqueList`), the script prints that element and stops further execution.
# Variables:
#     myList (list): A list of strings containing names.
#     uniqueList (set): A set to store unique elements from `myList`.
# The script performs the following steps:
# 1. Initializes an empty set `uniqueList`.
# 2. Iterates through each element in `myList`.
# 3. Checks if the current element is already in `uniqueList`.
# 4. If a duplicate is found, prints the duplicate element and breaks the loop.
# 5. If no duplicate is found, adds the current element to `uniqueList`.
# Example:
#     Given the list ["aditya", "ishika", "manshi", "ishika", "Gupta", "pathak"],
#     the script will print "ishika" as it is the first duplicate element.
# """
