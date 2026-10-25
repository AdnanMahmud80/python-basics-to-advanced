# Problem 18: Print Even Numbers
# Take N as input and print all even numbers
# from 1 to N.
n = int(input("Enter num: "))
for i in range (1,n+1):
    if (i%2==0):
        print("Even: ",i)
    
