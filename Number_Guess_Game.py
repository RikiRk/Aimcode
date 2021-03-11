import random
n = random.randint(1, 20)
print(n)
print("You have to guess the number and you have only 10 guesses, Let's start the game then ")
print("The first hints is , The number is between 1 to 20 ")
number_of_guesses = 0
while not int(number_of_guesses) > 9:
    user_input = int(input("Enter your number: "))
    number_of_guesses = int(number_of_guesses + 1)
    print("Used of guess- ", int(number_of_guesses))
    if user_input == n:
        print("You Won ... ! You've successfully enter the correct answer")
        break
    elif user_input > n:
        print("You have enter the greater number , Hint: try to guess lesser ")
    elif user_input < n:
        print("You have enter the lesser number , Hint: try to guess greater")
    else:
        print("You have use your all of your guesses, you have been failed")
print('you have used your all hints and usage of guess ! Today is your lucky day !!')
print("Hope, you like this game !! ")
