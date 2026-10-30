# Problem 29: Find Maximum in a List
# Find the largest number in a list.
# Do not use the built-in max() function initially.
arr = [1,2,3,4,5]
l = len(arr)
max = arr[0]
for i in range(l):
    if(arr[i] > max):
        max = arr[i]

print(max)
