# Problem 8: Convert Seconds
# Take a total number of seconds as input.
# Convert it into hours, minutes, and remaining seconds.
total_seconds = int(input("Enter total seconds: "))

hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600

minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)
