def reverse(s):
  str=""
  for i in s :
    str = i + str
  return str
s = 'python_for_nerds'
print("the string is: ",end="")
print(s)
print("The reverse string is: ",end="")
print(reverse(s))