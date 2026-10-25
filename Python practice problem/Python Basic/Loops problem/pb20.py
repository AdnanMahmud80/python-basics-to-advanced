# Problem 20: Multiplication Table
# Take a number as input and print its multiplication
# table from 1 to 10.

n = int(input("Enter num: "))

for i in range (1,n+1):
    print(f"{n}x{i}={n*i}")


