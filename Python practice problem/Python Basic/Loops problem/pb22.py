# Problem 22: Count Digits
# Take a non-negative integer as input and count
# how many digits it contains.
# Example: 12345 -> 5 digits


n = int (input("Enter Number: "))
count  = 0
while(n>0):
    digit = n%10
    count  +=1
    # print(digit)
    n = n//10
print(count)
