import random

playing = True
number = str(random.randint(0, 9))

print ("Welcome to the Guess the Number Game!,  I have selected a number between 0 and 9. Can you guess what it is?")
print ("the game ends when you guess the number correctly")
while playing:
    guess = input("Enter your guess: ")
    if number == guess:
        print("Congratulations! You guessed the number correctly!")
        playing = False
    else:
        print("Sorry, that's not the correct number. Try again!")