# Problem 7: Simple Interest
# Take Principal, Rate, and Time as input.
# Calculate and print the Simple Interest.
# SI = (P * R * T) / 100
p = float(input("Enter principal amount: "))
r = float(input("Enter interest rate: "))
t = float(input("Enter time in years: "))

si = (p * r * t) / 100

print("Simple Interest:", si)
