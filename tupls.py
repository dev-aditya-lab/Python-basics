myTuple = (1, 2, 3, 4, 5)

# count the number of times 1 appears in the tuple
print(myTuple.count(1))

# print the tuple
print(myTuple[0])

# print the length of the tuple
print(len(myTuple))

# print the first element of the tuple
print(myTuple[0])

# print the last element of the tuple
print(myTuple[-1])

# print the first 3 elements of the tuple
print(myTuple[0:3])

# print the last 3 elements of the tuple
print(myTuple[-3:])

# print the tuple in reverse
print(myTuple[::-1])

# convert the tuple to a list
myList = list(myTuple)

# print the list
print(myList)

# convert the list to a tuple
myTuple = tuple(myList)

# print the tuple
print(myTuple)

# unpack the tuple
a, b, c, d, e = myTuple

# print the unpacked values
print(a)
print(b)
print(c)
print(d)
print(e)

# create a tuple with one element
myTuple = (1,)
print(myTuple)

# create a tuple without parentheses
myTuple = 1, 2, 3
print(myTuple)

# create a tuple with multiple data types
myTuple = (1, "John", 1.23)

# print the tuple
print(myTuple)

# create a tuple using the tuple() constructor
myTuple = tuple((1, 2, 3, 4, 5))

# print the tuple
print(myTuple)

# create a tuple using a list
myList = [1, 2, 3, 4, 5]
myTuple = tuple(myList)

# print the tuple
print(myTuple)

# create a tuple using a string
myTuple = tuple("Hello")
print(myTuple)

# create a tuple using a range
myTuple = tuple(range(5))
print(myTuple)
