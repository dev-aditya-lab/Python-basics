# *args

def sum(*args):
    total = 0
    for num in args:
        total += num
    return total

# we can pass any number of arguments

print(sum(1, 2, 3, 4, 5))


# another way
# def sum(*args):
#     return sum(args)