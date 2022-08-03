from random import randint as dice
import time
print("")
print("-----------------------------------------------")
print("Guess the number v1.2")
print("")
print("Choose a Difficulty")
print("")
print("Easy (1)")
print("Medium (2) (unfinished)")
print("Hard (3) (unfinished)")
print("Impossible (4) (unfinished)")
print("Change Logs (5)")
print("")
difficulty = 0
play_again = 1
difficulty_select = "n/a"
vaild_responses =["yes", "no", "y", "n", "Yes", "YES", "No", "NO"]
yes_responses = ["yes", "y","Yes", "YES"]
no_responses = ["no", "n","No", "NO"]
difficulty_select = int(input("-->> "))


# difficulty num, 1 = e, 2 = m, 3 = h, 4 = i, 5 = cl,

while(difficulty == 0):
    if(difficulty_select == 1):
        difficulty = 1
    if(difficulty_select == 2):
        difficulty = 2
    if(difficulty_select == 3):
        difficulty = 3
    if(difficulty_select == 4):
        difficulty = 4
    if(difficulty_select == 5):
        difficulty = 5

while(difficulty == 1 and play_again == 1):
    play_again = 0
    print("-----------------------------------------------")
    print("Easy Difficulty")
    print("")
    print("A number from 1 to 9 will be chosen at random")
    print("You will have 5 guesses to find the correct number")
    NumbersGuessed = []
    secret_number = 0
    secret_number = dice(1, 9) 
    wrong_guesses = 0
    guesses_left = 5
    guess_number = 0
    correct = 0
    print("")
    print("You have "+str(guesses_left)+ " guesses left")

    while(guesses_left > 0):
        print("")
        guess_number = int(input("Put your guess here:")) # Forces an int value
        NumbersGuessed.insert(5, guess_number)       
        guesses_left = guesses_left - 1 # lowers guesses left on each guess
        
        while(guess_number == secret_number):
         print("You guessed the correct number!")
         print("")
         print("Your guesses were;")
         print(NumbersGuessed)
         print("")
         play_again = str(input("Play again? (y/n) "))
         if play_again in vaild_responses:
            if play_again in yes_responses:
                play_again = 1
                guesses_left = -1
                guess_number = 0
                correct = 1
                time.sleep(1)
                break
            
            if play_again in no_responses:
                play_again = 0
                print("...")        
                print("-----------------------------------------------")
                break
         else: print("Invaild Choice (y/n)")    

        if correct == 1:
            secret_number = 1
            guess_number = 1
            guesses_left = -1  
             

        if(guess_number != secret_number):
         print("You guessed the wrong number! You still have "+str(guesses_left)+" Attempt(s)")

        if(guess_number > 9):
         print("Invaild Number (Too High)")
 
        if(guess_number < 1):
         print("Invaild Number (Too Low)")
         
        while (guesses_left == 0):
         print("")
         print("You ran out of guesses! The correct number was "+str(secret_number)+"!")  
         print("")    
         print("Your guesses were;") 
         print(NumbersGuessed)
         print("")
         play_again = str(input("Play again? (y/n) "))
         if play_again in vaild_responses:
            if play_again in yes_responses:
                play_again = 1
                guesses_left = -1
                secret_number = 0
                time.sleep(1)
            
            if play_again in no_responses:
                play_again = 0
                print("...")        
                print("-----------------------------------------------")
                break
         else: print("Invaild Choice (y/n)")  

         

while(difficulty == 2):
    print("Medium Difficulty Chosen")
    print("")
    print("A number from 1 to 50 will be chosen at random")
    print("You will have 7 guesses to find the correct number")
    NumbersGuessed = []
    secret_number = 0
    secret_number = dice(1, 50)
    #print(secret_number)
    # Used to test 
    wrong_guesses = 0
    guesses_left = 7
    guess_number = 0
    print("")
    print("You have "+str(guesses_left)+ " guesses left")
    #print("start check")

    while(guesses_left > 0):
        guess_number = 0
        print("")
        guess_number = int(input("Put your guess here:")) # Forces an int value
        NumbersGuessed.insert(7, guess_number) 
        guesses_left = guesses_left - 1 # lowers guesses left on each guess

        if(guess_number == secret_number):
         print("You guessed the correct number!")
         print("")
         print("Play Again?")
         print("")
         print("-----------------------------------------------")
         break

        if(guess_number != secret_number):
        #print("wrong check")
         print("You guessed the wrong number! You still have "+str(guesses_left)+" Attempt(s)")

        if(guess_number > 50):
         print("Invaild Number (Too High)")
        
        if(guess_number > secret_number):
            print("Try a lower number!")
        
        if(guess_number < secret_number):
            print("Try a higher number!")
 
        if(guess_number < 1):
         print("Invaild Number (Too Low)")
         
        if(guesses_left == 0):
         print("")
         print("You ran out of guesses! The correct number was "+str(secret_number)+"!")  
         print("")    
         print("Your guesses were;") 
         print(NumbersGuessed)
         print("")
         print("Play again?")
         print("-----------------------------------------------")
         

