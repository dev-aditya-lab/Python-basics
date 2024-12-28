# **kwargs




def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        

print_kwargs(name="John", age=30, city="New York")
print_kwargs(name="John", age=3, )
print_kwargs(name="John", age=30, city="New York", email="i7O2I@example.com")