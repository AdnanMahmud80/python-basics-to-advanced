a = int(input("Enter num :"))
for i in range (2,a):
    if (a%i== 0):
        print("not prime")
        break
    else:
        print("prime")
        break

#A prime number is divisible only by 1 and itself with no remainder.

# Example: 7 is a prime number because 7 % 2, 7 % 3, and 7 % 4 are not 0.