while(difficulty == 3):
    print("Hard Difficulty Chosen")
    print("")
    print("A number from 1 to 100 will be chosen at random")
    print("You will have 10 guesses to find the correct number")
    NumbersGuessed = []
    secret_number = 0
    secret_number = dice(1, 100)
    #print(secret_number)
    # Used to test 
    wrong_guesses = 0
    guesses_left = 10
    guess_number = 0
    print("")
    print("You have "+str(guesses_left)+ " guesses left")

    while(guesses_left > 0):
        guess_number = 0
        print("")
        guess_number = int(input("Put your guess here:")) # Forces an int value
        NumbersGuessed.insert(10, guess_number) 
        #print(NumbersGuessed)  
        #print("You guessed "+str(guess_number))
        guesses_left = guesses_left - 1 # lowers guesses left on each guess
        #print("guess_left check "+str (guesses_left))

        if(guess_number == secret_number):
         print("You guessed the correct number!")
         print("")
         print("Play Again?")
         print("")
         print("-----------------------------------------------")
         break

        if(guess_number != secret_number):
        #print("wrong check")
         print("You guessed the wrong number! You still have "+str(guesses_left)+" Attempt(s)")

        if(guess_number > 100):
         print("Invaild Number (Too High)")
        
        if(guess_number > secret_number):
            print("Try a lower number!")
        
        if(guess_number < secret_number):
            print("Try a higher number!")
 
        if(guess_number < 1):
         print("Invaild Number (Too Low)")
         
        if(guesses_left == 0):
         print("")
         print("You ran out of guesses! The correct number was "+str(secret_number)+"!")  
         print("")    
         print("Your guesses were;") 
         print(NumbersGuessed)
         print("")
         print("Play again?")
         print("-----------------------------------------------")
         break    

while(difficulty == 4):
    print("Impossible Difficulty Chosen")
    print("")
    print("A number from 1 to 999 will be chosen at random")
    print("You will have 15 guesses to find the correct number")
    NumbersGuessed = []
    secret_number = 0
    secret_number = dice(1, 999)
    #print(secret_number)
    # Used to test 
    wrong_guesses = 0
    guesses_left = 15
    guess_number = 0
    print("")
    print("You have "+str(guesses_left)+ " guesses left")
    #print("start check")

    while(guesses_left > 0):
        guess_number = 0
        print("")
        guess_number = int(input("Put your guess here:")) # Forces an int value
        NumbersGuessed.insert(15, guess_number) 
        #print(NumbersGuessed)  
        #print("You guessed "+str(guess_number))
        guesses_left = guesses_left - 1 # lowers guesses left on each guess
        #print("guess_left check "+str (guesses_left))

        if(guess_number == secret_number):
         print("You guessed the correct number!")
         print("")
         print("Play Again?")
         print("")
         print("-----------------------------------------------")
         break

        if(guess_number != secret_number):
        #print("wrong check")
         print("You guessed the wrong number! You still have "+str(guesses_left)+" Attempt(s)")

        if(guess_number > 999):
         print("Invaild Number (Too High)")
        
        if(guess_number > secret_number):
            print("Try a lower number!")
        
        if(guess_number < secret_number):
            print("Try a higher number!")
 
        if(guess_number < 1):
         print("Invaild Number (Too Low)")
         
        if(guesses_left == 0):
         print("")
         print("You ran out of guesses! The correct number was "+str(secret_number)+"!")  
         print("")    
         print("Your guesses were;") 
         print(NumbersGuessed)
         print("")
         print("Play again?")
         print("-----------------------------------------------")
         break  


while(difficulty == 5):
    change_log_page = 1
    print("-----------------------------------------------")
    print("Guess the number          Current Version: v1.2")
    print("")
    print("Version 1.2 (28/08/2022)")
    print("- Updated starting menu")
    print("")
    print("Version 1.1 (27/08/2022)")
    print("- Play again option added")
    print("")
    print("Version 1.0 (25/08/2022)")
    print("- Release")
    print("")
    print("-----------------------------------------------")
    difficulty = 99


    

