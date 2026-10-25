# Problem 24: Reverse a Number
# Take a non-negative integer as input and reverse it.
# Example: 1234 -> 4321
n = int(input("Enter a number: "))
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

print("Reversed number:", reverse)
