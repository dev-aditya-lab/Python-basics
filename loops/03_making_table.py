tableOf = int(int(input("Enter the table of: ")))
for i in range(1, 11):
    if i == 5:
        continue
    print(f"{tableOf} x {i} = {tableOf * i}")
    
    
# This script generates and prints the multiplication table for a given number, 
# skipping the multiplication by 5.
# Usage:
#     Run the script and input the number for which you want the multiplication table.
#     The script will print the table from 1 to 10, excluding the multiplication by 5.
# Example:
#     Enter the table of: 3
#     Output:
#     3 x 1 = 3
#     3 x 2 = 6
#     3 x 3 = 9
#     3 x 4 = 12
#     3 x 6 = 18
#     3 x 7 = 21
#     3 x 8 = 24
#     3 x 9 = 27
#     3 x 10 = 30


