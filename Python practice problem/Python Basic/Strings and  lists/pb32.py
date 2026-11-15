# Problem 32: Count Even and Odd
# Count how many even and odd numbers are present
# in a list.
arr = [1,2,3,4,5]
l = len(arr)
sum = 0
c=0
s=0
for i in range (l):
    if arr[i]%2==0:
        c = c+1
    else:
        s = s+1

print(c,s)
