def reverse(s):
    if len(s) == 0:
        return s
    else :
        return reverse(s[1:])+s[0] 

s= "python_for_nerds"

print("The string is: ",end="")
print(s)
print("the reverse string is: ",end="")
print(reverse(s))     