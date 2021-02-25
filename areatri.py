a=input("Enter 1st side  ")
b=input("Enter 2nd side  ")
c=input("Enter 3rd side  ")
s=float(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("Area of triangle is  ",area)