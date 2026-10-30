# Problem 28: Palindrome String
# Check whether a string is a palindrome.
# Example: madam -> Palindrome
# Example: hello -> Not Palindrome
a = input("Enter string: ")
l = len(a)
b=""
for i in range(l-1,-1,-1):#reverse loop
    b = b+a[i]
print(b)
if a==b:
    print('Palindrome')
else:
    print("Not palindrome")
