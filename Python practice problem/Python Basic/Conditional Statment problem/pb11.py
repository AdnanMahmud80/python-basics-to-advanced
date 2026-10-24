# Problem 11: Find the Larger Number
# Take two numbers as input and print the larger number.
# If both numbers are equal, display that information.
a = int (input("Enter 1st digit:"))
b = int (input("Enter 2nd digit:"))

if (a<b):
    print("Largest Num:",b)
elif(a>b):
    print("Largest Num :",a)
else:
    print ("Both Num is equal")

