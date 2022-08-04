from random import randint as dice
import time

difficulty = 0
play_again = 1
hints = 99
change_log_open = False
difficulty_select = "n/a"
hint_numbers = ["2", "3", "4"]
vaild_responses =["yes", "no", "y", "n", "Yes", "YES", "No", "NO"]
yes_responses = ["yes", "y","Yes", "YES"]
no_responses = ["no", "n","No", "NO"]
vaild_difficulty = ["1", "e", "E", "easy", "Easy", "2", "m", "M", "medium", "Medium", "3", "h", "H", "hard", "Hard", "4", "i", "I", "impossible", "Impossible", "5", "cl", "CL", "change log", "Change Log"]
vaild_difficulty_easy = ["1", "e", "E", "easy", "Easy"]
vaild_difficulty_medium = ["2", "m", "M", "medium", "Medium"]
vaild_difficulty_hard = ["3", "h", "H", "hard", "Hard"]
vaild_difficulty_impossible = ["4", "i", "I", "impossible", "Impossible"]
vaild_difficulty_change = ["5", "cl", "CL", "change log", "Change Log"]

game_play = True
while game_play == True:
    while difficulty == 0:
        print("")
        print("-----------------------------------------------")
        print("Guess the number v1.3-b1")
        print("")
        print("Choose a Difficulty")
        print("")
        print("Easy (1)")
        print("Medium (2)")
        print("Hard (3)")
        print("Impossible (4)")
        print("Change Logs (5)")
        print("")

        difficulty_select = (input("-->> "))
        # difficulty num, 1 = e, 2 = m, 3 = h, 4 = i, 5 = cl,
        if difficulty_select in vaild_difficulty:
            if difficulty_select in vaild_difficulty_easy:
                difficulty = 1
            elif difficulty_select in vaild_difficulty_medium:
                difficulty = 2
            elif difficulty_select in vaild_difficulty_hard:
                difficulty = 3
            elif difficulty_select in vaild_difficulty_impossible:
                difficulty = 4
            elif difficulty_select in vaild_difficulty_change:
                difficulty = 5
        else: 
            print("Invaild Option")
            difficulty_select = 0

    if difficulty in hint_numbers:
        while hints == 99:
            hints = str(input("Hints (y/n) "))
            if hints in yes_responses:
                hints = True
            if hints in no_responses:
                hints = False
            else: 
                print("Invaild Option")
                hints = 0

    while(difficulty == 1 and play_again == 1): # Easy
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
            guess_number = int(input("Put your guess here: ")) # Forces an int value
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
                    if play_again in no_responses:
                        play_again = 0
                        guesses_left = -1
                        game_play = False
                        print("...")        
                        print("-----------------------------------------------")
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
                game_play = False
                print("...")        
                print("-----------------------------------------------")
                break
         else: print("Invaild Choice (y/n)")           

    while(difficulty == 2 and play_again == 1): # Medium
        play_again = 0
        print("-----------------------------------------------")
        print("Medium Difficulty")
        print("")
        print("A number from 1 to 50 will be chosen at random")
        print("You will have 7 guesses to find the correct number")
        NumbersGuessed = []
        secret_number = 0
        secret_number = dice(1, 50) 
        wrong_guesses = 0
        guesses_left = 7
        guess_number = 0
        correct = 0
        print("")
        print("You have "+str(guesses_left)+ " guesses left")

        while(guesses_left > 0):
            print("")
            guess_number = int(input("Put your guess here: ")) # Forces an int value
            NumbersGuessed.insert(7, guess_number)       
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
                    if play_again in no_responses:
                        play_again = 0
                        difficulty = 0
                        guesses_left = -1
                        game_play = False
                        print("...")        
                        print("-----------------------------------------------")
                else: print("Invaild Choice (y/n)")    

            if correct == 1:
                secret_number = 1
                guess_number = 1
                guesses_left = -1  
             
            if(guess_number != secret_number):
                print("You guessed the wrong number! You still have "+str(guesses_left)+" Attempt(s)")

            if(guess_number > 50):
                print("Invaild Number (Too High)")
            if(guess_number < 1):
                print("Invaild Number (Too Low)")

            if hints == True:                        
                if(guess_number < secret_number):
                    print("The Secret Number is Higher!\n ")
                if(guess_number > secret_number):
                    print("The Secret Number is Lower\n ")
         
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
                        game_play = False
                        print("...")        
                        print("-----------------------------------------------")
                else: print("Invaild Choice (y/n)") 

    while(difficulty == 3 and play_again == 1): # Hard
        play_again = 0
        print("-----------------------------------------------")
        print("Hard Difficulty")
        print("")
        print("A number from 1 to 99 will be chosen at random")
        print("You will have 11 guesses to find the correct number")
        NumbersGuessed = []
        secret_number = 0
        secret_number = dice(1, 99) 
        wrong_guesses = 0
        guesses_left = 11
        guess_number = 0
        correct = 0
        print("")
        print("You have "+str(guesses_left)+ " guesses left")

        while(guesses_left > 0):
            print("")
            guess_number = int(input("Put your guess here: ")) # Forces an int value
            NumbersGuessed.insert(11, guess_number)       
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

                    if play_again in no_responses:
                        play_again = 0
                        guesses_left = -1
                        game_play = False
                        print("...")        
                        print("-----------------------------------------------")
                else: print("Invaild Choice (y/n)")    

                if correct == 1:
                    secret_number = 1
                    guess_number = 1
                    guesses_left = -1  
             
                if(guess_number != secret_number):
                    print("You guessed the wrong number! You still have "+str(guesses_left)+" Attempt(s)")

                if(guess_number > 99):
                    print("Invaild Number (Too High)")    
                if(guess_number < 1):
                    print("Invaild Number (Too Low)")
                
                if hints == True:                        
                    if(guess_number < secret_number):
                        print("The Secret Number is Higher!\n ")
                    if(guess_number > secret_number):
                        print("The Secret Number is Lower\n ")
         
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
                            game_play = False
                            print("...")        
                            print("-----------------------------------------------")
                    else: print("Invaild Choice (y/n)")     

    while(difficulty == 4 and play_again == 1): # Impossible
        play_again = 0
        print("-----------------------------------------------")
        print("Impossible Difficulty")
        print("")
        print("A number from 1 to 999 will be chosen at random")
        print("You will have 20 guesses to find the correct number")
        NumbersGuessed = []
        secret_number = 0
        secret_number = dice(1, 999) 
        wrong_guesses = 0
        guesses_left = 20
        guess_number = 0
        correct = 0
        print("")
        print("You have "+str(guesses_left)+ " guesses left")

        while(guesses_left > 0):
            print("")
            guess_number = int(input("Put your guess here: ")) # Forces an int value
            NumbersGuessed.insert(20, guess_number)       
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

                    if play_again in no_responses:
                        play_again = 0
                        guesses_left = -1
                        game_play = False
                        print("...")        
                        print("-----------------------------------------------")
                else: print("Invaild Choice (y/n)")    

            if correct == 1:
                secret_number = 1
                guess_number = 1
                guesses_left = -1  
             
            if(guess_number != secret_number):
                print("You guessed the wrong number! You still have "+str(guesses_left)+" Attempt(s)")

            if(guess_number > 999):
                print("Invaild Number (Too High)") 
            if(guess_number < 1):
                print("Invaild Number (Too Low)")

            if hints == True:                        
                if(guess_number < secret_number):
                    print("The Secret Number is Higher!\n ")
                if(guess_number > secret_number):
                    print("The Secret Number is Lower\n ")
         
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
                        game_play = False
                        print("...")        
                        print("-----------------------------------------------")
                else: print("Invaild Choice (y/n)")     

    while(difficulty == 5): # Change Log
        change_log_page = 1
        print("-----------------------------------------------")
        print("Guess the number       Current Version: v1.3-b1")
        print("")
        print("Version 1.3-b1 (3/08/2022)")
        print("- New Difficulty option, Choose between Easy, Medium,\nHard and Impossible.\nAdded Option to use letters/word to choose a difficulty.\nMedium and above have togglable hints (Higher/Lower).\nOptimised code by making it longer :)\nChange log can now be closed.")
        print("")
        print("Version 1.2.1")
        print("- Removed prints used for testing")
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
        change_log_page = input("Close (y/y)\n-->> ")
        if change_log_page == 'y':
            change_log_page = 0
            difficulty = 0
        else: print("...")            
