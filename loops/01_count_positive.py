# Description: Count the number of positive numbers in a list

myList = [1,-2,-3,4,5,-6,7,8,-9,10]

count = 0
for i in myList:
    if -i < 0:
        count += 1
        
print(count)