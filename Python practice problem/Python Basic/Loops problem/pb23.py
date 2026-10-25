# Problem 23: Sum of Digits
# Take a non-negative integer as input and calculate
# the sum of its digits.
# Example: 123 -> 1 + 2 + 3 = 6

n = int(input("Enter a number: "))
total = 0

while n > 0:
    digit = n % 10
    total = total + digit
    n = n // 10

print("Sum of digits:", total)
