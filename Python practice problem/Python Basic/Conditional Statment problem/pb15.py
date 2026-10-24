# Problem 15: Grade Calculator
# Take marks as input and calculate the grade:
# 80 or above = A+
# 70-79 = A
# 60-69 = A-
# 50-59 = B
# 40-49 = C
# Below 40 = F
marks = int(input("Enter your marks: "))

if marks >= 80:
    print("Grade: A+")
elif marks >= 70:
    print("Grade: A")
elif marks >= 60:
    print("Grade: A-")
elif marks >= 50:
    print("Grade: B")
elif marks >= 40:
    print("Grade: C")
else:
    print("Grade: F")
