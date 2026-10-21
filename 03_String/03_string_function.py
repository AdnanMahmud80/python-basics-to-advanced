name = "Adnan mahmud omi"
a = len(name) # length of the string
print ("len = ",a)
b = name.endswith("Omi") # check if the string ends with "Omi"
print ("endswith = ",b)
c = name.startswith("Adnan") # check if the string starts with "Adnan"
print ("startswith = ",c)
d = name.capitalize() # capitalize the first letter of the string
print ("capitalize = ",d)
e = name.upper() # convert the string to uppercase
print ("upper = ",e)
f = name.lower() # convert the string to lowercase
print ("lower = ",f)
g = name.replace("Adnan", "Omi") # replace "Adnan" with "Omi"
print ("replace 1 = ",g)
g1 = name.replace(" ", "") # replace "space" with ("") without space
print ("replace 2 = ",g1)
h = name.split() # split the string into a list of words
print ("split = ",h)
i = name.find("Mahmud") # find the index of the substring "Mahmud"
print ("find = ",i)
j = name.count("a") # count the number of occurrences of "a"
print ("count = ",j)
k = name.isalpha() # check if the string contains only alphabetic characters
print ("isalpha = ",k)
l = name.isdigit() # check if the string contains only digits
print ("isdigit = ",l)
m = name.strip() # remove leading and trailing whitespace
print ("strip = ",m)#qs???????
n = name.center(30, "*") # center the string and fill with "*"
print ("center = ",n)
o = name.ljust(30, "-") # left justify the string and fill with "-"
print ("ljust = ",o)
p = name.rjust(30, "-") # right justify the string and fill with "-"
print ("rjust = ",p)
q = name.swapcase() # swap the case of the string
print ("swapcase = ",q)
r = name.title() # convert the string to title case
print ("title = ",r)
s = name.isupper() # check if the string is in uppercase
print ("isupper = ",s)




## --------------------------Python String Methods — Short Explanation---------------------------------------

# | Method                    | How it works                                         |
# | ------------------------- | ---------------------------------------------------- |
# | `len(name)`               | Counts all characters and spaces.                    |
# | `endswith("Omi")`         | Checks the ending of the string.                     |
# | `startswith("Adnan")`     | Checks the beginning of the string.                  |
# | `capitalize()`            | First letter uppercase, rest lowercase.              |
# | `upper()`                 | Converts all letters to uppercase.                   |
# | `lower()`                 | Converts all letters to lowercase.                   |
# | `replace("Adnan", "Omi")` | Replaces `Adnan` with `Omi`.                         |
# | `replace(" ", "")`        | Removes all spaces.                                  |
# | `split()`                 | Splits the string into a list of words.              |
# | `find("Mahmud")`          | Finds the index of the text; returns `-1` if absent. |
# | `count("a")`              | Counts occurrences of `a`.                           |
# | `isalpha()`               | Checks if all characters are letters.                |
# | `isdigit()`               | Checks if all characters are digits.                 |
# | `strip()`                 | Removes spaces from the beginning and end.           |
# | `center(30, "*")`         | Centers the string with `*` padding.                 |
# | `ljust(30, "-")`          | Aligns left with `-` padding.                        |
# | `rjust(30, "-")`          | Aligns right with `-` padding.                       |
# | `swapcase()`              | Changes uppercase to lowercase and vice versa.       |
# | `title()`                 | Capitalizes the first letter of each word.           |
# | `isupper()`               | Checks if all cased letters are uppercase.           |