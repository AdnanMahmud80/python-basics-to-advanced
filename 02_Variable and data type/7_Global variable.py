x = "awesome"#This is global varible. It can easily acces code all platfrom

def myfunc():
  x = "fantastic"#This is local . it only use for this function
  print(f"Python is {x}")
#function global varible initialization
def myfunc1():
  global x
  x = "Fantastic"

myfunc()
myfunc1()

print("Python is " + x)
