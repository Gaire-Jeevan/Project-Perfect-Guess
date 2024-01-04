import random
randNumber = random.randint(1, 100)
userGuess = None # it is defined lateron so while entering into loop userguess is not defined
guesses = 0
while(userGuess != randNumber):
    userGuess = int(input("Enter any number between 1 to 100:- "))
    guesses += 1
    if(userGuess==randNumber):
        print("You guessed it right!")
    else:
        if(userGuess>randNumber):
            print("You guessed it wrong! Enter a smaller number") 
        else:
            print("You guessed it wrong! Enter a larger number")  

print(f"You guessed the number in {guesses} guesses")

with open("highscore.txt", "w") as f:
    highscore = int(f.read())

if(guesses<hiscore):
    print("You have just broken the high score!")
    with open("hiscore.txt","w") as f:
        f.write(str(guesses))