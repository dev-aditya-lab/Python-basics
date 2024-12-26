myList = [123, "John", "Doe", 123.51]

# print the list
print(myList)

# print the length of the list
print(len(myList))

# print the first element of the list
print(myList[0])

# print the last element of the list
print(myList[-1])

# print the first 3 elements of the list
print(myList[0:3])

# print the last 3 elements of the list
print(myList[-3:])

# print the list in reverse
print(myList[::-1])

# add an element to the list at the end
myList.append("New Element")

# add an element to the list at a specific index
myList.insert(1, "New Element")

# remove an element from the list
myList.remove("John")

# remove the last element from the list
myList.pop()

# remove the first element from the list
myList.pop(0)

# remove all elements from the list
myList.clear()

# sort the list
myList.sort()
