# move ticket pricing based on age and day of the week

age= int(input("Enter your age: "))
day= input("Enter the day of the week: ")


price = 12 if age >= 18 else 8
# the above line is a short hand for the if else statement that means is age is greater than or equal to 18 then price is 12 else price is 8
if day == "Wednesday":
    price -= 2
    
print("Your ticket price is ${price}")




# if age <18: 
#     if day == "Wednesday":
#         print("Your ticket price is $6")
#     else:
#         print("Your ticket price is $8")
# else:
#     if day == "Wednesday":
#         print("Your ticket price is $10")
#     else:
#         print("Your ticket price is $12")
        
        
        
