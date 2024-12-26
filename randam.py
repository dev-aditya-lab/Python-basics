import random

# generate a random number between 0 and 1
print(random.random())

# generate a random number between 1 and 10
print(random.randint(1, 10))

# generate a random number from a list
print(random.choice([1, 2, 3, 4, 5]))

# generate a random number from a list
# k=5 means generate 5 random numbers
print(random.choices([1, 2, 3, 4, 5], k=5))
print(random.choices([1, 2, 3, 4, 5], k=10))

# generate a random number from a list
# weights=[1, 2, 3, 4, 5] means the probability of each number is 1/2/3/4/5
print(random.choices([1, 2, 3, 4, 5], weights=[1, 4, 3, 4, 5], k=5))


# shuffle a list
print(random.shuffle([1, 2, 3, 4, 5]))