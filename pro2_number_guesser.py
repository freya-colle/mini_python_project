import random

input_number = input("Choose a number to generate random numbers: ")
guesses = 0

if input_number.isdigit():
    if int(input_number) <= 0:
        print("Please enter a number larger than zero")
        quit();
    else:
        random_num = random.randint(0, int(input_number))
else:
    print("Enter a number please. ")

while True:
    guesses += 1
    user_guess = input("Guess a number: ")
    if (user_guess.isdigit()):
        if (int(user_guess) == random_num):
            print("You got it right")
            break;
        print("You get it wrong")
    else:
        print("Please enter a number")
        continue;
    
print(f"You got it in {guesses} guesses")

    