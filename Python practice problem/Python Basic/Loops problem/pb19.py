# Problem 19: Sum from 1 to N
# Take N as input and calculate the sum of all
# integers from 1 to N.

n = int(input("Enter num: "))
sum = 0
for i in range (1,n+1):
    sum = sum +i
print("sum:",sum)
