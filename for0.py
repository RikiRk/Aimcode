import math

x = int(input("Enter your number "))
y = int(math.sqrt(x))

for i in range(2, y):
    if x % i == 0:
        print("your number is not prime ", x)
    elif x % i != 0:
        print("your number is prime ", x)
    else:
    break
