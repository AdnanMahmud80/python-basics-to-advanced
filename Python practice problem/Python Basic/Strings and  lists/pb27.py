# Problem 27: Reverse a String
# Take a string as input and print it in reverse order.
a = input("Enter string: ")
l = len(a)
b=""
for i in range(l-1,-1,-1):#reverse loop
    b = b+a[i]
print(b)
