while True:
    n = int(input("Enter the number you got in exam - "))
    if 100 >= n >= 91:
        print("Your grade is O")
    elif n >= 81 >= 90:
        print("Your grade is A")
    elif 80 >= n >= 71:
        print(" Your grade B+")
    elif 50 >= n >= 61:
        print("Your grade C ")
    elif n == 30:
        print("You are passed")
    elif n <= 49:
        print("You have failed")
    else:
        print("You have enter Wrong number")
