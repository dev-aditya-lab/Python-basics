# Write a program to find the sum of all even numbers from 1 to given no.

num = int(input("Enter a number: "))
sum = 0
for i in range(2, num + 1, 2):
    sum += i
print(sum)