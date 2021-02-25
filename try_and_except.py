n = int(input("Enter your number - "))

n1 = int(input("Enter your second number - "))
try:
    print("Total - ", int(n) + int(n1))

except Exception as e:
    print(e)

print("This is the try and except using program")
