a=int(input("Enter the 1st number : "))
b=int(input("Enter the 2nd number : "))
c=int(input("Enter the 3rd number : "))
print("The Max Num is ", end="")
if b <= a >= c:
    print(a)
elif a <= b >= c:
    print(b)
elif b <= c >= a:
    print(c)