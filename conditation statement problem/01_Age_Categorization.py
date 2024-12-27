# age group categorization based on the input age

inputage = input("Enter your age: ")
age = int(inputage)
if age <=13:
    print("You are a child")
elif age <=20: 
    print("You are an Teenager")
elif age <60:
    print("You are an Adult")
elif age >=60:
    print("You are an old person")