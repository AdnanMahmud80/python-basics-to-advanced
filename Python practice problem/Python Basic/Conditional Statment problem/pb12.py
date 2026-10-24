# Problem 12: Largest of Three Numbers
# Take three numbers as input and find the largest.
a = int (input("Enter 1st digit:"))
b = int (input("Enter 2nd digit:"))
c = int (input("Enter 3rd digit:"))


if (a<b):
    if(b>c):
     print("Largest Num:",b)
    else:
       print("Largest Num:",c)
elif(a>b):
    if(a>c):
     print("Largest Num :",a)
    else:
           print("Largest Num:",c)
else:
    print ("All Number is equal")
