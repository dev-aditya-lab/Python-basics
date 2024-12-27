marks = int(input("Enter your marks: "))

if marks > 100 or marks < 0:
    print("Invalid marks")
    exit()

if marks >= 90:
    print("A grade")
elif marks >= 80:
    print("B grade")
elif marks >= 70:
    print("C grade")
elif marks >= 60:
    print("D grade")
else:
    print("F grade")