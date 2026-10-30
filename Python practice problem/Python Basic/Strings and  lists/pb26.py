# Problem 26: Count Vowels
# Take a string as input and count the vowels.
# Vowels: a, e, i, o, u
# Count both uppercase and lowercase vowels.
a = input("Enter string: ")
l = len(a)
c = 0
d=0
for i in a:
    if(i in "aeiou"):
        c +=1
    elif(i in "AEIOU"):
        d+=1

print("Upper vowels:",d,"\n Lower vowels: ",c)
