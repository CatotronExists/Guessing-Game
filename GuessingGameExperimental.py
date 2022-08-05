import time
from random import randint as dice

vaild_responses =["yes", "no", "y", "n", "Yes", "YES", "No", "NO"]
yes_responses = ["yes", "y","Yes", "YES"]
no_responses = ["no", "n","No", "NO"]
game_play = True
play_again = True
guesses_left = 5
correct = False
numbers_guessed = []

###   Functions   ###
def guess_check(guess): # Checks Guess
    global guesses_left
    global correct
    numbers_guessed.insert(5, guess_number) # Adds guess to 'guess list'   
    guesses_left = guesses_left - 1 # lowers guesses left on each guess
    if guess == secret_number:
        correct = True
    else:
        correct = False
        print("You guessed the wrong number! You still have "+str(guesses_left)+" Attempt(s)")
        if(guess_number > 9):
            print("Invaild Number (Too High)") 
        if(guess_number < 1):
            print("Invaild Number (Too Low)")

def yes():
    global play_again
    global guesses_left
    global guess_number
    global correct
    play_again = 1
    guesses_left = -1
    guess_number = 0
    correct = 2
    time.sleep(1)  

def no():
    global play_again
    global difficulty
    global game_play
    global correct
    global guesses_left
    play_again = 0
    difficulty = -1 # ends program
    game_play = False
    correct = False
    guesses_left = -1       
    print("-----------------------------------------------")

while(game_play == True and play_again == True):
        print("-----------------------------------------------")
        print("Easy Difficulty\n")
        print("A number from 1 to 9 will be chosen at random")
        print("You will have 5 guesses to find the correct number")
        numbers_guessed = []
        secret_number = dice(1, 9) 
        guesses_left = 5
        print("\nYou have "+str(guesses_left)+ " guesses left")
        while(guesses_left > 0):
            guess_number = int(input("\nPut your guess here: ")) # Forces an int value
            guess_check(guess_number)
            
            if correct == False:
                while(guesses_left == 0):
                    guesses_left = False
                    print("\nYou ran out of guesses! The correct number was "+str(secret_number)+"!\n")  
                    print("Your guesses were;") 
                    print(numbers_guessed)
                    play_again = str(input("\nPlay again? (y/n) "))
                    if play_again in vaild_responses:
                        if play_again in yes_responses:
                            yes()          
                        if play_again in no_responses:
                            no()
                            break
                    else: print("Invaild Choice (y/n)")    

            while(correct == True):
                print("You guessed the correct number!\n")
                print("Your guesses were;")
                print(numbers_guessed)
                play_again = str(input("\nPlay again? (y/n) "))
                if play_again in vaild_responses:
                    if play_again in yes_responses:
                        yes()
                    if play_again in no_responses:
                        no()
                        break
                else: print("Invaild Choice (y/n)") 