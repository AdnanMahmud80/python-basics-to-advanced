marks1 = int(input("Enter marks:"))
marks2 = int (input("Enter marks:"))
marks3 = int (input ("Enter marks:"))

total_percentage = 100*(marks1 + marks2 + marks3)/300

if (total_percentage>40):
 print("you passed",total_percentage)
else:
 print("you fail",total_percentage)

