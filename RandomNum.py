from random import randint 

secret_num = randint(1,15)

user_num = -1

try_count= 1 

print("secret number will between 1 to 15 ")

while secret_num != user_num:
    print("%d try : " %try_count , end="")
    user_num = int(input())
    if user_num < secret_num:
        print("Too low")
    elif user_num > secret_num:
        print("Too high")
    else:
        print("Right")
    try_count += 1                    
