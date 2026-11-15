# Problem 21: Factorial
# Take a non-negative integer as input and calculate
# its factorial.
# Example: 5! = 5 * 4 * 3 * 2 * 1 = 120
n = int(input("Enter num:"))
fact = 1
for i in range (1,n+1):
    fact = fact * i

print(fact)


