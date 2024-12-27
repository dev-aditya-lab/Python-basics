userDetails = {
    "name": "John",
    "age": 30,
    "city": "New York"
}



# print the entire dictionary
print(userDetails)

# print the value of a specific key
print(userDetails["name"])

# print the value of a specific key using get()
print(userDetails.get("name"))

# print the keys of the dictionary
print(userDetails.keys())

# print the values of the dictionary
print(userDetails.values())

# print the key-value pairs of the dictionary
print(userDetails.items())

# add a new key-value pair to the dictionary
# if the key already exists, the value will be updated
# if the key does not exist, a new key-value pair will be added
userDetails["email"] = "i7O2I@example.com"

# update the value of a key
userDetails["name"] = "Jane"

# remove a key-value pair from the dictionary
userDetails.pop("city")

# remove all key-value pairs from the dictionary
userDetails.clear()

# delete the dictionary
del userDetails

