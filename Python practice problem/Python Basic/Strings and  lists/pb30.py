# Problem 30: Find Minimum in a List
# Find the smallest number in a list.
# Do not use the built-in min() function initially.
arr = [1,2,3,4,5]
l = len(arr)
min = arr[0]
for i in range(l):
    if(arr[i] < min):
        min = arr[i]

print(min)
